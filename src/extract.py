from dotenv import load_dotenv
import os
import requests
import pprint

load_dotenv()

api_key = os.getenv('API_KEY')

url = "https://opensky-network.org/api/states/all"

response = requests.get(url)
data = response.json()
