from extract import extract_flights
from transform import transform_data
from load import load_flights
import pprint


def main():

    # 1. EXTRACT
    raw_data = extract_flights()

    # 2. TRANSFORM
    data = transform_data(raw_data)

    pprint.pprint(data[:5])

    # 3. LOAD
    load_flights(data)


if __name__ == "__main__":
    main()
