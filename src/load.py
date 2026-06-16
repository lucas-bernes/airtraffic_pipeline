from database import get_connection


def load_flights(flights: list):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO flight_tracker (
        timestamp,
        icao24,
        callsign,
        origin_country,
        latitude,
        longitude,
        altitude,
        velocity
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        for flight in flights:

            cursor.execute(
                query,
                (
                    flight.get("datetime"),
                    flight.get("icao24"),
                    flight.get("callsign").strip() if flight.get(
                        "callsign") else None,
                    flight.get("origin_country"),
                    flight.get("latitude"),
                    flight.get("longitude"),
                    flight.get("altitude"),
                    flight.get("velocity")
                )
            )

        conn.commit()
        print(f"{len(flights)} records successfully inserted.")

    except Exception as e:
        conn.rollback()
        print(f"Error inserting data: {e}")
        raise

    finally:
        cursor.close()
        conn.close()
