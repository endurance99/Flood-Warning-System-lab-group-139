from floodsystem.stationdata import build_station_list
from floodsystem import stationdata, geo, station

def run():

    stations = build_station_list()

    inconsistent_stations = station.inconsistent_typical_range_stations(stations)

    inconsistent_stations_sorted = sorted(inconsistent_stations, key=lambda x: x.name)

    for statioon in inconsistent_stations_sorted:
        print(statioon.name)

run()