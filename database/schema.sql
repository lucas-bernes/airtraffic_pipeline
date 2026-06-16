CREATE DATABASE IF NOT EXISTS flight_tracker;

USE flight_tracker;

CREATE TABLE IF NOT EXISTS flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    datetime DATETIME,
    icao24 VARCHAR(20),
    callsign VARCHAR(20),
    origin_country VARCHAR(100)
);