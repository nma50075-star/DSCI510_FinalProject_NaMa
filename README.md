# Airbnb Price Analysis in Los Angeles

## Introduction
This project analyzes Airbnb listing prices in Los Angeles. 
The goal is to understand the distribution of listing prices and identify general pricing patterns.

The project demonstrates a complete data pipeline:
- retrieving data from an API
- loading and cleaning dataset
- performing analysis
- generating visualizations

This project follows modular programming practices by organizing code into separate scripts in the src folder.

## Data Sources

| Source | Description | Type |
|-------|------------|------|
| InsideAirbnb dataset | Airbnb listing price data for Los Angeles | CSV dataset |
| OpenStreetMap API | Provides geographic location information | API |

## Analysis
The analysis focuses on price distribution of Airbnb listings.

Steps:
1. Load dataset using pandas
2. Clean the price column by removing symbols such as "$" and ","
3. Convert price values to numeric format
4. Plot histogram to visualize distribution of prices

The histogram helps identify the range of most common listing prices.

## Summary of Results
The price distribution visualization shows that most Airbnb listings fall within a mid-range price category, with fewer listings at extremely high prices.

The distribution is slightly right-skewed, meaning there are some listings with much higher prices compared to the majority.

## How to run

Step 1 install dependencies:

pip install -r requirements.txt

Step 2 run test:

python src/tests.py

Step 3 run pipeline:

python src/main.py

The program will:
- load dataset
- clean price column
- generate histogram plot

## Project structure

src/
    data_collection.py
    load.py
    process.py
    analyze.py
    main.py
    config.py
    tests.py

docs/
    Na_Ma_progress_report.pdf
    Na_Ma_presentation.pdf

requirements.txt
README.md
