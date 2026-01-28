from floodsystem import stationdata, geo

# Build a list of all stations
stations = stationdata.build_station_list()

# Find stations within 10 km of Cambridge city centre
cambridge_centre = (52.2053, 0.1218)
nearby_stations = geo.stations_within_radius(stations=stations, centre=cambridge_centre, r=10)

# Extract station names and sort alphabetically
station_names = sorted([station.name for station in nearby_stations])

# Print the names
print(station_names)
