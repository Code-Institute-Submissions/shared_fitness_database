import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import math

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SUPER_SECRET_KEY')
app.config['MONGO_DBNAME'] = "gym_life_db"
app.config['MONGO_URI'] = os.environ.get("MONGO_SFDB_URI")

mongo = PyMongo(app)


"""ROUTES"""

""" INDEX/HOME """
# The below route will display the home page on index.html, the function below is for the pagination on the index page,
# the function which will choose a limit for the number of exercises per page, count the total number
# of exercises and then will then provide the logic for what exercises will be shown on each page
@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def index():
    per_page = 3
    page = int(request.args.get('page', 1))
    total = mongo.db.exercises.count_documents({})
    exercises = mongo.db.exercises.find().skip((page - 1) * per_page).limit(per_page)
    pages = range(1, int(math.ceil(total / per_page)) + 1)
    return render_template('index.html', exercises=exercises, page=page, pages=pages, total=total)


""" SEARCH """
@app.route('/search', methods=['POST', 'GET'])
def search():
    exercises = mongo.db.exercises.find()
    return render_template('search.html', exercises=exercises)


""" REGISTER """
@app.route("/register", methods=['POST', 'GET'])
def register():
    # User registration - Check to see if the username already exists in the database.
    # If it isn't we then create a new user in the database with the provided username/password provided.
    # If the username is already in the database, we inform the user that the username has already been taken,
    # and to try another
    if request.method == 'POST':
        list_of_users = mongo.db.users
        check_existing_users = list_of_users.find_one(
            {"user_name": request.form['username']})
        if not check_existing_users:
            list_of_users.insert_one({"user_name": request.form['username'],
                                      "password": request.form['password']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        flash(
            "Sorry, username '{}' has been taken. Please choose another".format(request.form['username']))
        return redirect(url_for('register'))
    return render_template('register.html')


""" LOG IN """
@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
    # Initially confirm the user isn't already logged in
    if session.get('username'):
        flash("You are already logged in. To log in as a different user, try logging out first.")
        return redirect(url_for('index'))

    # User login - Check to see if the username/password already exists in the database.
    # If the correct username/password combo is entered, then they user is logged in and redirected to the home page.
    # If it isn't we alert them that they have entered the wrong username/password.
    # If they enter a username that isn't stored in the database, we ask them to check the username was spelt correctly.

    if request.method == 'POST':
        list_of_users = mongo.db.users
        current_user = list_of_users.find_one(
            {'user_name': request.form['username']})
        if current_user:
            if request.form['password'] == current_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            flash("Incorrect username and/or password. Please try again.")
            return render_template('log_in.html')
        flash("The username '{}' does not exist, please check username was spelt correctly.".format(request.form['username']))
    return render_template('log_in.html')


""" LOG OUT """
@app.route("/log_out")
def log_out():
    # Log out the user by clearing the session data
    session.pop('username', None)
    flash("Logged Out Successfully")
    return redirect(url_for('index'))


""" USER ACCOUNT PAGE"""
@app.route('/user_account/<account_name>', methods=['POST', 'GET'])
def user_account(account_name):
    # We need ensure the account being accessed using the current url matches the account stored in session.
    if account_name != session.get('username'):
        flash("Sorry, you may only access your own account page. Please sign in again...")
        session.pop('username', None)
        return redirect(url_for('log_in.html'))
    else:
        user = mongo.db.users.find_one({"user_name": account_name})

        exercises = mongo.db.exercises.find()

    return render_template('user_account.html', exercises=exercises, user=user)


""" ADD EXERCISE PAGE """
# This function will render the add_exercise.html page,
# and allow the form select boxes to access the relevant collection in the database
@app.route('/add_exercise', methods=['POST', 'GET'])
def add_exercise():
    # Select box options from database
    muscles = mongo.db.muscles.find()
    types_of_exercise = mongo.db.types_of_exercise.find()
    mechanics = mongo.db.mechanics.find()
    equipment = mongo.db.equipment.find()
    difficulty = mongo.db.difficulty.find()
    return render_template('add_exercise.html',
                           muscles=muscles,
                           types_of_exercise=types_of_exercise,
                           mechanics=mechanics,
                           equipment=equipment,
                           difficulty=difficulty)


""" INSERT EXERCISE """
# This function allows the information in the form to be submitted to the database therefore creating a new entry
# in the exercises collection and redirecting the user back to the index page after the form has been posted
@app.route('/insert_exercise', methods=['POST'])
def insert_exercise():
    exercises = mongo.db.exercises
    exercises.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


""" EXERCISE PAGE """
# This function will render the exercise.html page which will use the exercise id to display a specific exercise
# and its information, and allow the user that created said exercise to be able to access edit and delete functionality
@app.route('/exercise/<exercise_id>', methods=['POST', 'GET'])
def exercise(exercise_id):
    this_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    return render_template('exercise.html',
                           exercise=this_exercise)


""" EDIT EXERCISE PAGE """
# This function will render the edit_exercise.html page, and will pre-fill the form fields
# with the information previously submitted by the user, this allows them to view the exercise and its information
# and change any fields they may need to as they see fit
@app.route("/edit_exercise/<exercise_id>", methods=['POST', 'GET'])
def edit_exercise(exercise_id):
    this_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})

    muscles = mongo.db.muscles.find()
    types_of_exercise = mongo.db.types_of_exercise.find()
    mechanics = mongo.db.mechanics.find()
    equipment = mongo.db.equipment.find()
    difficulty = mongo.db.difficulty.find()
    return render_template('edit_exercise.html',
                           exercise=this_exercise,
                           muscles=muscles,
                           types_of_exercise=types_of_exercise,
                           mechanics=mechanics,
                           equipment=equipment,
                           difficulty=difficulty)


""" UPDATE EXERCISE """
# This function allows the information in the form to be submitted to the database therefore editing the exercise
# being accessed from exercises collection and redirecting the user back to the index page after the form has been posted
@app.route("/update_exercise/<exercise_id>", methods=['POST'])
def update_exercise(exercise_id):
    updated_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    updated_fields = request.form.to_dict()
    mongo.db.exercises.update_one(updated_exercise, {"$set": updated_fields})

    return redirect(url_for('index'))


""" DELETE EXERCISE PAGE """
# This function will render the delete_exercise.html page
@app.route("/delete_exercise/<exercise_id>", methods=['POST', 'GET'])
def delete_exercise(exercise_id):
    deleted_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})

    return render_template('delete_exercise.html', exercise=deleted_exercise)


""" REMOVE EXERCISE """
# This function allows the exercise to be removed from the database
# should the user that created the exercise decide it is necessary to do so
@app.route("/remove_exercise/<exercise_id>", methods=['POST', 'GET'])
def remove_exercise(exercise_id):
    mongo.db.exercises.remove({"_id": ObjectId(exercise_id)})
    return redirect(url_for('index'))


app.run(host=os.environ.get('IP', '127.0.0.1'),
        port=int(os.environ.get('PORT', '8080')),
        debug=True)