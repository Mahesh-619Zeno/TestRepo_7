import requests

def make_api_call(url, headers=None):
    print(f"Making API call to: {url}")  

    try:
        response = requests.get(url, headers=headers)
        return response.status_code, response.json()
    except Exception as e:
        print(f"API call failed: {e}")  
        return 500, {"error": str(e)}
