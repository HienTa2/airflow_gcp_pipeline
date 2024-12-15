# Data Fusion GCP Pipeline

![Project Banner](assets/banner.png)

[![License](https://img.shields.io/github/license/HienTa2/airflow_gcp_pipeline)](LICENSE)
[![Issues](https://img.shields.io/github/issues/HienTa2/airflow_gcp_pipeline)](https://github.com/HienTa2/airflow_gcp_pipeline/issues)

---

## Overview

This project demonstrates an ETL pipeline using Apache Airflow and Google Cloud Platform (GCP) services. The pipeline extracts data from Google Cloud Storage (GCS), transforms it in Cloud Data Fusion, and loads it into BigQuery for analysis.

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Data Fusion Pipeline Setup](#data-fusion-pipeline-setup)
- [Contributing](#contributing)

---

## Features

- **Data Extraction**: Pulls data from Google Cloud Storage.
- **Data Transformation**: Processes data using Cloud Data Fusion.
- **Data Loading**: Loads transformed data into BigQuery.
- **Orchestration**: Manages ETL workflows with Apache Airflow.

---

## Architecture

![image](https://github.com/user-attachments/assets/a7e7df1f-f245-4a4f-93b5-4f770c44262c)


---

## Prerequisites

- Python 3.7 or higher
- Google Cloud SDK installed and configured
- Apache Airflow set up
- Access to the following GCP services:
  - BigQuery
  - Cloud Storage
  - Cloud Data Fusion

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/HienTa2/airflow_gcp_pipeline.git
   cd airflow_gcp_pipeline
   ```


## Set up a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```


## Set up Google Cloud credentials:
  ```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
  ```
## Set up local login without using service account:
  ```bash
gcloud auth application-default login
  ```

## Data Fusion Pipeline Setup

### Steps to Create the Pipeline

1. **Navigate to Cloud Data Fusion:**
   - Open **Cloud Data Fusion** in GCP.
   - Open the **Studio** and create a new pipeline.

2. **Add a GCS Source:**
   - Drag the **GCS Source** plugin onto the canvas.
   - Configure the plugin:
     - **Bucket**: `emp_data_etl`
     - **File Path**: `employee_data/employee_data.csv`
     - **Format**: `CSV`
   - Test the connection to ensure it works.

3. **Add the Wrangler Plugin (Optional for Data Transformation):**
   - Drag the **Wrangler** plugin onto the canvas and connect it to the **GCS Source**.
   - Open the **Wrangler** UI by clicking on the plugin and select **Configure**.
   - Use the Wrangler interface to:
     - **Rename Columns**: Rename any column headers by clicking on the column name and editing it.
     - **Filter Rows**: Remove rows based on specific conditions (e.g., "Filter rows where salary is greater than $50,000").
     - **Add Columns**: Add calculated fields or combine existing columns.
     - **Clean Data**: Trim spaces, remove null values, or standardize text formats.
   - Once the transformations are complete, save the configuration.
  
  ![Image 2](https://github.com/user-attachments/assets/faf54c8f-7a6e-4f09-9bbf-73372d522c10)

  <img src="https://github.com/user-attachments/assets/80f7e4ff-4614-427c-a67c-4b013755c2b5" alt="Image 3 Description" width="400">





4. **Add a BigQuery Sink:**
   - Drag the **BigQuery Sink** plugin onto the canvas.
   - Configure the plugin:
     - **Project ID**: `data-pipeline-444601`
     - **Dataset**: `etl_results`
     - **Table Name**: `employee_data`
   - Test the connection to ensure it works.
  

 ![{4BF3C5EB-FB97-4384-9CC3-43982675027E}](https://github.com/user-attachments/assets/e104fc33-1236-439b-a6cc-60090b419963)



6. **Connect the Plugins:**
   - Connect the **GCS Source** → **Wrangler** (if used) → **BigQuery Sink**.

7. **Validate and Deploy:**
   - Click on **Validate** to check for errors in the pipeline.
   - Once validated, click **Deploy**.

     
![{46A05AAE-F52C-4E84-80D4-0F6130930635}](https://github.com/user-attachments/assets/1128ac9c-25c3-49c1-a4b3-8a7d062ab172)


8. **Run the Pipeline:**
   - After deployment, click **Run** to execute the pipeline.
   - Monitor the progress from the **Pipeline Studio** dashboard.
  

  ![{A7F1218D-DB12-46D9-8709-92D855EBD21B}](https://github.com/user-attachments/assets/029e0656-a6ee-4888-b5aa-a316443a3744)



10. **Export the Pipeline:**
   - Once the pipeline is complete, export it as a JSON file:
     - Click the **Options Menu** (three dots in the top-right corner).
     - Select **Export Pipeline** and save it as `data_fusion_pipeline.json`.

---

### Wrangler Transformations Example
- Rename `first_name` to `First Name`.
- Remove rows where `department` is `null`.
- Add a new column `full_name` by concatenating `first_name` and `last_name`.

---




