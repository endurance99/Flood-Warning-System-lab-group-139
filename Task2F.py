import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood, datafetcher
from floodsystem.plot import plot_water_level_with_fit

# Build station list and update water levels
stations = build_station_list()
update_water_levels(stations)

# Find the 5 stations with highest relative water levels
stations_highest = flood.stations_highest_rel_level(stations, 5)

# For each of the 5 stations, fetch data for the last 2 days and plot
dt = datetime.timedelta(days=2)

for station in stations_highest:
    try:
        # Fetch water level time history for the last 2 days
        dates, levels = datafetcher.fetch_measure_levels(station.measure_id, dt)
        
        if dates and levels:
            # Plot the data with a degree 4 polynomial fit
            plot_water_level_with_fit(station, dates, levels, 4)
    except Exception as e:
        print(f"Could not fetch data for {station.name}: {e}")
