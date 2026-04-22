from src.load import load_airbnb_kaggle
from src.load import load_insideairbnb_la
from src.load import load_tourism

from src.process import clean_airbnb_kaggle
from src.process import clean_insideairbnb
from src.process import clean_tourism

from src.analyze import plot_price_histogram
from src.analyze import plot_room_type_price
from src.analyze import plot_minimum_nights_price
from src.analyze import plot_price_vs_reviews
from src.analyze import plot_reviews_by_room_type
from src.analyze import plot_tourism_total_trend
from src.analyze import plot_tourism_asia_vs_central_america

def main():
    airbnb_df = load_airbnb_kaggle()
    airbnb_df = clean_airbnb_kaggle(airbnb_df)

    inside_df = load_insideairbnb_la()
    inside_df = clean_insideairbnb(inside_df)

    tourism_df = load_tourism()
    tourism_df = clean_tourism(tourism_df)

    plot_price_histogram(airbnb_df)
    plot_room_type_price(airbnb_df)
    plot_minimum_nights_price(airbnb_df)
    plot_price_vs_reviews(airbnb_df)

    plot_reviews_by_room_type(inside_df)

    plot_tourism_total_trend(tourism_df)
    plot_tourism_asia_vs_central_america(tourism_df)

if __name__ == "__main__":
    main()
