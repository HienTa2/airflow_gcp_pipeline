
import os
from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

if __name__ == "__main__":
    # Define variables
    bucket_name = "your_bucket_name"
    source_file_name = "data.csv"  # Replace with your local file
    destination_blob_name = "raw_data/data.csv"

    # Upload the file
    upload_to_gcs(bucket_name, source_file_name, destination_blob_name)
