CREATE TABLE IF NOT EXISTS flight_tracker (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    icao24 VARCHAR(20),
    callsign VARCHAR(20),
    origin_country VARCHAR(100),
    latitude DOUBLE,
    longitude DOUBLE,
    altitude DOUBLE,
    velocity DOUBLE
);