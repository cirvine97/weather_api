from flask import Flask, redirect, url_for, request, render_template
import requests
import json
import config


def get_lat_lon(
        city_name:str, 
        API_key:str
) -> list:
    '''Get the latlong of a city name'''
    geocoder_address = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}'
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
    lat_lon = get_lat_lon(city_name=city_name,
                           API_key=API_key
                           )

    # Get the weather info
    weather_address = f'https://api.openweathermap.org/data/2.5/weather?lat={lat_lon[0]}&lon={lat_lon[1]}&appid={API_key}'
    weather_response = requests.get(weather_address)
    data = weather_response.text
    data = json.loads(data)

    return data


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def input_city():
    if request.method == "POST":
        city = request.form["nm"]
        return redirect(url_for("weather_report", city_name=city))
    else:
        return render_template("input.html")

@app.route("/weather/<city_name>")
def weather_report(city_name):
    weather = get_weather(city_name=city_name, API_key=config.API_key)
    return weather

if __name__ == "__main__":
    app.run(debug=True)