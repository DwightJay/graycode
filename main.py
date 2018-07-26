import requests
from bs4 import BeautifulSoup
import os
from flask import Flask


def true_facts():
	response = requests.get("http://unkno.com")

	soup = BeautifulSoup(response.content, "html.parser")
	facts = soup.find_all("div", id="content")

	return facts[0].getText()

#true_facts()


app = Flask(__name__)

@app.route('/facts/')
def get_facts():
	return true_facts()

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 6738))
	app.run(host='0.0.0.0', port=port)
