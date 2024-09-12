from toolz import pipe, partial, compose, curry, first

from repository.json_repository import read_from_json, read_city_location


def find_all_locations():
    locations = pipe(
        read_from_json('../assents/targets.json'),
        lambda li: list(map(lambda c: c["city"], li["targets"])),
        lambda li: list(map(lambda c: read_city_location('../city_location.json', c), li))
    )
    return locations


import math


# Function to calculate the distance between two coordinates using the Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0  # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance


def find_all_distance():
    jerusalem_location = read_city_location('../city_location.json', "Jerusalem")
    (lat, lon) = jerusalem_location["Jerusalem"]
    city_locations = find_all_locations()

    def calculate_distance(target):
        city_name = target["city"]
        return  pipe(
            city_locations ,
            lambda li: filter(lambda u: city_name in u, li) ,
            partial(map, lambda u: first(list(u.values() ))),
            partial(map, lambda x: haversine_distance(lat, lon, x[0], x[1])),
            list
        )
    distances = pipe(
        read_from_json('../assents/targets.json'),
        lambda data: list(map(calculate_distance, data["targets"])),

    )
    return distances


def calculate_distance_score(distance, max_distance):
    return max(0, 100 - (distance / max_distance * 100))

def calculate_time_score(time_to_execute):
    return max(0, 100 - time_to_execute / 24 * 100)

def weather_score(weather):
    if weather['condition'] == "Clear":
        return 1.0  # Best condition
    elif weather['condition'] == "Clouds":
        return 0.7  # Clouds are moderate
    elif weather['condition'] == "Rain":
        return 0.4  # Rainy weather
    elif weather['condition'] == "Stormy":
        return 0.2  # Stormy weather is least favorable
    else:
        return 0  # Unfavorable condition
