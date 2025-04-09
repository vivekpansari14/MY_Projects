from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")  # OpenWeatherMap

@app.route('/')
def home():
    return app.send_static_file("index.html")

@app.route('/weather')
def get_weather():
    location = request.args.get("location")
    if not location:
        return jsonify({"status": "fail", "message": "Location is required"}), 400

    geo_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={GOOGLE_API_KEY}"
    geo_res = requests.get(geo_url).json()
    if not geo_res['results']:
        return jsonify({"status": "fail", "message": "Invalid location"}), 404

    lat = geo_res['results'][0]['geometry']['location']['lat']
    lon = geo_res['results'][0]['geometry']['location']['lng']

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={WEATHER_API_KEY}"
    weather_res = requests.get(weather_url).json()

    return jsonify({"status": "success", "lat": lat, "lon": lon, "weather": weather_res})

if __name__ == '__main__':
    app.run(debug=True)