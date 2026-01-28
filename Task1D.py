from floodsystem import stationdata, geo

# Build a list of all stations
stations = stationdata.build_station_list()

river_stations = sorted(geo.rivers_with_station(stations))

print(f"{len(river_stations)} stations. First 10 - {list(river_stations)[:10]}")

station_on_river = geo.stations_by_river(stations)

print(sorted(station_on_river['River Aire']))
print(sorted(station_on_river['River Cam']))
print(sorted(station_on_river['River Thames']))