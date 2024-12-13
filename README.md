# airflow_gcp_pipeline
Creating ETL pipeline on GCP with Data Fusion and Airflow




![image](https://github.com/user-attachments/assets/445b8758-48bb-4866-b388-a7232b46a081)

Steps to Set Up Cloud Data Fusion Pipeline
Navigate to Cloud Data Fusion

Open Cloud Data Fusion from the Google Cloud Console.
Select your instance or create a new instance if one doesn’t exist.
Open the Studio

Click on "Studio" from the Cloud Data Fusion dashboard.
Create a New Pipeline

Click "Create Pipeline" and choose the pipeline type (Batch or Realtime).
Add a GCS Source

Drag the GCS Source plugin onto the canvas.
Configure the GCS Source:
Bucket: emp_data_etl
File path: employee_data/employee_data.csv
Format: CSV
Test the connection to ensure it works.
Add a Wrangler Plugin (Optional)

Drag a Wrangler plugin onto the canvas to clean or transform the data.
Configure it for basic operations like renaming columns or filtering rows.
Add a BigQuery Sink

Drag the BigQuery Sink plugin onto the canvas.
Configure it:
Project ID: data-pipeline-444601
Dataset: Create or use an existing dataset (e.g., etl_results).
Table Name: employee_data
Test the connection to ensure the table is accessible.
Connect the Plugins

Connect the GCS Source to the Wrangler (if used) and then to the BigQuery Sink.
Validate the Pipeline

Click on Validate to check for configuration errors.
Deploy and Run

Deploy the pipeline by clicking Deploy.
After deployment, click Run to execute the pipeline.
Export the Pipeline

Once the pipeline is complete, export it as a JSON file:
Go to the Options menu (three dots) in the pipeline editor.
Click Export Pipeline and save the file (e.g., data_fusion_pipeline.json).
