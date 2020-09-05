from flask import Flask, render_template, request
from dotenv import load_dotenv
import urllib.request, urllib.parse, urllib.error
import http.client
import requests
import json
import os

app = Flask(__name__)

URI = os.getenv('ATLAS_URI')

@app.route('/track')
def index():
    user_id = request.args.get('user_id')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
