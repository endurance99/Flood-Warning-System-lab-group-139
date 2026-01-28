from .utils import sorted_by_key  # noqa
from haversine import haversine
from .station import MonitoringStation

def stations_level_over_threshold(stations, tolerance):
    """Returns a list of tuples of stations and their relative water levels
    that are over a given tolerance.

    Args:
        stations: List of MonitoringStation objects
        tolerance: Relative water level threshold

    Returns:
        List of tuples of (MonitoringStation, relative water level) where the
        relative water level is over the given tolerance
    """

    stations_over_threshold = []

    for station in stations:
        rel_level = station.relative_water_level()
        if rel_level is not None and rel_level > tolerance:
            stations_over_threshold.append((station, rel_level))

    return sorted_by_key(stations_over_threshold, 1, reverse=True)