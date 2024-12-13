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


## Set up a virtual environment:

python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate



## Set up Google Cloud credentials:
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"


## Data Fusion Pipeline Setup
### Steps to Create the Pipeline
  1. Navigate to Cloud Data Fusion in GCP.
  2. Open the Studio and create a new pipeline.
  3. Add the following components:
       * GCS Source:
            * Bucket: emp_data_etl
            * File Path: employee_data/employee_data.csv
       * Wrangler Plugin (Optional) for data transformation.
       * BigQuery Sink:
         * Project: data-pipeline-444601
         * Dataset: etl_results
         * Table: employee_data
  4. Validate and deploy the pipeline.
  5. Export the pipeline as data_fusion_pipeline.json.


