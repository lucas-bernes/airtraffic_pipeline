import os
import requests


def extract_flights():

    url = "https://opensky-network.org/api/states/all"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(
            f"API Error: {response.status_code}"
        )

    return response.json()
