#!/usr/bin/env python
import requests
import json
import pandas as pd
import sys
import logging
import os

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"


def parse_arg():
    """
    Parse the first argument to get the csv file
    """
    try:
        csv_file = sys.argv[1]
    except IndexError:
        logging.error(f"Usage: python {sys.argv[0]} <csv_file>")
        sys.exit(1)
    return csv_file


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


def transform(record):
    """
    Turn ISS JSON record into a single-row DataFrame.
    Turns the UNIX timestamp into YYYY-MM-DD HH:MM:SS format.
    """
    logging.info("Transforming JSON record into a properly formatted dataframe")
    
    longitude = float(record["iss_position"]["longitude"])
    latitude = float(record["iss_position"]["latitude"])
    timestamp = record["timestamp"]
    
    # Convert timestamp
    readable_time = pd.to_datetime(timestamp, unit="s")
    
    # Create dataframe
    df = pd.DataFrame([{
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": readable_time
    }])
    
    logging.info(f"Transformed: {df.shape[0]} row × {df.shape[1]} columns")
    
    return df


def load(df, csv_file):
    """
    Load: Append transformed data to the csv file.
    Creates a file if it doesn't exist.
    """
    if os.path.exists(csv_file):
        logging.info(f"{csv_file} exists. Appending new record.")
        
        # Read existing data
        existing_df = pd.read_csv(csv_file)
        
        # Append new record
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        
        # Rewrite full CSV
        combined_df.to_csv(csv_file, index=False)
        
    else:
        logging.info(f"{csv_file} does not exist. Creating new file.")
        df.to_csv(csv_file, index=False)
    
    logging.info(f"Loaded transformed data (saved to {csv_file})")


def main():
    """Run the complete ETL pipeline."""

    # Parse command line arguments
    csv_file = parse_arg()
    
    # Extract: Get data from API
    data = extract(URL)

    #in case the data does not extract properly
    if data is None:
        logging.error("Extraction failed. Exiting.")
        sys.exit(1)
    
    # Transform: Clean and organize data
    df = transform(data)
    
    # Load: Save to CSV and show summary
    load(df, csv_file)
    logging.info(f"Processed {len(df)} records")


# This block is executed only if the script is run directly, not imported as a module.
if __name__ == "__main__":
    main()