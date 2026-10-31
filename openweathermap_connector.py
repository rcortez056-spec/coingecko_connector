import requests

class OpenWeatherMapConnector:
    def __init__(self, api_key, base_url="https://api.openweathermap.org/data/2.5"):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = 10

    def _get(self, endpoint, params):
        url = f"{self.base_url}/{endpoint}"
        params["appid"] = self.api_key
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
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

    def get_current_weather(self, city):
        endpoint = "weather"
        params = {"q": city}
        return self._get(endpoint, params)
