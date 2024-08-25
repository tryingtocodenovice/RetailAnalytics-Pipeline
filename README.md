# Retail Analytics Pipeline using Dagster

This repository contains a data pipeline for analyzing e-commerce data using [Dagster](https://dagster.io/). The pipeline loads, processes, and materializes data to derive insights from a retail dataset. It demonstrates how to manage assets, perform transformations, and store results using the Dagster orchestrator.

## Table of Contents

-   [Introduction](#introduction)
-   [Data Source](#data-source)
-   [Pipeline Overview](#pipeline-overview)
-   [Assets and Operations](#assets-and-operations)
    -   [Data Loading](#data-loading)
    -   [Data Transformation](#data-transformation)
    -   [Aggregation and Analysis](#aggregation-and-analysis)
    -   [Materialization](#materialization)
-   [Insights Derived](#insights-derived)
-   [Setup and Execution](#setup-and-execution)
-   [Testing the Pipeline](#testing-the-pipeline)
-   [Verifying Results](#verifying-results)
-  [ Notes and Future Enhancement](#notes-and-future-enhancement)

## Introduction

The goal of this project is to analyze customer interactions on an e-commerce website, identifying trends and patterns in customer behavior. The pipeline utilizes Dagster to orchestrate the loading, processing, and storage of data, ultimately delivering valuable insights for business decision-making.

## Data Source

The primary dataset used in this project is sourced from the [Retail Rocket dataset](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset), which contains anonymized interaction data from an e-commerce website. The dataset includes information on events like views, cart additions, and purchases, as well as item properties such as category and price.

## Pipeline Overview

The pipeline consists of several components designed to load, transform, and analyze the e-commerce data:

1.  **Data Loading**: Reads event and item property data from CSV files.
2.  **Data Transformation**: Merges events with item properties and performs calculations.
3.  **Aggregation and Analysis**: Computes statistics such as event type counts and hourly trends.
4.  **Materialization**: Stores the processed data into SQLite tables for further analysis.

## Assets and Operations

### Data Loading

-   **`load_events_data`**: Loads event data from a CSV file, converts timestamps to datetime, and applies hourly partitions.
-   **`load_item_properties_data`**: Loads item properties data from two CSV files, concatenates them, converts timestamps to datetime, and retains the latest value for each item-property pair.

### Data Transformation

-   **`transform_and_join_data`**: Joins event data with item properties data to create a unified dataset. This dataset includes calculated fields such as time since the last event, the hour of the day, the previous event type, and a flag indicating if a 'view' event led to a 'purchase'.

### Aggregation and Analysis

-   **`event_type_analysis`**: Aggregates event data to count occurrences of each event type (view, cart, purchase) per hour.
-   **`hourly_trend_analysis`**: Analyzes hourly trends by computing the rolling average of event counts, providing insights into changes in customer behavior over time.

### Materialization

-   **`materialize_data`**: Stores the processed data into SQLite tables. The data is materialized into the following tables: `table_1` for events, `table_2` for item properties, `joined_table` for the merged dataset, `hourly_trend` for hourly trends, and `event_type_counts` for event type counts.

## Insights Derived

The pipeline enables the following insights:

1.  **Customer Behavior Trends**: By analyzing the hourly trends, the pipeline can identify peak hours for customer activity, helping businesses optimize staffing and marketing strategies.
2.  **Event Sequence Analysis**: The `view_to_purchase` flag indicates how often views lead to purchases, providing insights into conversion rates.
3.  **Product Popularity**: Aggregated counts of events by type reveal which products are viewed most often and which are most frequently added to the cart or purchased.
4.  **Impact of Time**: The time since the last event and the hour of the day can help understand how customer behavior varies over time, potentially indicating the influence of time-based promotions or sales.

## Setup and Execution

1.  **Clone the Repository**:
    
    bash
    
        
    `git clone https://github.com/your-username/retail-analytics-pipeline.git
    cd retail-analytics-pipeline` 
    
2.  **Install Dependencies**:
    
    It's recommended to use a virtual environment. Install dependencies using the `requirements.txt` file:
    
    bash
    
   
    
    ``python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt`` 
    
3.  **Run the Pipeline**:
    
    You can execute the Dagster job using the following command:
    
    bash
    
    
    `dagster job execute -f dagster_pipeline.py -j retailAnalytics_job` 
    
    This command runs the entire pipeline, which will load the data, process it, and store the results in the specified SQLite database.

## Testing the Pipeline

To test the pipeline, you can use the predefined test files located in the `tests` directory. Follow the steps below to run the tests:

1.  **Navigate to the Tests Directory**:
    
    Change your current directory to the `tests` directory:
        
    `cd tests` 
    
2.  **Run the Tests**:
    
    Use the following command to run all test files using `pytest`:
    
    bash
        
    `pytest` 
    
    This command will execute `test_load_events_data.py`, `test_transform_and_join_data.py`, and `test_load_item_properties_data.py` to ensure each component of the pipeline is working as expected.

## Verifying Results

After running the pipeline, you can verify the results by inspecting the SQLite database using the provided Python function. 

1.  **Navigate to the Tests Directory**:
    
    Change your current directory to the `tests` directory:
        
    `cd tests` 
    
2.  **Run the Verification Script**:

   
    `python verify_results.py`

## Notes and Future Enhancement

-   **Improving Logging and Error Handling**:
    
    -   Logging has been implemented to provide detailed insights into the pipeline execution, aiding in troubleshooting and monitoring. Future work could enhance logging to include more granular details on memory usage and system resource consumption.
    -   Robust error handling has been added to catch exceptions and log relevant error messages, ensuring that failures are diagnosed effectively. Ongoing efforts can focus on refining these mechanisms to anticipate and manage other potential failure scenarios.
-   **Scalability Considerations**:
    
    -   The current setup is designed for a single SQLite database, suitable for small to medium-scale data. For handling larger datasets or production-level applications, consider migrating to more scalable database solutions such as PostgreSQL or Amazon RDS.
    -   Future enhancements may include implementing distributed processing capabilities using frameworks like Apache Spark or Dask to handle larger datasets efficiently.
-   **Testing and Verification**:
    
    -   Unit tests have been implemented to ensure the integrity of data loading and transformation operations. Continuous integration and deployment (CI/CD) pipelines could be introduced to automate testing and deployment, ensuring that changes do not introduce regressions.

-   **Data Quality and Monitoring**:
    
    -   Implementing data quality checks and monitoring tools to track the health and quality of data throughout the pipeline would be beneficial. This could include anomaly detection, data completeness checks, and tracking data lineage.
    -   Alerts and notifications for pipeline failures or data quality issues could be integrated to provide proactive monitoring and response capabilities.


 



    
