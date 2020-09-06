from flask import Flask, render_template, request
from dotenv import load_dotenv
import urllib.request, urllib.parse, urllib.error
import http.client
import requests
import pymongo
import json
import random
import os

app = Flask(__name__)

URI = os.getenv('ATLAS_URI')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/scan/')
def scan():
    location_id = request.args.get('location_id')
    return render_template('scan.html', location_id=location_id)

@app.route('/scan_success')
def scan_success():
    user_id = request.args.get('user_id')
    location_id = request.args.get('location_id')

    def add_location(user_id, location_id):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['QRowd']
        my_col = my_db['users']
        user = my_col.find_one({'user_id': int(user_id)})
        if user == None:
            response = user_id + ' was not found'
        else:
            my_col.update_one({'user_id': int(user_id)}, {'$push': {'locations': int(location_id)}})
            response = user_id + ' has been successfully updated'
        return response

    response = add_location(user_id, location_id)
    return render_template('scan_success.html', response=response)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_success')
def signup_success():
    response = random.randint(0000, 9999)

    def in_db(user_id):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['QRowd']
        my_col = my_db['users']
        user = my_col.find_one({'user_id': int(user_id)})
        if user == None:
            return False
        else:
            return True

    def add_to_db(user_id):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['QRowd']
        my_col = my_db['users']
        user = my_col.insert_one({'user_id': int(user_id), 'locations': []})

    while True:
        if in_db(response) == False:
            add_to_db(response)
            break
        response = random.randint(0000, 9999)

    return render_template('signup_success.html', response=response)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/map')
def map():
    user_id = request.args.get('user_id')

    def location_list(user_id):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['QRowd']
        my_col = my_db['users']
        user = my_col.find_one({'user_id': int(user_id)})
        return user

    def get_location(location_id):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['QRowd']
        my_col = my_db['locations']
        location = my_col.find_one({'location_id': int(location_id)})
        return location

    locations = list(location_list(user_id)['locations'])
    lon = []
    lat = []

    for location in locations:
        lon.append(get_location(int(location))['longitude'])
        lat.append(get_location(int(location))['latitude'])

    return render_template('map.html', lon=lon, lat=lat)

if __name__ == '__main__':
    app.run()
