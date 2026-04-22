# DSCI510 Final Project  
## Airbnb Pricing and Tourism Trend Analysis

---

## Project Overview

This project explores factors that influence Airbnb pricing and connects short-term rental patterns with broader tourism trends. By combining multiple datasets, the analysis provides insights into pricing behavior, user engagement, and demand dynamics in the short-term rental market.

The project follows a structured data pipeline, including data collection, cleaning, analysis, and visualization.

---

## Objectives

- Analyze the distribution of Airbnb prices
- Understand how room type affects pricing
- Explore the relationship between price and user engagement (reviews)
- Examine the impact of minimum stay requirements on pricing
- Identify tourism trends over time
- Compare visitor trends across different regions

---

## Datasets

This project integrates three datasets:

### 1. Kaggle Airbnb Open Data
- Source: Kaggle  
- Purpose: Main dataset for pricing analysis  
- Key variables:
  - `price`
  - `minimum_nights`
  - `number_of_reviews`
  - `room_type`

---

### 2. InsideAirbnb Los Angeles Listings Data
- Source: InsideAirbnb  
- Purpose: Supplementary dataset for room type and review analysis  
- Key variables:
  - `room_type`
  - `number_of_reviews`

---

### 3. Tourism Dataset (International Visitors)
- Source: Public tourism statistics dataset  
- Purpose: Analyze long-term tourism trends  
- Key variables:
  - `time`
  - `total`
  - `asia`
  - `central_america`

---

## Project Structure

```text
DSCI510_FinalProject_NaMa-main/
├── doc/
│   └── Na_Ma_progress_report.pdf
├── src/
│   ├── __init__.py
│   ├── analyze.py
│   ├── config.py
│   ├── data_collection.py
│   ├── load.py
│   ├── main.py
│   ├── process.py
│   └── tests.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── results.ipynb

---

## Data Processing Pipeline

The project is organized into modular components:

- load.py → Load datasets from local files  
- process.py → Clean and standardize data  
- analyze.py → Generate visualizations  
- main.py → Execute the full pipeline  

---

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

---

### 2. Prepare datasets

Create a `data/` folder and place the datasets inside:

data/  
├── airbnb_kaggle.csv  
├── insideairbnb_la.csv  
└── tourism.csv  

---

### 3. Run the pipeline
python -m src.main

---

### 4. Run tests (if required)
python -m src.tests

---

## Results

The project generates multiple visualizations to support analysis:

- Distribution of Airbnb prices  
- Average price by room type  
- Price vs minimum nights  
- Price vs number of reviews  
- Average reviews by room type  
- Tourism trends over time  
- Comparison of visitors from Asia vs Central America  

---

## Key Insights

- Airbnb pricing varies significantly across listings, with room type acting as an important positioning factor.  
- Listings with higher review counts do not always have higher prices, suggesting that popularity and pricing are not perfectly aligned.  
- Tourism data shows a long-term increase in international visitors, especially from Asia, indicating growing demand that may influence short-term rental markets.  

---

## Notes

- The `data/` and `results/` folders are excluded from the repository as required.  
- `.env.example` is provided as a template for environment variables. Real keys should not be uploaded.  
- This project focuses on data analysis and visualization using Python.  

---

## Author

Na Ma  
Communication Data Science, USC  
