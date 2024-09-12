import os.path

from api.api_requstes import get_api
from repository.json_repository import write_api_to_json

cities = [
    "Damascus", "Beirut", "Amman", "Cairo", "Baghdad", "Tehran", "Riyadh",
    "Tripoli", "Ankara", "Khartoum", "Gaza Strip", "Sanaa", "Manama",
    "Kuwait City", "Doha", "Jerusalem"
]
api_key = "e5ce7138efa2964869aaf6d2072382fa"
url_location = "https://api.openweathermap.org/geo/1.0/direct"
url_data = "https://api.openweathermap.org/data/2.5/forecast"

if __name__ == "__main__":
    exist_data = os.path.isfile("city_data.json")
    if exist_data:
        print("city_data is exists")
    else:
        city_data = get_api(url_data , cities , api_key)
        write_api_to_json(city_data , "city_data.json")

    exist_location = os.path.isfile("city_location.json")
    if exist_location:
        print("city_location is exists")
    else:
        city_data = get_api(url_location, cities, api_key)
        write_api_to_json(city_data, "city_location.json")