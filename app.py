from flask import Flask, render_template, request
from dotenv import load_dotenv
import urllib.request, urllib.parse, urllib.error
import http.client
import requests
import pymongo
import dns
import json
import os

app = Flask(__name__)

URI = os.getenv('ATLAS_URI')
location_id = ''



def scan():
    location_id = request.args.get('location_id')
    return render_template('index.html')

@app.route('/scan_success')
def scan_success():
    user_id = request.args.get('user_id')

    def add_location(user_id, location_id):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['QRowd']
        my_col = my_db['users']
        user = my_col.find({'user_id': str(user_id)})
        if user == None:
            response = user_id + ' was not found'
        else:
            my_col.update({'user_id': user_id}, {'$push': {'locations': location_id}})
            response = user_id + ' has been successfully updated'
        return response

    response = add_location(user_id, location_id)
    print(location_id)
    return render_template('scan_success.html', response=response)

if __name__ == '__main__':
    app.run()
