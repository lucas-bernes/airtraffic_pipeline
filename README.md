# Flight Tracker ETL Pipeline

This project is a simple ETL pipeline that extracts real-time flight data from the OpenSky Network API, transforms it, and loads it into a MySQL database.

## Overview

The pipeline performs three main steps:

1. Extract: Fetches raw flight data from OpenSky API
2. Transform: Cleans and structures the data
3. Load: Stores processed data into a MySQL database

## Project Structure

flight-tracker/
├── dags/
│   └── flights_dag.py
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── database.py
│   ├── db_init.py
│   └── main.py
├── sql/
│   └── schema.sql
├── requirements.txt
└── README.md

## Data Source

OpenSky Network API  
https://opensky-network.org/apidoc/rest.html

## Database Schema

The main table stores flight state data:

- datetime: timestamp of the observation
- icao24: aircraft unique identifier
- callsign: flight identifier
- origin_country: country of registration

## Setup Instructions

### 1. Clone the repository

git clone <repo-url>  
cd flight-tracker

### 2. Create virtual environment

python -m venv .venv

Linux/Mac:
source .venv/bin/activate

Windows:
.venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Configure environment variables

Create a .env file:

DB_HOST=localhost  
DB_USER=root  
DB_PASSWORD=your_password  
DB_NAME=flight_tracker

### 5. Initialize database

Run:

python src/db_init.py

Or run SQL manually:

mysql -u root -p < sql/schema.sql

### 6. Run the pipeline

python src/main.py

## Notes

- This project is for learning ETL concepts
- Data is pulled from a live API and may change over time
- No orchestration tool (Airflow) is used in this version

## Possible Improvements

- Add Airflow orchestration
- Add Docker support
- Implement batch inserts
- Add deduplication logic
- Improve logging and error handling