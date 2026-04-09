from src.load import load_insideairbnb
from src.process import clean_price
from src.analyze import plot_price_histogram

def main():
    df = load_insideairbnb()
    df = clean_price(df)
    plot_price_histogram(df)

if __name__ == "__main__":
    main()
