import requests
# from flask import Blueprint, render_template, flash, redirect, url_for
# from flask import current_app as current_app
import os

# intro = Blueprint('home',__name__, url_prefix = '/')
# @intro.route('/home', methods = ['GET'])
def gc():
    API_KEY = 'AIzaSyCNvGv9pR4IqFUg1xCQOMgECDDwC_bK-8w'

    address = '구래역'

    params = {
        'key': API_KEY,
        'address': address
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

    response = requests.get(base_url, params=params).json()
    response.keys()

    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']
    return lat, lon
