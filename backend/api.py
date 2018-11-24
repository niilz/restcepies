#!/usr/bin/env python
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import urllib.request
import re
import json

app = Flask(__name__)
# enables cross-origin requests
CORS(app)


base_url = "https://www.chefkoch.de/rs/s0/"
id_name_pattern = re.compile(r'rezepte\/(\d+)\/(.+).html')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Content-Type': 'text/html'
}
#headers = {}
data = None

@app.route('/')
def collect_recipes():
    ingredients = request.args
    url = base_url
    for i in range(len(ingredients)):
        url += f'+{ingredients[str(i)]}'
    url += '/rezepte.html'
    print("URL", url)
    req = urllib.request.Request(url, data, headers)
    page = urllib.request.urlopen(req).read()
    print(page)
    return "Hello World"
    # recipes = {}
    # for ID, name in id_name_pattern.findall(page):
    #     if ID not in recipes:
    #         recipes[ID] = name
    # return jsonify(recipes)





