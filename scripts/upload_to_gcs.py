from google.cloud import storage
import os

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """
    Uploads a file to a Google Cloud Storage bucket.

    Args:
        bucket_name (str): Name of the GCS bucket.
        source_file_name (str): Path to the source file to upload.
        destination_blob_name (str): Name of the destination blob in the bucket.

    Returns:
        None
    """
    try:
        # Initialize the GCS client
        storage_client = storage.Client()

        # Get the bucket and blob
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        # Upload the file to the bucket
        blob.upload_from_filename(source_file_name)

        # Print confirmation message
        print(f"File '{source_file_name}' uploaded to '{destination_blob_name}' in bucket '{bucket_name}'.")
    except Exception as e:
        print(f"An error occurred while uploading the file: {e}")

# Example usage
if __name__ == "__main__":
    bucket_name = "hien-bkt-employee"
    source_file_name = os.path.join(os.path.dirname(__file__), "employee_data.csv")
    destination_blob_name = "employee_data.csv"  # This is the name you want in the bucket

    upload_to_gcs(bucket_name, source_file_name, destination_blob_name)
