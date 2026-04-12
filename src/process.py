import pandas as pd

def clean_price(df):
    df = df.copy()
    df["price"] = df["price"].replace("[$,]", "", regex=True)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])
    return df
