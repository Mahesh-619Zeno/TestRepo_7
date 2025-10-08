from config import API_BASE_URL, DEFAULT_HEADERS
from utils import make_api_call
import datetime

print("Running at:", datetime.datetime.now())

endpoint = "/status"
url = API_BASE_URL + endpoint

status_code, response = make_api_call(url, headers=DEFAULT_HEADERS)

print("Status Code:", status_code)
print("Response:", response)
