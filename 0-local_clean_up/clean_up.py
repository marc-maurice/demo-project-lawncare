import boto3

# Initialize S3 client
s3_client = boto3.client("s3")

# Specify your bucket and folder
bucket_name = "demo-lawncare-co-mm"
landing_folder = "landing/"

def clean_landing_folder(bucket_name, prefix):
    # List objects in the specified folder
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    
    if "Contents" in response:
        objects_to_delete = [{"Key": obj["Key"]} for obj in response["Contents"]]
        
        # Batch delete objects
        delete_response = s3_client.delete_objects(
            Bucket=bucket_name,
            Delete={"Objects": objects_to_delete}
        )
        print(f"Deleted the following objects from {bucket_name}/{prefix}:")
        for deleted in delete_response.get("Deleted", []):
            print(deleted["Key"])
    else:
        print(f"No objects found in {bucket_name}/{prefix}.")

# Call the function to clean the landing folder
clean_landing_folder(bucket_name, landing_folder)
