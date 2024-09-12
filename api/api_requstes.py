from functools import partial

import requests
import json

from toolz import get_in, pipe

from repository.json_repository import read_from_json

cities = [
    "Damascus", "Beirut", "Amman", "Cairo", "Baghdad", "Tehran", "Riyadh",
    "Tripoli", "Ankara", "Khartoum", "Gaza Strip", "Sanaa", "Manama",
    "Kuwait City", "Doha", "Jerusalem"
]
api_key = "e5ce7138efa2964869aaf6d2072382fa"
url_location = "https://api.openweathermap.org/geo/1.0/direct"
url_data = "https://api.openweathermap.org/data/2.5/forecast"

def get_api(url, cities, api_key):
    results = {}
    def fetch_city_data(city):
        try:
            city_url = f"{url}?q={city}&limit=2&appid={api_key}"
            response = requests.get(city_url)
            city_data = response.json()
            results[city] = city_data

        except Exception as e:
            print(f"{e} in {city}")

    list(map(fetch_city_data, cities))
    return results


def find_weather_by_city(path, city) -> dict:
    date_filter = "2024-09-12 15:00:00"
    data = read_from_json(path)
    data = data[city]
    if not data or 'list' not in data:
        return None

    weather_entry = next(
        (item for item in data['list'] if item['dt_txt'] == date_filter),
        None
    )

    if not weather_entry:
        return {
            'city': city,
            'weather': 'לא נמצא',
            'clouds': 0,
            'wind': 'לא נמצא'
        }

    return {
        'city': city,
        'weather': get_in(['weather', 0, 'main'], weather_entry, default='לא נמצא'),
        'clouds': get_in(['clouds', 'all'], weather_entry, default=0),
        'wind': get_in(['wind', 'speed'], weather_entry, default='לא נמצא')
    }





