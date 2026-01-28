# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
from .station import MonitoringStation

# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

def stations_by_distance(stations, p):

    stations_dist = []

    for station in stations:
        distance = haversine(station.coord, p)
        stations_dist.append((station.name, distance))

    return sorted_by_key(stations_dist, 1)

def stations_within_radius(stations, centre, r):
    """Returns a list of stations within radius r of a centre point.

    Args:
        stations: List of MonitoringStation objects
        centre: Tuple of (latitude, longitude) of the centre point
        r: Radius in km

    Returns:
        List of MonitoringStation objects within radius r of centre
    """

    stations_in_radius = []

    for station in stations:
        station_location = (station.coord[0], station.coord[1])
        distance = haversine(centre, station_location)
        if distance <= r:
            stations_in_radius.append(station)

    return stations_in_radius
