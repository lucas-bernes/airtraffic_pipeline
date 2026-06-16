import requests


def extract_flights():

    url = "https://opensky-network.org/api/states/all"

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise Exception(
            f"API Error: {response.status_code}"
        )

    return response.json()
