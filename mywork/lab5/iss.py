#!/usr/bin/env python
import mysql.connector
import requests
import json
import pandas as pd
import sys
import logging
import os

# db config stuff
DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "iss"

db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DB)

#logging config
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"


def register_reporter(table, reporter_id, reporter_name):
    """
    Registers the reporter into the reporters table in the database
    If the reporter is already there, skip the insert
    """
    try:
        cursor = db.cursor()
        check_query = f"select reporter_id from {table} where reporter_id = %s"
        cursor.execute(check_query, (reporter_id,))
        result = cursor.fetchall()

        if len(result) == 0:
            #reporter is not in the table yet, insert them into it
            logging.info("Reporter not found in reporters table. Inserting them into reporters.")
            insert_query = f"insert into {table} (reporter_id, reporter_name) values (%s, %s)"
            cursor.execute(insert_query, (reporter_id, reporter_name))
            db.commit()
        else:
            #reporter already in table, skip inserting
            logging.info("Reporter already in reporters table. Skipping insertion.")
        
    except Exception as e:
        logging.error(f"Error connecting to MySQL: {e}")
    finally:
        cursor.close()


def extract(url):
    """
    Download ISS location data from API.
    Returns parsed JSON record.
    """
    logging.info(f"Getting data from {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        logging.info("Successfully extracted ISS data")
        return data
        
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error occurred: {e}")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
    
    return None


def load(record, reporter_id):
    """
    Insert current iss location into locations table
    Convert time from unix to readable day month year time
    """
    try:
        cursor = db.cursor()
        message = record["message"]
        latitude = float(record["iss_position"]["latitude"])
        longitude = float(record["iss_position"]["longitude"])
        timestamp = record["timestamp"]

        # Convert timestamp
        readable_time = pd.to_datetime(timestamp, unit="s")

        insert_query = "insert into locations (message, latitude, longitude, timestamp, reporter_id) values (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (message, latitude, longitude, readable_time, reporter_id))
        db.commit()
        logging.info("Inserted the current ISS location into the database")

    except Exception as e:
        logging.error(f"Error connecting to MySQL: {e}")

    finally:
        cursor.close()
    


def main():
    """Establish reporter and perform ETL pipline to insert ISS location into the database"""
    reporter_id = "uak4ux"
    reporter_name = "Owen Kearney"
    try:
        register_reporter("reporters", reporter_id, reporter_name)

        data = extract(URL)
        if data is None:
            logging.error("Extraction failed. Exiting.")
            sys.exit(1)

        load(data, reporter_id)

    except Exception as e:
        logging.error(f"Unexpected error: {e}")

    finally:
        db.close()
        logging.info("Database connection closed")

    


# This block is executed only if the script is run directly, not imported as a module.
if __name__ == "__main__":
    main()