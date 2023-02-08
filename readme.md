This repo contains code for an API that pulls weather data after being polled for specific cities to give bespoke weather information. It is structured as:
readme.md (this file)
requirements.txt (all dependencies for API to run)
config.py (configuration file for API key and temperature units)
app.py (Main file. API code)
templates/ (Contains html templates for API)
testing/ (Contains pytest testing scripts for functions in API).

This API makes use of the Open Weather API. You will need a key to use this API. Generate one here ttps://home.openweathermap.org/users/sign_up.

Set-up instructions:
1) Paste API key and selected desired temperature unit in config.py
2) From the weather_api/ root directory, run `pip install -r requirements.txt` to install all dependencies. You may wish to use a virtual environment. 
3) From the weather_api. root directory, run `flask --app app run` to launch the API. Then navigate to `0.0.0.0:5000` within a browser to interact with it. 