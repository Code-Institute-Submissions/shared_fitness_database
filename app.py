import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import math

app = Flask(__name__)

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



app.run(host=os.environ.get('IP', '127.0.0.1'),
        port=int(os.environ.get('PORT', '8080')),
        debug=True)