import boto3
import os
import json
from datetime import datetime, timedelta
from generate_data import generate_historical_data_for_date

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
    historicals_folder = os.environ['HISTORICALS_FOLDER']

    # Define date range: 2.5 years ago up to 2 days ago
    end_date = datetime.now() - timedelta(days=2)
    start_date = datetime.now() - timedelta(days=2.5 * 365)

    # Generate data for each day in the range
    current_date = start_date
    while current_date < end_date:
        file_name = f"{historicals_folder}{current_date.strftime('%Y-%m-%d')}.json"

        # Check if the file already exists
        if check_if_file_exists(bucket_name, file_name):
            print(f"File {file_name} already exists. Skipping...")
        else:
            # Generate data for the current date
            daily_data = generate_historical_data_for_date(current_date)

            # Upload the file to S3
            s3_client.put_object(
                Bucket=bucket_name,
                Key=file_name,
                Body=json.dumps(daily_data)
            )
            print(f"Uploaded file {file_name} to S3.")

        # Move to the next day
        current_date += timedelta(days=1)

    return {
        "statusCode": 200,
        "body": "Historical data generation completed."
    }
