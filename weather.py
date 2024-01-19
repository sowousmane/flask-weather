import datetime
import json
import os
from flask import Flask, render_template, request, abort, Response
import urllib.request
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
#initialize the Flask application
app = Flask(__name__)

def get_weather(city_name=None):   
    data = {}
    # get city from url
    if city_name:
        data['q'] = request.args.get('city')
    # get city from form
    else:
        data['q'] = request.form['city'] 

    data['appid'] = os.getenv("OPEN_WEATHER_TOKEN")
    data['units'] = 'metric'

    url_values = urllib.parse.urlencode(data)
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    full_url = url + '?' + url_values
    data = urllib.request.urlopen(full_url)
    #print(data)
    data=json.loads(data.read().decode('utf8'))
    #print(data)
    return data

@app.route("/search-city", methods=["POST"])
def validate_search():
    if request.method == "POST":
        print(request.form['city'])
    data=get_weather()
    return render_template('index.html', title='Weather App', data=data)

@app.route('/',methods=['GET', 'POST'])
def home():
    result = None
    current_year = datetime.datetime.now().year

    if request.method == 'POST':
        # Handle form submission
        result = validate_search()  # Replace with your actual function
    
    return render_template('home.html', title="home", current_year=current_year ,result=result)

# Get weather using params in url
@app.route('/forecast', methods=['GET'])
def get_wea():    
    data=get_weather(request.args.get('city'))
    return render_template('index.html', title='App', data=data)