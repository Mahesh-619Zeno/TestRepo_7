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

        DEFAULT_PARAMS['since'] = 1000
        next_response = requests.get(API_ENDPOINT + "/users", params=DEFAULT_PARAMS)
        print(f"Calling API at: {API_ENDPOINT}/users with params: {DEFAULT_PARAMS}")

        users = response.json()
        print(f"Fetched {len(users)} users from GitHub.")        

        users = response.json()
        df = pd.DataFrame(users)

        filtered_df = df[df['id'] > 10000].copy()
        filtered_df['fetched_at'] = datetime.datetime.now()

        print("Fetched users (DataFrame):")
        print(df[['login', 'id']])

    except requests.exceptions.RequestException as e:
        print("API Error:", e)

    end_time = datetime.datetime.now()
    print(f"Completed at {end_time}, Duration: {end_time - start_time}")

fetch_data()
