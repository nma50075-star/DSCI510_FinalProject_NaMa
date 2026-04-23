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

```bash text
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
```

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

```bash
data/  
├── airbnb_kaggle.csv  
├── insideairbnb_la.csv  
└── tourism.csv  
```

---

### 3. Run the pipeline
python -m src.main

---

### 4. Run tests (if required)
python -m src.tests

---

## Results

### 1. Price Distribution

The distribution of Airbnb listing prices is right-skewed, with most listings concentrated at lower price ranges and a small number of high-priced listings.

---

### 2. Price by Room Type

Entire homes/apartments have the highest average prices, while shared rooms are the most affordable. This reflects clear segmentation in the Airbnb market.

---

### 3. Price vs Reviews

There is no strong linear relationship between price and number of reviews. Lower-priced listings tend to receive more reviews, suggesting higher booking frequency.

---

### 4. Reviews by Room Type

Entire homes receive the highest number of reviews overall, indicating strong demand compared to other room types.

---

### 5. Tourism Trend

Tourism arrivals show an overall increasing trend over time with some fluctuations, likely due to seasonal or external factors.

---

### 6. Regional Comparison

Asia consistently contributes more visitors than Central America, highlighting regional differences in travel demand.

---

### Overall Insight

Airbnb pricing is primarily influenced by room type rather than popularity. Meanwhile, tourism trends suggest steady growth with regional variation, which may impact Airbnb demand.

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

## AI Usage

- Some portions of this project were developed with the assistance of ChatGPT, particularly for data cleaning and initial data visualization functions.
- All AI-generated code sections have been clearly labeled with `# AI generated:` as required.
- After understanding the initial examples, additional analysis and visualizations were implemented independently.

---

## Author

Na Ma  
Communication Data Science, USC  
