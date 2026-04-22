import pandas as pd
from src.process import clean_price
from src.process import clean_tourism

def test_clean_price():
    df = pd.DataFrame({"price": ["$100", "$2,500", "$80"]})
    cleaned_df = clean_price(df)
    assert cleaned_df["price"].tolist() == [100, 2500, 80]

def test_clean_tourism():
    df = pd.DataFrame({
        "time": ["2000-01", "2000-02"],
        "total": ["2,866,229", "2,948,121"],
        "asia": ["532,666", "570,342"],
        "central_america": ["64,922", "55,336"]
})

    cleaned_df = clean_tourism(df)
    assert cleaned_df["total"].tolist() == [2866229, 2948121]
    assert cleaned_df["asia"].tolist() == [532666, 570342]
    assert cleaned_df["central_america"].tolist() == [64922, 55336]

if __name__ == "__main__":
    test_clean_price()
    test_clean_tourism()
    print("All tests passed.")
