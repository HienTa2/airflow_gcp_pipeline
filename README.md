# Airflow GCP Pipeline

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

4. **Add a BigQuery Sink:**
   - Drag the **BigQuery Sink** plugin onto the canvas.
   - Configure the plugin:
     - **Project ID**: `data-pipeline-444601`
     - **Dataset**: `etl_results`
     - **Table Name**: `employee_data`
   - Test the connection to ensure it works.

5. **Connect the Plugins:**
   - Connect the **GCS Source** → **Wrangler** (if used) → **BigQuery Sink**.

6. **Validate and Deploy:**
   - Click on **Validate** to check for errors in the pipeline.
   - Once validated, click **Deploy**.

7. **Run the Pipeline:**
   - After deployment, click **Run** to execute the pipeline.
   - Monitor the progress from the **Pipeline Studio** dashboard.

8. **Export the Pipeline:**
   - Once the pipeline is complete, export it as a JSON file:
     - Click the **Options Menu** (three dots in the top-right corner).
     - Select **Export Pipeline** and save it as `data_fusion_pipeline.json`.

---

### Wrangler Transformations Example
- Rename `first_name` to `First Name`.
- Remove rows where `department` is `null`.
- Add a new column `full_name` by concatenating `first_name` and `last_name`.

---

### Screenshot Example
Below is an example of how the Wrangler plugin looks when performing transformations:

![Cloud Data Fusion Wrangler Example](assets/screenshots/wrangler_example.png)



