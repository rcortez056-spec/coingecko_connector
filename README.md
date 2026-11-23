# API Connector Library

A collection of Python API connector classes for pulling live data into AI agents and automation pipelines.

## Connectors

| File | API | What It Fetches |
|------|-----|-----------------|
| `coingecko_connector.py` | CoinGecko | Crypto prices, market data, coin info |
| `alphavantage_connector.py` | Alpha Vantage | Stock prices, financial market data |
| `newsapi_connector.py` | NewsAPI | Live news articles by keyword or topic |
| `nasa_apod_connector.py` | NASA APOD | Astronomy Picture of the Day data |
| `openweathermap_connector.py` | OpenWeatherMap | Current weather and forecasts |

## Usage

Each connector is a standalone Python class. Import the one you need and initialize it with your API key.

```python
from newsapi_connector import NewsAPIConnector

connector = NewsAPIConnector(api_key="your_key_here")
results = connector.get_top_headlines(query="AI agents")
```

## Use Cases

- Feed live news into AI research agents
- Supply real-time market data to trading or prediction systems
- Power automation pipelines that need external data sources

## Built By

Ramon Cortez — AI Architect | [Linkedin.com](https://linkedin.com/in/ramon-cortez-a227a2112)
