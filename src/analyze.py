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
