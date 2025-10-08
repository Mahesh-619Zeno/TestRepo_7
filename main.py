# main_v1.py

from config import API_BASE_URL, DEFAULT_HEADERS
from utils import make_api_call
import datetime
import time

# Print current timestamp
now = datetime.datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Script started at:", now)
print("Request started at:", formatted_now)
if now.hour < 12:
    greeting = "Good morning"
elif now.hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"
print(greeting + "! Sending API request...")

AUTH_HEADERS = DEFAULT_HEADERS.copy()

print("Script started at:", now)

endpoint = "/status"
url = API_BASE_URL + endpoint

start_time = time.time()

status_code, response = make_api_call(url, headers=DEFAULT_HEADERS)

end_time = time.time()
duration = round(end_time - start_time, 3)

# Save timestamp of API call
log_time = datetime.datetime.now().strftime("%H:%M:%S")
print(f"[{log_time}] Status Code: {status_code}")

print(f"[{log_time}] Status Code: {status_code}")
print("Response:", response)
print(f"API call completed in {duration} seconds.")