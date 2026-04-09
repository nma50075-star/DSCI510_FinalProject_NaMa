import requests

def get_location_data(city):
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": city,
        "format": "json"
    }

    headers = {
        "User-Agent": "DSCI510 final project"
    }

    response = requests.get(url, params=params, headers=headers)

    data = response.json()

    return data

if __name__ == "__main__":
    result = get_location_data("Los Angeles")
    print(result)
