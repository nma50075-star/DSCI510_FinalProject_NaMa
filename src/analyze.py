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

def plot_room_type_price(df):
    avg_price = df.groupby("room_type")["price"].mean()

    plt.figure()
    avg_price.plot(kind="bar")

    plt.title("Average Price by Room Type")
    plt.xlabel("Room Type")
    plt.ylabel("Average Price")

    plt.savefig(RESULTS_FOLDER + "room_type_price.png")
    plt.close()

def plot_accommodates_price(df):
    plt.figure()

    plt.scatter(df["accommodates"], df["price"])

    plt.title("Price vs Accommodates")
    plt.xlabel("Accommodates")
    plt.ylabel("Price")

    plt.savefig(RESULTS_FOLDER + "accommodates_price.png")
    plt.close()
