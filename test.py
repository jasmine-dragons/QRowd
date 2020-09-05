from flask import Flask, render_template, request
from dotenv import load_dotenv
import urllib.request, urllib.parse, urllib.error
import http.client
import geocoder
import json
from json import loads
import os

load_dotenv()
MAPS_TOKEN = os.getenv('MAPS_TOKEN')
DATASET_ID = os.getenv('DATASET_ID')
MAPS_USER = os.getenv('MAPS_USER')


conn = http.client.HTTPSConnection('api.mapbox.com')

conn.request('GET', '/datasets/v1/' + MAPS_USER + '/' + DATASET_ID + '/features?access_token=' + MAPS_TOKEN)

# Decode UTF8 responses
res = conn.getresponse()
data = res.read().decode("utf-8")
# Create JSON object from data
try:
    js = json.loads(data)
except:
    js = None
# Check JSON object for errors (ie. invalid WORD)
if not js:
    print('error')
# 'https://api.mapbox.com/datasets/v1/nishantbalaji/ckeq2oto816oe28k48h74h0h8?access_token=' + MAPS_TOKEN


feature_id = 1;
type = 'Point'
body = {
  "id": "1",
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [
        100, 0
    ]
  },
  "properties": {
    "prop0": "value0"
  }
}

bodyjs = json.dumps(body)

conn.request('PUT', '/datasets/v1/' + MAPS_USER + '/' + DATASET_ID + '/features/' + str(feature_id) + '?access_token=' + MAPS_TOKEN,body=bodyjs)
response = conn.getresponse()
print(response.status, response.reason)


conn = http.client.HTTPSConnection('api.mapbox.com')
conn.request('GET', '/datasets/v1/' + MAPS_USER + '/' + DATASET_ID + '/features?access_token=' + MAPS_TOKEN)
# Decode UTF8 responses
res = conn.getresponse()
data = res.read().decode("utf-8")
# Create JSON object from data
js = json.loads(data)
print(js)
