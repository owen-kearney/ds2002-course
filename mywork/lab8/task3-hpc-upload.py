#!/usr/bin/env python
import sys
import logging
import os
import boto3
import glob


#logging config
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])


def parse_args():
    """
    Parses and returns the arguments given in the command line
    Arguments are the input folder and the destination
    """
    if len(sys.argv) != 3:
        print("Usage: python task3-hpc-upload.py <input_folder> <bucket/prefix/>", file=sys.stderr)
        sys.exit(1)
    return sys.argv[1], sys.argv[2]


def upload(input_folder, destination):
    """
    Uploads the results-*.csv files from the scratch directory
    to the S3 cloud storage
    """
    try:
        s3 = boto3.client('s3', region_name='us-east-1')
        #split desination into bucket and prefix parts
        parts = destination.split('/', 1)
        bucket = parts[0]
        prefix = parts[1] if len(parts) > 1 else ""

        #looks through the folder for all matching files using the wildcard
        files = glob.glob(os.path.join(input_folder, "results-*.csv"))

        if not files:
            logging.warning("No files found to upload.")
            return False

        for file_path in files:
            filename = os.path.basename(file_path)
            key = os.path.join(prefix, filename)
            logging.info(f"Uploading {filename} to s3://{bucket}/{key}")
            s3.upload_file(file_path, bucket, key)
        return True
    
    except Exception as e:
        logging.error(f"Error during upload: {e}")
        return False
        


def main():
    """
    Calls the parse_args and upload functions
    """
    input_folder, destination = parse_args()
    uploaded = upload(input_folder, destination)

    if uploaded:
        logging.info("Upload completed successfully.")
    else:
        logging.error("Upload failed.")



if __name__ == "__main__":
    main()