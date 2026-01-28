from floodsystem.stationdata import build_station_list
from floodsystem import stationdata, geo

def run():

    stations = build_station_list()

    rivers_with_most_stations = geo.rivers_by_station_number(stations, 9)

    print(rivers_with_most_stations)

run()