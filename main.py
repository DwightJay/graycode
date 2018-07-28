import requests
from bs4 import BeautifulSoup
import os
from flask import Flask
import geomag

app = Flask(__name__)

@app.route('/<latitude>/<longitude>')
def get_declination(latitude,longitude):
	return str(geomag.declination(int(latitude), int(longitude)))

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 6738))
	app.run(host='0.0.0.0', port=port)
