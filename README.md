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
- [License](#license)

---

## Features

- **Data Extraction**: Pulls data from Google Cloud Storage.
- **Data Transformation**: Processes data using Cloud Data Fusion.
- **Data Loading**: Loads transformed data into BigQuery.
- **Orchestration**: Manages ETL workflows with Apache Airflow.

---

## Architecture

![Architecture Diagram](assets/diagrams/data_fusion_pipeline.png)

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
