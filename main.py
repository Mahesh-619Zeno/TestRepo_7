# main_v1.py

from config import API_BASE_URL, DEFAULT_HEADERS
from utils import make_api_call
import datetime

# Print current timestamp
now = datetime.datetime.now()
print("Script started at:", now)

endpoint = "/status"
url = API_BASE_URL + endpoint

status_code, response = make_api_call(url, headers=DEFAULT_HEADERS)

# Save timestamp of API call
log_time = datetime.datetime.now()

print(f"[{log_time}] Status Code: {status_code}")
print("Response:", response)
