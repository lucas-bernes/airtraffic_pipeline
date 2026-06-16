from extract import extract_flights
from datetime import datetime
import pprint


def transform_data(raw_data):

    timestamp = raw_data['time']

    flights = []

    for state in raw_data['states']:

        flight = {
            "datetime": datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S"),
            "icao24": state[0],
            "callsign": state[1],
            "origin_country": state[2],
            "longitude": state[5],
            "latitude": state[6],
            "altitude": state[7],
            "on_ground": state[8],
            "velocity": state[9]
        }

        flights.append(flight)

    return flights
