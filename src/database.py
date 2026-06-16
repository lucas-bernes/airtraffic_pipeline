import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def get_connection():

    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        print("Successfully connected to MySQL.")

        return conn

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        raise
