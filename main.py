import datetime
import requests
from config import API_ENDPOINT, DEFAULT_PARAMS

def fetch_data():
    print(f"[{datetime.datetime.now()}] Fetching data from {API_ENDPOINT}...")
    response = requests.get(API_ENDPOINT + "/users", params=DEFAULT_PARAMS)
    if response.status_code == 200:
        print("Fetched users:")
        for user in response.json():
            print("-", user['login'])
    else:
        print("Error fetching data:", response.status_code)

fetch_data()
