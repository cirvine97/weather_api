from flask import Flask
import requests
import json
import config

app = Flask(__name__)

# Inputs
city_name = config.city
API_key = config.API_key

def get_lat_lon(
        city_name:str, 
        API_key:str
        ) -> list:
    '''Get the latlong of a city name'''
    gecoder_address = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}'
    geocoder_response = requests.get(geocoder_API)
    data = geocoder_response.text
    data = json.loads(data)
    lat = data[0]['lat']
    lon = data[0]['lon']
    return [lat, lon]

lat_lon = get_lat_lon(city_name=city_name,
                      API_key=API_key)

if __name__== "__main__":
    app.run(debug=True)