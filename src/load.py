import pandas as pd
from src.config import DATA_FILE_1

def load_insideairbnb():
    df = pd.read_csv(DATA_FILE_1, low_memory=False)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    print(df.columns)
    return df
