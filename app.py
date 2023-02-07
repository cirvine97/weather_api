from flask import Flask, redirect, url_for, request, render_template
import requests
import json
import config
import logging


def get_lat_lon(
        city_name:str, 
        API_key:str
) -> list:
    '''Get the latlong of a city name'''
    geocoder_address = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}'
    geocoder_response = requests.get(geocoder_address)
    data = geocoder_response.text
    data = json.loads(data)
    # Catch the case that an invalid city name has been provided
    if len(data) == 0:
        raise ValueError("Invalid city name")
    lat = data[0]['lat']
    lon = data[0]['lon']
    return [lat, lon]

def get_weather(
    city_name:str,
    API_key:str
) -> dict:
    '''Returns the JSON output of a city's weather.'''
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

def surfaced_values(
    city_name:str,
    API_key:str,
    temperature_units:str
) -> dict:
    '''Format the JSON output to be surfaced on the API'''
    weather_json = get_weather(city_name, API_key)
    description = weather_json['weather'][0]['description']
    icon = weather_json['weather'][0]['icon']
    kelvin_temp = weather_json['main']['temp']

    if temperature_units == 'Celsius':
        temperature = kelvin_temp - 273.15
    elif temperature_units == 'Farenheit':
        temperature = (kelvin_temp - 273.15)*(9/5) + 32
    else:
        raise ValueError('Temperature units must be Celsius or Farenheit')
    
    results = {
        "Description": description,
        "Icon": icon,
        "Temperature": temperature
    }
    # Convert to json
    results_json = json.dumps(results)

    return results_json


app = Flask(__name__)

# Start logging
logging.basicConfig(filename='record.log',
                    level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route("/", methods=["POST", "GET"])
def input_city():
    app.logger.error('Error log information')
    if request.method == "POST":
        city = request.form["nm"]
        return redirect(url_for("weather_report", city_name=city))
    else:
        app.logger.info("Info log information")
        return render_template("input.html")

@app.route("/weather/<city_name>")
def weather_report(city_name):
    app.logger.error("Error log information")
    values = surfaced_values(city_name,
                             config.API_key,
                             config.temperature_unit)
    return values

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)