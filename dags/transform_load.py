from google.cloud import bigquery

def load_data_to_bigquery(dataset_id, table_id, source_uri):
    """Loads data from GCS to BigQuery."""
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    load_job = client.load_table_from_uri(source_uri, table_ref, job_config=job_config)
    print(f"Starting job {load_job.job_id}")

    load_job.result()  # Wait for the job to complete
    print(f"Table {table_id} loaded successfully.")

if __name__ == "__main__":
    # Define variables
    dataset_id = "your_dataset_id"
    table_id = "your_table_id"
    source_uri = "gs://your_bucket_name/processed_data/data.csv"

    # Load the data
    load_data_to_bigquery(dataset_id, table_id, source_uri)

