import requests
API_KEY = "your_api_key_here"

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        weather_data = response.json()

        if response.status_code == 200:
            print(f"\nWeather in {weather_data['name']}, {weather_data['sys']['country']}:")
            print(f"🌡️ Temperature: {weather_data['main']['temp']}°C")
            print(f"🌥️ Weather: {weather_data['weather'][0]['description'].capitalize()}")
            print(f"💧 Humidity: {weather_data['main']['humidity']}%")
            print(f"🌬️ Wind Speed: {weather_data['wind']['speed']} m/s")
        else:
            print("❌ City not found or API error:", weather_data.get("message", "Unknown error"))

    except requests.exceptions.RequestException as e:
        print("❌ Network error:", e)

if __name__ == "__main__":
    print("=== Weather Checker ===")
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ").strip()

    get_weather(city, api_key)