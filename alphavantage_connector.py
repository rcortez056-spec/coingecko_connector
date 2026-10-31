import requests

class AlphaVantageConnector:
    def __init__(self, api_key, base_url="https://www.alphavantage.co/query"):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = 10

    def _get(self, params):
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

    def get_daily_stock_data(self, symbol):
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key
        }
        return self._get(params)
