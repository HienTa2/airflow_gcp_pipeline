# Airflow GCP Pipeline

![Project Banner](assets/banner.png)

[![License](https://img.shields.io/github/license/HienTa2/airflow_gcp_pipeline)](LICENSE)
[![Issues](https://img.shields.io/github/issues/HienTa2/airflow_gcp_pipeline)](https://github.com/HienTa2/airflow_gcp_pipeline/issues)

## Overview

This project demonstrates an ETL pipeline using Apache Airflow and Google Cloud Platform (GCP) services. The pipeline extracts data from various sources, transforms it, and loads it into BigQuery for analysis.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Data Fusion Pipeline Setup](#data-fusion-pipeline-setup)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Data Extraction**: Retrieves data from multiple sources.
- **Data Transformation**: Processes and cleans data for analysis.
- **Data Loading**: Stores transformed data into BigQuery.
- **Orchestration**: Utilizes Apache Airflow for scheduling and monitoring.

## Architecture

![Architecture Diagram](assets/architecture.png)

## Prerequisites

- Python 3.7 or higher
- Google Cloud SDK
- Apache Airflow
- Access to GCP services: BigQuery, Cloud Storage, Data Fusion

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/HienTa2/airflow_gcp_pipeline.git
   cd airflow_gcp_pipeline
