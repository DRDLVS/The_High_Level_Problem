# The High Level Problem

## Overview

This project focuses on designing and implementing a robust data engineering architecture. It includes data ingestion, storage, processing, access, and analysis layers. Each layer is crucial for managing and transforming data from various sources into actionable insights.

## Table of Contents

1. [Data Ingestion Layer](#data-ingestion-layer)
2. [Data Storage Layer](#data-storage-layer)
3. [Data Processing Layer](#data-processing-layer)
4. [Data Access Layer](#data-access-layer)
5. [Data Analysis Layer](#data-analysis-layer)
6. [Summary of Problem-Solving Approaches](#summary-of-problem-solving-approaches)

## 1. Data Ingestion Layer

**Objective:**
The Data Ingestion Layer is responsible for acquiring data from various sources, ensuring it is available for processing and analysis.

### Components and Processes

- **ETL/ELT Pipelines:** For structured and semi-structured data.
- **Tools:** Python scripts for ETL processes.

### Data Sources

- **Annual Tax Returns (3rd Party XML API):**
  - **Method:** Data is retrieved through API calls, managing authentication and rate-limiting.
  - **Tool:** Custom Python microservice for handling rate limits and parsing XML data.

- **Credit Card Transaction History (3rd Party JSON API and Internal PostgreSQL Databases):**
  - **Method:** API calls for external data and ETL jobs for internal databases.
  - **Tool:** Python scripts for batch ETL processes.

- **Bank Statements (3rd Party XML API, S3 Bucket, OCR for PDFs):**
  - **Method:** XML data is retrieved through API calls; S3 bucket data is processed in batches. OCR is used for extracting text from PDF bank statements.
  - **Tool:** AWS Lambda for S3 triggers, Python scripts for XML processing, and OCR libraries such as Tesseract or OCR.space API for PDFs.

### Example Code for XML Data Ingestion

**File: `main.py`**
```python
import pandas as pd
import requests
from lxml import etree

# Download the XML file from the URL
url = 'https://data.ny.gov/api/views/nacg-rg66/rows.xml?accessType=DOWNLOAD'
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    try:
        # Parse the XML file and convert it into a DataFrame
        parser = etree.XMLParser(remove_blank_text=True)
        root = etree.fromstring(response.content, parser)
        df = pd.read_xml(response.content, xpath='.//row', parser='lxml')

        # Display the structure of the DataFrame
        print("Available columns in the DataFrame:")
        print(df.columns)

        # Handle missing data
        print("Missing data in the DataFrame before cleaning:")
        print(df.isnull().sum())

        if 'tax_liability_of_nontaxable_returns_in_thousands' in df.columns:
            df.drop(columns=['tax_liability_of_nontaxable_returns_in_thousands'], inplace=True)

        df.dropna(subset=['tax_liability_of_taxable_returns_in_thousands', 'average_tax_of_taxable_returns'], inplace=True)

        df.fillna({
            'tax_year': 0,
            'resident_type': 'unknown',
            'place_of_residence': 'unknown',
            'country': 'unknown',
            'state': 'unknown',
            'county': 'unknown',
            'number_of_all_returns': 0,
            'ny_agi_of_all_returns_in_thousands': 0,
            'tax_liability_of_all_returns_in_thousands': 0,
            'number_of_taxable_returns': 0,
            'ny_agi_of_taxable_returns_in_thousands': 0,
            'number_of_nontaxable_returns': 0,
            'ny_agi_of_nontaxable_returns_in_thousands': 0,
            'average_ny_agi_of_all_returns': 0,
            'average_tax_of_all_returns': 0,
            'average_ny_agi_of_taxable_returns': 0,
            'average_tax_of_taxable_returns': 0,
            'average_ny_agi_of_nontaxable_returns': 0,
            'county_sort_order': 0
        }, inplace=True)

        for column in df.select_dtypes(include=['float64']).columns:
            df[column] = df[column].fillna(0).astype(int)

        print("Missing data in the DataFrame after cleaning:")
        print(df.isnull().sum())

        df.to_csv('tax_data_cleaned_v6.csv', index=False)
        print("Cleaned data saved to 'tax_data_cleaned_v6.csv'.")
    except ValueError as e:
        print(f"Error reading XML: {e}")
else:
    print(f"Error downloading the XML file. Status code: {response.status_code}")
```


## 2. Data Storage Layer


**Objective:**
The Data Storage Layer ensures secure and efficient storage of data, making it available for processing and querying.

### Components and Processes

- **S3 Bucket:** For scalable storage of raw and processed data files.
- **Redshift:** Data warehouse for storing structured data, enabling complex queries and analysis.

### Example Code for Loading Data into Redshift

**File: `load_to_redshift.py`**

```python
import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv('cleaned_transactions.csv')

# Redshift connection details
redshift_engine = create_engine('redshift+psycopg2://username:password@redshift-cluster:5439/database')

# Load data into Redshift
df.to_sql('transactions', redshift_engine, index=False, if_exists='append')
```


## 3. Data Processing Layer

**Objective:**
The Data Processing Layer transforms raw data into a format suitable for analysis, ensuring data quality and consistency.

### Components and Processes

- **ETL/ELT Pipelines:** Apply transformations, aggregations, and cleaning operations.
- **Batch Processing:** Handles large volumes of data through scheduled jobs.
- **Data Cleaning and Transformation:** Includes missing value handling, data type conversions, and feature engineering.

### Example Code for Data Transformation

**File: `transform_data.py`**
```python
import pandas as pd

# Load data
df = pd.read_csv('transactions.csv')

# Data transformation
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['amount'] = df['amount'].astype(float)

# Filter and clean data
df = df[df['status'] == 'completed']

# Save transformed data
df.to_csv('cleaned_transactions.csv', index=False)
```


## 4. Data Access Layer

**Objective:**
The Data Access Layer provides tools and interfaces for accessing and visualizing data.

### Components and Processes

- **Power BI:** For interactive visualizations and business intelligence.
- **Tableau:** For creating a wide range of interactive and shareable dashboards.

### Configuration Steps

1. Connect Power BI/Tableau to data sources (e.g., Redshift).
2. Configure dashboards to visualize key metrics and trends.

## 5. Data Analysis Layer

**Objective:**
The Data Analysis Layer extracts actionable insights from data through statistical analysis, data visualization, and machine learning.

### Components and Processes

- **Python (Pandas, NumPy, Matplotlib, Seaborn):** For data manipulation, visualization, and statistical analysis.
- **SQL Queries:** For querying structured data in Redshift or PostgreSQL.
- **Machine Learning Models:** For predictive analytics and advanced data insights.

### Example Code for Data Analysis in Python

**File: `analyze_data.py`**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load cleaned CSV data
df = pd.read_csv('tax_data_cleaned_v6.csv')

# Basic descriptive analysis
print(df.describe())

# Data visualization
plt.figure(figsize=(10, 6))
sns.histplot(df['average_tax_of_taxable_returns'], kde=True)
plt.title('Distribution of Average Tax of Taxable Returns')
plt.xlabel('Average Tax')
plt.ylabel('Frequency')
plt.show()

# Simple regression model
X = df[['ny_agi_of_taxable_returns_in_thousands']]
y = df['average_tax_of_taxable_returns']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f'R^2 Score: {score}')
```

## 6. Summary of Problem-Solving Approaches

### Data Ingestion

- **Problem:** Efficiently gather and process data from diverse sources.
- **Solution:** Implemented ETL/ELT pipelines using Python. Used OCR for extracting data from PDF bank statements.

### Data Storage

- **Problem:** Securely store data for efficient access and analysis.
- **Solution:** Utilized AWS S3 for scalable storage and Redshift for structured data warehousing.

### Data Processing

- **Problem:** Transform raw data into clean, analyzable formats.
- **Solution:** Applied ETL processes and batch jobs for data cleaning and transformation.

### Data Access

- **Problem:** Make data accessible for visualization and analysis.
- **Solution:** Leveraged Power BI and Tableau for interactive visualizations and dashboard creation.

### Data Analysis

- **Problem:** Extract insights from processed data.
- **Solution:** Employed Python for data analysis, including statistical modeling and machine learning.
