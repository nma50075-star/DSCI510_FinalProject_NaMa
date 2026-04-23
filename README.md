# DSCI510 Final Project – Airbnb Pricing & Tourism Analysis

## Introduction

This project explores the relationship between Airbnb pricing patterns and tourism trends. By analyzing Airbnb listing data alongside international tourism statistics, the goal is to understand how external demand factors may influence short-term rental markets.

---

## Data Sources

| Dataset          | Source                  | Description                                             |
| ---------------- | ----------------------- | ------------------------------------------------------- |
| Airbnb Open Data | Kaggle                  | Listing details including price, room type, and reviews |
| Inside Airbnb LA | InsideAirbnb            | Detailed Los Angeles Airbnb listing data                |
| Tourism Data     | Kaggle / public dataset | Monthly international visitor arrivals                  |

---

## Analysis

The project includes the following analyses:

* Distribution of Airbnb listing prices
* Average price by room type
* Relationship between price and number of reviews
* Price vs minimum nights requirement
* Reviews distribution across room types
* Tourism trend over time
* Comparison of tourism arrivals between Asia and Central America

---

## Summary of the Results

* Airbnb pricing varies significantly across listings, with room type acting as an important factor
* Listings with higher review counts do not always have higher prices
* Tourism data shows a long-term increase in international visitors, especially from Asia
* External demand trends may influence short-term rental markets over time

---

## How to Run

### Step 1: Install dependencies

```
pip install -r requirements.txt
```

### Step 2: Prepare data

Create a `data/` folder in the project root and place the following files:

* Airbnb Kaggle dataset → `data/airbnb_kaggle.csv`
* Inside Airbnb LA dataset → `data/insideairbnb_la.csv`
* Tourism dataset → `data/tourism.csv`

Note: Data files are not included in this repository as required.

---

### Step 3: Run the pipeline

```
python -m src.main
```

This will:

* Load datasets
* Clean and process data
* Generate visualizations in the `results/` folder

---

### Step 4: Run notebook (optional)

```
results.ipynb
```

This notebook imports functions from `src/` and reproduces the analysis.

---

## Project Structure

```
DSCI510_FinalProject_NaMa/
├── doc/
│   ├── Na_Ma_progress_report.pdf
│   ├── Na_Ma_presentation.pdf
├── src/
│   ├── __init__.py
│   ├── analyze.py
│   ├── config.py
│   ├── data_collection.py
│   ├── load.py
│   ├── main.py
│   ├── process.py
│   ├── tests.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── results.ipynb
```

---

## Notes

* The `data/` and `results/` folders are excluded from the repository as required
* `.env.example` is provided as a template for environment variables
* No API keys or sensitive data are included in this repository

---

## AI Usage

Some portions of this project were developed with the assistance of ChatGPT, particularly for:

* Debugging and refining data processing logic
* Structuring visualization functions
* Improving code organization and documentation

All AI-generated code sections have been clearly labeled with `# AI generated:` in the source files.

---

## Author

Na Ma
Communication Data Science, USC

