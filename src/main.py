from src.load import load_insideairbnb
from src.process import clean_price
from src.analyze import plot_price_histogram
from src.analyze import plot_room_type_price
from src.analyze import plot_minimum_nights_price

def main():
    df = load_insideairbnb()
    df = clean_price(df)

    plot_price_histogram(df)
    plot_room_type_price(df)
    plot_minimum_nights_price(df)

if __name__ == "__main__":
    main()
