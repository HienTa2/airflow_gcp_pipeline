from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import extract_data
import transform_load

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "etl_pipeline",
    default_args=default_args,
    description="ETL pipeline using Airflow and GCP",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data.upload_to_gcs,
        op_kwargs={
            "bucket_name": "your_bucket_name",
            "source_file_name": "data.csv",
            "destination_blob_name": "raw_data/data.csv",
        },
    )

    transform_load_task = PythonOperator(
        task_id="transform_and_load_data",
        python_callable=transform_load.load_data_to_bigquery,
        op_kwargs={
            "dataset_id": "your_dataset_id",
            "table_id": "your_table_id",
            "source_uri": "gs://your_bucket_name/processed_data/data.csv",
        },
    )

    extract_task >> transform_load_task
