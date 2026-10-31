import requests

class NasaApodConnector:
    def __init__(self, api_key="DEMO_KEY", base_url="https://api.nasa.gov/planetary/apod"):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = 10

    def get_picture_of_the_day(self, date=None):
        params = {"api_key": self.api_key}
        if date:
            params["date"] = date
        try:
            response = requests.get(self.base_url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.ConnectionError:
            return {"error": "Connection error occurred"}
        except requests.exceptions.Timeout:
            return {"error": "Request timed out"}
        except Exception as err:
            return {"error": f"An unexpected error occurred: {err}"}
