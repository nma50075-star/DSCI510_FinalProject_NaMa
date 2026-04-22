import pandas as pd
from src.config import PRICE_COL
from src.config import NUMBER_OF_REVIEWS_COL
from src.config import MINIMUM_NIGHTS_COL
from src.config import TOURISM_TIME_COL
from src.config import TOURISM_TOTAL_COL
from src.config import TOURISM_ASIA_COL
from src.config import TOURISM_CENTRAL_AMERICA_COL

def clean_price(df):
    df = df.copy()
    df[PRICE_COL] = df[PRICE_COL].astype(str)
    df[PRICE_COL] = df[PRICE_COL].str.replace("$", "", regex=False)
    df[PRICE_COL] = df[PRICE_COL].str.replace(",", "", regex=False)
    df[PRICE_COL] = pd.to_numeric(df[PRICE_COL], errors="coerce")
    df = df.dropna(subset=[PRICE_COL])
    return df

def clean_numeric_column(df, column_name):
    df = df.copy()
    df[column_name] = df[column_name].astype(str)
    df[column_name] = df[column_name].str.replace(",", "", regex=False)
    df[column_name] = pd.to_numeric(df[column_name], errors="coerce")
    return df

def clean_airbnb_kaggle(df):
    df = df.copy()
    df = clean_price(df)

    if MINIMUM_NIGHTS_COL in df.columns:
        df = clean_numeric_column(df, MINIMUM_NIGHTS_COL)

    if NUMBER_OF_REVIEWS_COL in df.columns:
        df = clean_numeric_column(df, NUMBER_OF_REVIEWS_COL)

    df = df.dropna(subset=[MINIMUM_NIGHTS_COL])
    return df

def clean_insideairbnb(df):
    df = df.copy()

    if NUMBER_OF_REVIEWS_COL in df.columns:
        df = clean_numeric_column(df, NUMBER_OF_REVIEWS_COL)

    df = df.dropna(subset=[ROOM_TYPE_COL, NUMBER_OF_REVIEWS_COL])
    return df

def clean_tourism(df):
    df = df.copy()
    df[TOURISM_TIME_COL] = pd.to_datetime(df[TOURISM_TIME_COL], errors="coerce")

    df = clean_numeric_column(df, TOURISM_TOTAL_COL)
    df = clean_numeric_column(df, TOURISM_ASIA_COL)
    df = clean_numeric_column(df, TOURISM_CENTRAL_AMERICA_COL)

    df = df.dropna(subset=[TOURISM_TIME_COL, TOURISM_TOTAL_COL, TOURISM_ASIA_COL, TOURISM_CENTRAL_AMERICA_COL])
    return df
