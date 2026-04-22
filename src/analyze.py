import os
import matplotlib.pyplot as plt
from src.config import RESULTS_FOLDER
from src.config import PRICE_COL
from src.config import ROOM_TYPE_COL
from src.config import MINIMUM_NIGHTS_COL
from src.config import NUMBER_OF_REVIEWS_COL
from src.config import TOURISM_TIME_COL
from src.config import TOURISM_TOTAL_COL
from src.config import TOURISM_ASIA_COL
from src.config import TOURISM_CENTRAL_AMERICA_COL

def make_results_folder():
    if not os.path.exists(RESULTS_FOLDER):
        os.makedirs(RESULTS_FOLDER)

def plot_price_histogram(df):
    make_results_folder()
    plt.figure()
    df[PRICE_COL].hist()
    plt.title("Distribution of Airbnb Prices")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(RESULTS_FOLDER + "price_histogram.png")
    plt.close()

def plot_room_type_price(df):
    make_results_folder()
    avg_price = df.groupby(ROOM_TYPE_COL)[PRICE_COL].mean()

    plt.figure()
    avg_price.plot(kind="bar")
    plt.title("Average Airbnb Price by Room Type")
    plt.xlabel("Room Type")
    plt.ylabel("Average Price")
    plt.tight_layout()
    plt.savefig(RESULTS_FOLDER + "room_type_price.png")
    plt.close()

def plot_minimum_nights_price(df):
    make_results_folder()
    plt.figure()
    plt.scatter(df[MINIMUM_NIGHTS_COL], df[PRICE_COL])
    plt.title("Price vs Minimum Nights")
    plt.xlabel("Minimum Nights")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig(RESULTS_FOLDER + "minimum_nights_price.png")
    plt.close()

def plot_price_vs_reviews(df):
    make_results_folder()
    plt.figure()
    plt.scatter(df[NUMBER_OF_REVIEWS_COL], df[PRICE_COL])
    plt.title("Price vs Number of Reviews")
    plt.xlabel("Number of Reviews")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig(RESULTS_FOLDER + "price_vs_reviews.png")
    plt.close()

def plot_reviews_by_room_type(df):
    make_results_folder()
    avg_reviews = df.groupby(ROOM_TYPE_COL)[NUMBER_OF_REVIEWS_COL].mean()

    plt.figure()
    avg_reviews.plot(kind="bar")
    plt.title("Average Number of Reviews by Room Type")
    plt.xlabel("Room Type")
    plt.ylabel("Average Number of Reviews")
    plt.tight_layout()
    plt.savefig(RESULTS_FOLDER + "reviews_by_room_type.png")
    plt.close()

def plot_tourism_total_trend(df):
    make_results_folder()
    plt.figure()
    plt.plot(df[TOURISM_TIME_COL], df[TOURISM_TOTAL_COL])
    plt.title("Total International Visitors Over Time")
    plt.xlabel("Time")
    plt.ylabel("Visitors")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(RESULTS_FOLDER + "tourism_total_trend.png")
    plt.close()

def plot_tourism_asia_vs_central_america(df):
    make_results_folder()
    plt.figure()
    plt.plot(df[TOURISM_TIME_COL], df[TOURISM_ASIA_COL], label="Asia")
    plt.plot(df[TOURISM_TIME_COL], df[TOURISM_CENTRAL_AMERICA_COL], label="Central America")
    plt.title("Visitors from Asia vs Central America Over Time")
    plt.xlabel("Time")
    plt.ylabel("Visitors")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(RESULTS_FOLDER + "tourism_asia_vs_central_america.png")
    plt.close()
