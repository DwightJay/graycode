
import requests
from bs4 import BeautifulSoup
import os
from flask import Flask
import geomag
from weather import Weather, Unit
import pyowm
# ip address location finder
import urllib.request
import json

app = Flask(__name__)

# location finder WORKS!!!!
with urllib.request.urlopen("https://geoip-db.com/json") as url:
    data = json.loads(url.read().decode())
    print(data)

country = data['country_code']
city = data['city']
latitude = data['latitude']
longitude =data['longitude']
#print(city)
cc = city + ',' + country
#global latitude, longitude

@app.route('/')
def get_declination():
    owm = pyowm.OWM('6a4296ddd0988dee8222522a8656542c')  # You MUST provide a valid API key
    # Have a pro subscription? Then use:
    # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

    # Search for current weather in ANYWHERE!
    #observation = owm.weather_at_place('Seattle, US'))
    observation = owm.weather_at_place(cc)
    w = observation.get_weather()
    print(w)

    # Weather details
    print(w.get_wind())                  # {'speed': 4.6, 'deg': 330}
    print(w.get_humidity())              # 87
    print(w.get_temperature('fahrenheit'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

    # Search current weather observations in the surroundings of
    # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
    observation_list = owm.weather_around_coords(latitude, longitude)
    print(type(observation_list))
   
    #print(observation_list)
    #w = observation_list.get_weather()
    weather = Weather(Unit.CELSIUS) 
    lookup = weather.lookup_by_latlng(latitude, longitude)
    condition = lookup.condition
    print(condition.text)
     # magnetic declination, temp in celcius
    print(str(geomag.declination(latitude, longitude)))
    
    return str(condition.text)
    #str(condition.text)
    #str(geomag.declination(int(latitude), int(longitude)))

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 6738))
	app.run(host='0.0.0.0', port=port)
