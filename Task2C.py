from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import stationdata, geo, station, flood

stations = build_station_list()
update_water_levels(stations)

stations_highest = flood.stations_highest_rel_level(stations, 10)

for s in stations_highest:
    print(f"{s.name}: {s.relative_water_level()}")