from flask import Flask
import requests
import json
import config

app = Flask(__name__)

# Inputs
city_name = config.city
API_key = config.API_key

print(city_name, API_key)