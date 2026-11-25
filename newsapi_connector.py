
import requests

class NewsApiConnector:
    def __init__(self, api_key="DEMO_KEY", base_url="https://newsapi.org/v2"):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = 10

    def get_everything(self, query, language="en", sort_by="publishedAt", page_size=5):
        params = {
            "q": query,
            "language": language,
            "sortBy": sort_by,
            "pageSize": page_size,
            "apiKey": self.api_key,
        }
        try:
            response = requests.get(f"{self.base_url}/everything", params=params, timeout=self.timeout)
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

    def get_top_headlines(self, query=None, country="us", page_size=5):
        params = {
            "country": country,
            "pageSize": page_size,
            "apiKey": self.api_key,
        }
        if query:
            params["q"] = query
        try:
            response = requests.get(f"{self.base_url}/top-headlines", params=params, timeout=self.timeout)
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
