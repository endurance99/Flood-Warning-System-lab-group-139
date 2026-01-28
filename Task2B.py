from floodsystem.stationdata import build_station_list
from floodsystem import stationdata, geo, station, flood


def run():

    stations = build_station_list()

    over_threshold_stations = flood.stations_level_over_threshold(stations, 0.8)

    for statioon, level in over_threshold_stations:
        print(f"{statioon.name}: {level:.2f}")

run()