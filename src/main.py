from extract import extract_flights
from transform import transform_data
import pprint


def main():
    raw_data = extract_flights()
    data = transform_data(extract_flights())
    pprint.pprint(data)


if __name__ == "__main__":
    main()
