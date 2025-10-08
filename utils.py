# utils.py

import requests

def fetch_data(url, timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
