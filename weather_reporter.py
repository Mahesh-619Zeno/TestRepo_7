import sys
import requests
from datetime import datetime

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(city_name, api_key):
    params = {
        'q': city_name,
        'appid': api_key
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return None

def print_weather_info(data):
    if not data:
        print("No data to display.")
        return

    try:
        city = data['name']
        country = data['sys']['country']
        temp = kelvin_to_celsius(data['main']['temp'])
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        timestamp = data['dt']
        time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

        print("\n--- Weather Report ---")
        print(f"Location   : {city}, {country}")
        print(f"Time       : {time}")
        print(f"Temperature: {temp:.2f}°C")
        print(f"Weather    : {weather.capitalize()}")
        print(f"Humidity   : {humidity}%")
        print(f"Wind Speed : {wind_speed} m/s")
        print("----------------------\n")
    except KeyError as e:
        print(f"Unexpected data format. Missing key: {e}")

def run_cli():
    print("Welcome to the Weather Reporter CLI")
    print("Type 'exit' to quit.\n")

    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    if not api_key:
        print("API key is required.")
        sys.exit(1)

    while True:
        city = input("Enter city name: ").strip()
        if city.lower() == 'exit':
            print("Goodbye!")
            break

        if not city:
            print("Please enter a valid city name.")
            continue

        print("Fetching weather data...")
        data = get_weather(city, api_key)
        print_weather_info(data)

if __name__ == "__main__":
    run_cli()
