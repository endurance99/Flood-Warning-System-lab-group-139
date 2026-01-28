from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def run():
    """Plots water levels over the past 10 days for the 5 stations
    with the highest current relative water level."""
    
    stations = build_station_list()
    update_water_levels(stations)
    
    # Sort stations by relative water level (descending)
    stations_sorted = sorted(stations, key=lambda s: s.relative_water_level() or 0, reverse=True)
    
    # Get top 5 stations
    top5_stations = stations_sorted[:5]
    
    # Plot water levels for each of the top 5 stations
    for station in top5_stations:
        # Fetch dates and levels from datafetcher
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
        # Plot water levels
        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    run()