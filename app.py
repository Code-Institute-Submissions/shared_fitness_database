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

""" INDEX PAGE """
@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def index():
    exercises = mongo.db.exercises.find()
    return render_template('index.html', exercises=exercises)


@app.route('/search', methods=['POST', 'GET'])
def search():
    exercises = mongo.db.exercises.find()
    return render_template('search.html', exercises=exercises)


@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')


@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
    """ Confirm not already logged in """
    if session.get('username'):
        flash("Already logged in. To log in as a different user, try logging out first.")
        return redirect(url_for('index'))

    """ User login - check username and password, and then route accordingly """
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
        flash("Username '{}' does not exist.".format(request.form['username']))
    return render_template('log_in.html')


app.run(host=os.environ.get('IP', '127.0.0.1'),
        port=int(os.environ.get('PORT', '8080')),
        debug=True)