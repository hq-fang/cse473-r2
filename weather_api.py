# weather_api.py

import requests
import os

# In practice, store your API key securely, e.g. in environment variables
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "5fad286d5766eeddce16801bb35e64d1")

def get_current_weather(city: str) -> dict:
    """
    Fetches current weather data for a given city from OpenWeatherMap (or another API).
    Returns a dictionary matching the action's output_schema in the tool definition.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        # Handle error or fallback
        return {
            "description": "Unable to fetch weather data.",
            "temperature": 0.0,
            "humidity": 0
        }
    
    data = response.json()
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    
    return {
        "description": weather_description,
        "temperature": temperature,
        "humidity": humidity
    }
