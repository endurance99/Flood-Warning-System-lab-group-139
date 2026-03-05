from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
import datetime


def run():
    """Plots water levels over the past 10 days for the 5 stations
    with the highest current relative water level."""
    
    stations = build_station_list()
    update_water_levels(stations)

    # Get a list of stations with valid, realistic relative water levels (filtering out extreme/unrealistic values)
    candidate_stations = stations_highest_rel_level(stations, 10)  # get more than 5 to allow for missing data

    plotted = 0
    for station in candidate_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=10))
        # Only plot if there is data
        if dates and levels and len(dates) > 0 and len(levels) > 0:
            plot_water_levels(station, dates, levels)
            plotted += 1
        if plotted == 5:
            break


if __name__ == "__main__":
    run()