from flask import Flask, render_template, request
from dotenv import load_dotenv
import urllib.request, urllib.parse, urllib.error
import http.client
import geocoder
import json
import os


MAPS_TOKEN = os.getenv('MAPS_TOKEN')
