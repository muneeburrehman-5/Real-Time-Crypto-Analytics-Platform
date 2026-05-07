import requests
import json

URL = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1,
    "sparkline": "false"
}

def extract():
    response = requests.get(URL, params=params)

    if response.status_code != 200:
        raise Exception("API Error")

    data = response.json()

    with open("data/raw.json", "w") as f:
        json.dump(data, f)

    return data