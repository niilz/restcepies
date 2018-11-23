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

@app.route('/')
def collect_recipes():
    ingredients = request.args
    url = base_url
    for i in range(len(ingredients)):
        url += f'+{ingredients[str(i)]}'
    url += '/rezepte.html'
    print("URL", url)
    page = urllib.request.urlopen(url).read().decode('utf-8')
    recipes = {}
    for ID, name in id_name_pattern.findall(page):
        if ID not in recipes:
            recipes[ID] = name
    return jsonify(recipes)





