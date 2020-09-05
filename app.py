from flask import Flask, render_template, request
from dotenv import load_dotenv
import urllib.request, urllib.parse, urllib.error
import http.client
import requests
import json
import os
import aes


app = Flask(__name__)
app.secret_key = os.getenv('FLASK_KEY')


URI = os.getenv('ATLAS_URI')
cipher = aes.AESCipher(os.getenv('CIPHER_KEY'))


URL = "https://geocode.search.hereapi.com/v1/geocode"
location = input("Enter the location here: ")
api_key = 'A5KBDur5Hp4Nok2YSD5pqg5I4rvZ1fDTMauWFD0feKM'
PARAMS = {'apikey':api_key,'q':location}

r = requests.get(url = URL, params = PARAMS)
data = r.json()

latitude = data['items'][0]['position']['lat']
longitude = data['items'][0]['position']['lng']


@app.route('/')
def login():
    return render_template('map.html',apikey=api_key,latitude=latitude,longitude=longitude)


'''@app.route('/login')
def login():
    return render_template('login.html', logged_in=session.get('logged_in'))


@app.route('/login_success')
def login_success():
    email = request.args.get('email')
    password = request.args.get('password')

    inputs = {
        'email': email,
        'password': password
    }

    def get_from_db(email, password):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['VHomes']
        my_col = my_db['users']
        user = my_col.find_one({'email': str(email)})
        dec_pass = cipher.decrypt(str(user['password']))
        if str(user['email']) == email and dec_pass == password:
            return True
        else:
            return False

    if get_from_db(email, password) == False:
        response = 'incorrect username or password'
        session['logged_in'] = False
        return render_template('login_unsuccessful.html', response=response)
    else:
        response = 'logged in as ' + email
        session['logged_in'] = True
        return render_template('login_success.html', response=response)


@app.route('/signup')
def signup():
    return render_template('signup.html', logged_in=session.get('logged_in'));


@app.route('/signup_success')
def signup_success():
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('password')

    enc_pass = cipher.encrypt(password)

    inputs = {
        'name': name,
        'email': email,
        'password': enc_pass
    }

    def check_db(email):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['VHomes']
        my_col = my_db['users']
        user = my_col.find_one({'email': str(email)})
        return user

    def add_to_db(inputs):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['VHomes']
        my_col = my_db['users']
        my_col.insert_one(inputs)

    if check_db(email) == None:
        add_to_db(inputs)
        response = 'sign up successful!'
        session['logged_in'] = True
        return render_template('signup_success.html', response=response)
    else:
        response = 'email already registered'
        session['logged_in'] = False
        return render_template('signup_unsuccessful.html', response=response)
'''
if __name__ == '__main__':
    app.run()
