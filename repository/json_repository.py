import json
from typing import List
from  toolz import get_in


def write_api_to_json(list: dict, filename: str):
    with open(filename, 'w') as jsonfile:
        json.dump(list, jsonfile, indent=4)

def read_from_json(filename: str) :
    with open(filename, 'r') as jsonfile:
        return json.load(jsonfile)


def read_city_location(filename: str , city :str):
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
        city_lat = get_in([city , 0,'lat'],data)
        city_lon = get_in([city , 0,'lon'],data)
        return {city:(city_lat, city_lon)}
