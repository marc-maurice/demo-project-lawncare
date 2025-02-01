import boto3
import os
import json
from datetime import datetime, timedelta
from generate_daily_data import generate_daily_data

# Initialize S3 client
s3_client = boto3.client("s3")

def check_if_file_exists(bucket_name, file_name):
    try:
        s3_client.head_object(Bucket=bucket_name, Key=file_name)
        return True
    except s3_client.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            return False
        raise

def lambda_handler(event, context):
    # Read environment variables
    bucket_name = os.environ['BUCKET_NAME']
    daily_folder = os.environ['DAILY_FOLDER']

    # Define the date for the incremental load (yesterday)
    date = datetime.now() - timedelta(days=1)
    file_name = f"{daily_folder}{date.strftime('%Y-%m-%d')}.json"

    # Check if the file already exists
    if check_if_file_exists(bucket_name, file_name):
        return {
            "statusCode": 400,
            "body": f"Daily data file {file_name} already exists in {bucket_name}."
        }

    # Generate daily data
    daily_data = generate_daily_data(date)

    # Upload the file to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(daily_data)
    )

    return {
        "statusCode": 200,
        "body": f"Daily data for {date.strftime('%Y-%m-%d')} written to {file_name} in {bucket_name}."
    }
