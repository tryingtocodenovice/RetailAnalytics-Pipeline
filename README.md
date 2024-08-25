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
-   [Conclusion](#conclusion)

## Introduction

The goal of this project is to analyze customer interactions on an e-commerce website, identifying trends and patterns in customer behavior. The pipeline utilizes Dagster to orchestrate the loading, processing, and storage of data, ultimately delivering valuable insights for business decision-making.

## Data Source

The primary dataset used in this project is sourced from the [Retail Rocket dataset](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset), which contains anonymized interaction data from an e-commerce website. The dataset includes information on events like views, cart additions, and purchases, as well as item properties such as category and price.

## Pipeline Ov
