import datetime
import requests
import pandas as pd
from config import API_ENDPOINT, DEFAULT_PARAMS

def fetch_data():
    start_time = datetime.datetime.now()
    print(f"[{start_time}] Fetching data from {API_ENDPOINT}...")

    try:
        response = requests.get(API_ENDPOINT + "/users", params=DEFAULT_PARAMS)
        response.raise_for_status()

        users = response.json()
        df = pd.DataFrame(users)
        print("Fetched users (DataFrame):")
        print(df[['login', 'id']])

    except requests.exceptions.RequestException as e:
        print("API Error:", e)

    end_time = datetime.datetime.now()
    print(f"Completed at {end_time}, Duration: {end_time - start_time}")

fetch_data()
