from google.cloud import storage

def list_files(bucket_name):
    """Lists all files in the bucket."""
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    print(f"Files in {bucket_name}:")
    for blob in blobs:
        print(blob.name)

if __name__ == "__main__":
    bucket_name = "your_bucket_name"
    list_files(bucket_name)

