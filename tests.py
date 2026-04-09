from src.data_collection import get_location_data

def test_api():
    data = get_location_data("Los Angeles")
    assert len(data) > 0

if __name__ == "__main__":
    test_api()
    print("API test passed")
