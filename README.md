# **🏗️ End-to-End ELT Data Pipeline with AWS, Snowflake, dbt, and Looker**

## **Project Overview**

This project implements a **scalable ELT data pipeline** using **AWS, Snowflake, and dbt** to process and transform raw **OLTP transactional data** into analytics-ready data for **business intelligence (BI) reporting** in Looker.

### **🔹 Key Technologies Used**

- **AWS Lambda** → Data generation & processing
- **AWS Glue** → ETL jobs & metadata cataloging
- **AWS S3** → Cloud storage for raw & processed data
- **Snowflake** → Cloud-based data warehouse
- **dbt (Data Build Tool)** → Data transformation & modeling
- **Apache Airflow** → Workflow automation & scheduling
- **Looker** → BI dashboards and visualizations

---

## **🔄 End-to-End Data Flow & Architecture**

### **Step 0: Clear Out Previous Demo Data**

Before running the demo, existing data is deleted from **S3** to prevent conflicts.

- **AWS Lambda Function: `demo-lawncare-co-cleanup-mm`**
    - Deletes all files in `s3://demo-lawncare-co-mm/landing/`
    - Ensures a clean environment for demo runs.

---

## **🛠️ Step 1: Generate Historical OLTP Data**

A **Lambda function** generates **2.5 years of historical transaction data**.

- **AWS Lambda Function: `demo-lawncare-co-historicals-mm`**
    - Creates **50 locations' worth of transactional data**.
    - Saves **CSV files** in **S3 (`landing/historicals/`)**.
    - **Example data fields**: Transactions, customers, payments, discounts.

---

## **🛠️ Step 2: Generate Daily Incremental OLTP Data**

A separate **Lambda function** generates **daily incremental transactions**.

- **AWS Lambda Function: `demo-lawncare-co-daily-mm`**
    - Generates **daily OLTP data**.
    - Saves **JSON files** in **S3 (`landing/daily/`)**.

---

## **🛠️ Step 3: Glue Crawlers – Catalog Data**

AWS **Glue Crawlers** scan **S3** to detect and store metadata.

- **AWS Glue Crawlers:**
    - **Crawler 1: `demo-lawncare-co-historicals-crawler-mm`**
    - **Crawler 2: `demo-lawncare-co-daily-crawler`**
    - Scans `landing/historicals/` and `landing/daily/` S3 locations.
    - Creates **Glue Data Catalog tables**.

---

## **🛠️ Step 4: Glue ETL – Raw to Staged Data in S3**

AWS Glue ETL processes and converts raw OLTP data into **cleaned Parquet files**.

- **AWS Glue Job: `Raw to Staged`**
    - Converts raw CSV data into **Parquet** format.
    - **Source:** `landing/historicals/` & `landing/daily/`
    - **Target:** `staged/historicals/` & `staged/daily/`

---

## **🛠️ Step 5: Load Data into Snowflake**

Summary of the Ingestion Process:

- **Snowflake Storage Integration** enables secure access to **S3**.
- **External Stage (`demo_lawncare_stage`)** references the **staged Parquet files**.
- **Staging Table (`stg_parquet`)** is used to store ingested raw data.
- **COPY INTO command** loads **staged Parquet files** from **S3 to Snowflake**.

---

## **📂 Step 6: Transform & Model Data with dbt**

Once data is in Snowflake, **dbt transforms it** into **structured analytics-ready models**.

### **📌 dbt Architecture**

| Layer | Purpose |
| --- | --- |
| **Staging** | Extracts raw data from Snowflake |
| **Cleansed** | Standardizes formats, removes duplicates |
| **Core** | Fact and dimension tables |
| **Marts** | Business-ready reporting tables |
| **Viz Queries** | Aggregated queries for BI dashboards |

### **📂 Folder Structure**

```
demodbtlawncare/
│── models/
│   ├── staging/
│   ├── cleansed/
│   ├── core/
│   ├── marts/
│   ├── viz_queries/
```

---

## **📊 Step 7: Visualization in Looker**

The **Looker dashboard** connects to **Snowflake’s marts**.

### **YTD Flash Looker Report**

- Filters: **Service Type, Customer Segment**
- **Revenue Summary**
    - Current Year
    - Previous Year
    - All Time
- **Key Visuals:**
    - Year-over-year revenue trends
    - Total transactions per service type
    - Customer count per segment