import requests

def query(image_data, api_url, headers):
    try:
        response = requests.post(api_url, headers=headers, data=image_data)
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
