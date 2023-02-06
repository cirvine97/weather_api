from flask import Flask, redirect, url_for, request, render_template
import requests
import json
import config

# Inputs
city_name = config.city
API_key = config.API_key

def get_lat_lon(
        city_name:str, 
        API_key:str
) -> list:
    '''Get the latlong of a city name'''
    gecoder_address = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}'
    geocoder_response = requests.get(geocoder_address)
    data = geocoder_response.text
    data = json.loads(data)
    lat = data[0]['lat']
    lon = data[0]['lon']
    return [lat, lon]

def get_weather(
    city_name:str,
    API_key:str
) -> dict:
    
    # Get the lat lon of the city 
    lat_lon = get_lat_long(city_name=city_name,
                           API_key=API_key
                           )

    # Get the weather info
    weather_address = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_lon[0]}&lon={lat_lon[1]}&appid={API_key}'
    weather_response = requests.get(weather_address)
    data = weather_response.text
    data = json.loads(data)

    return data


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)