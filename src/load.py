import pandas as pd
from src.config import DATA_FILE_1

def load_insideairbnb():
    df = pd.read_csv(DATA_FILE_1)
    return df
