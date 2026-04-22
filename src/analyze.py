import matplotlib.pyplot as plt
from src.config import RESULTS_FOLDER

def plot_price_histogram(df):
    plt.figure()
    df["price"].hist()
    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.savefig(RESULTS_FOLDER + "price_histogram.png")
    plt.close()

def average_price_by_room_type(df):
    result = df.groupby("room_type")["price"].mean()
    return result

def price_vs_accommodates(df):
    return df[["accommodates", "price"]]
