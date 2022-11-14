# Write your solution here
import math

def get_station_data(filename: str):
    station_data = {}
    with open(filename) as new_file:
        for line in new_file:
            parts = line.strip().split(";")
            if parts[0] == "Longitude":
                continue
            station_data[parts[3]] = (float(parts[0]), float(parts[1]))

    return station_data

def distance(stations: dict, station1: str, station2: str):
    for station_name, coords in stations.items():
        if station_name == station1:
            (longitude1, latitude1) = coords
        if station_name == station2:
            (longitude2, latitude2) = coords

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    greatest = 0
    for station_name1 in stations:
        for station_name2 in stations:
            distance_km = distance(stations, station_name1, station_name2)
            if distance_km > greatest:
                greatest = distance_km
                station1 = station_name1
                station2 = station_name2

    return (station1, station2, greatest)
