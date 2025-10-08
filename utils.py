import requests

def make_api_call(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        return response.status_code, response.json()
    except Exception as e:
        return 500, {"error": str(e)}
