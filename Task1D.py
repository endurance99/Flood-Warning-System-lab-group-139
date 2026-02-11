from floodsystem import stationdata, geo

# Build a list of all stations
stations = stationdata.build_station_list()

river = sorted(geo.rivers_with_station(stations))

print(f"{len(river)} stations. First 10 - {list(river)[0:9]}")

station_on_river = geo.stations_by_river(stations)

print(sorted(station_on_river['River Aire']))
print(sorted(station_on_river['River Cam']))
print(sorted(station_on_river['River Thames']))