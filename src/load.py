import pandas as pd
from src.config import AIRBNB_KAGGLE_FILE
from src.config import INSIDEAIRBNB_LA_FILE
from src.config import TOURISM_FILE

def load_airbnb_kaggle():
    df = pd.read_csv(AIRBNB_KAGGLE_FILE, low_memory=False)
    return df

def load_insideairbnb_la():
    df = pd.read_csv(INSIDEAIRBNB_LA_FILE, encoding="latin1", low_memory=False)
    return df

def load_tourism():
    df = pd.read_csv(TOURISM_FILE, low_memory=False)
    return df
