# airflow_gcp_pipeline
Creating ETL pipeline on GCP with Data Fusion and Airflow




![image](https://github.com/user-attachments/assets/445b8758-48bb-4866-b388-a7232b46a081)

## Steps to Set Up Cloud Data Fusion Pipeline

### 1. Navigate to Cloud Data Fusion
- Open **Cloud Data Fusion** from the Google Cloud Console.
- Select your instance or create a new instance if one doesn’t exist.

### 2. Open the Studio
- On the Cloud Data Fusion dashboard, click on **"Studio"** to access the pipeline editor.

### 3. Create a New Pipeline
- Click on **"Create Pipeline"**.
- Choose the pipeline type:
  - **Batch Pipeline**: For batch processing.
  - **Realtime Pipeline**: For streaming data.

### 4. Add a GCS Source
- Drag the **GCS Source** plugin onto the canvas.
- Configure the GCS Source:
  - **Bucket Name**: `emp_data_etl`
  - **File Path**: `employee_data/employee_data.csv`
  - **File Format**: `CSV`
- Test the connection to ensure it works.

### 5. Add a Wrangler Plugin (Optional)
- Drag the **Wrangler** plugin onto the canvas to clean or transform data.
- Use the plugin to:
  - Rename columns.
  - Filter rows.
  - Perform other data transformation tasks.

### 6. Add a BigQuery Sink
- Drag the **BigQuery Sink** plugin onto the canvas.
- Configure the BigQuery Sink:
  - **Project ID**: `data-pipeline-444601`
  - **Dataset**: Create or use an existing dataset (e.g., `etl_results`).
  - **Table Name**: `employee_data`
- Test the connection to ensure the table is accessible.

### 7. Connect Plugins
- Connect the **GCS Source** to the **Wrangler** (if used), and then to the **BigQuery Sink**.

### 8. Validate the Pipeline
- Click **"Validate"** to check for any configuration errors.

### 9. Deploy and Run
- Click **"Deploy"** to save and deploy the pipeline.
- Once deployed, click **"Run"** to execute the pipeline.

### 10. Export the Pipeline
- After running the pipeline, export it as a JSON file:
  - Click on the **Options Menu** (three dots in the top-right corner of the editor).
  - Select **Export Pipeline** and save it as `data_fusion_pipeline.json`.

---

