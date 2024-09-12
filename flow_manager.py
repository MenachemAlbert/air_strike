from repository.json_repository import read_from_json, read_city_location
from service.mission_service import find_all_locations

targets = read_from_json("assents/targets.json")["targets"]

print(targets)

print(find_all_locations())

il_location = read_city_location('city_location.json', "Jerusalem")

print(il_location)