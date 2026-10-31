import requests
import logging

logger = logging.getLogger(__name__)

class CoinGeckoConnector:
    def __init__(self, api_key: str = None):
        self.base_url = "https://api.coingecko.com/api/v3"
        self.headers = {}
        if api_key:
            self.headers["x-cg-pro-api-key"] = api_key

    def _make_request(self, endpoint: str, params: dict = None):
        """Helper method with built-in error handling for all API requests."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err} - Response: {response.text}")
            return {"error": str(http_err), "status_code": response.status_code}
        except requests.exceptions.ConnectionError as conn_err:
            logger.error(f"Connection error occurred: {conn_err}")
            return {"error": "Connection error occurred"}
        except requests.exceptions.Timeout as timeout_err:
            logger.error(f"Timeout error occurred: {timeout_err}")
            return {"error": "Request timed out"}
        except Exception as err:
            logger.error(f"An unexpected error occurred: {err}")
            return {"error": str(err)}

    def get_coin_price(self, coin_id: str, vs_currency: str = "usd"):
        """Fetches the current price of a specific coin with error handling."""
        params = {
            "ids": coin_id,
            "vs_currencies": vs_currency
        }
        return self._make_request("simple/price", params=params)

    def get_trending_coins(self):
        """Fetches trending search coins on CoinGecko with error handling."""
        return self._make_request("search/trending")

    def load_data(self, coin_ids: list[str], vs_currency: str = "usd"):
        """Data loading function to fetch and structure coin data for ingestion."""
        loaded_records = []
        for coin_id in coin_ids:
            result = self.get_coin_price(coin_id, vs_currency)
            if "error" not in result:
                loaded_records.append({
                    "coin_id": coin_id,
                    "currency": vs_currency,
                    "payload": result
                })
        return loaded_records
