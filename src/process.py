def clean_price(df):
    df = df.copy()
    df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)
    return df
