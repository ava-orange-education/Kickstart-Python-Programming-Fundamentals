from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'your_api_key' with your actual API key from OpenWeatherMap
API_KEY = 'your_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            try:
                response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
                if response.status_code == 200:
                    weather_data = response.json()
                else:
                    error = 'City not found. Please try another city.'
            except requests.exceptions.RequestException:
                error = 'Failed to connect to the weather service. Please try again later.'
    return render_template('weather.html', weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
