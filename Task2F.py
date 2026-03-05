import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood, datafetcher
from floodsystem.plot import plot_water_level_with_fit

# Build station list and update water levels
stations = build_station_list()
update_water_levels(stations)

# Find more than 5 stations with highest relative water levels to allow for missing data
candidate_stations = flood.stations_highest_rel_level(stations, 10)

# For each of the candidate stations, fetch data for the last 2 days and plot up to 5 valid graphs
dt = datetime.timedelta(days=2)
plotted = 0
for station in candidate_stations:
    try:
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id, dt)
        if dates and levels and len(dates) > 0 and len(levels) > 0:
            plot_water_level_with_fit(station, dates, levels, 4)
            plotted += 1
        if plotted == 5:
            break
    except Exception as e:
        print(f"Could not fetch data for {station.name}: {e}")
