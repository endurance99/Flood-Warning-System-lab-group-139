# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the flood module"""

from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation


def test_stations_level_over_threshold():
    """Test for stations_level_over_threshold function"""
    # Create a small static list of stations with different relative water levels
    s1 = MonitoringStation("s1", "m1", "Station 1", (0, 0), (0.0, 1.0), "River A", "Town A")
    s1.latest_level = 0.8  # rel_level = 0.8

    s2 = MonitoringStation("s2", "m2", "Station 2", (0, 0), (0.0, 2.0), "River B", "Town B")
    s2.latest_level = 1.5  # rel_level = 0.75

    s3 = MonitoringStation("s3", "m3", "Station 3", (0, 0), (0.0, 1.0), "River C", "Town C")
    s3.latest_level = 1.2  # rel_level = 1.2

    s4 = MonitoringStation("s4", "m4", "Station 4", (0, 0), (0.0, 1.0), "River D", "Town D")
    s4.latest_level = None  # rel_level = None

    s5 = MonitoringStation("s5", "m5", "Station 5", (0, 0), None, "River E", "Town E")  # inconsistent range
    s5.latest_level = 0.5  # rel_level = None

    stations = [s1, s2, s3, s4, s5]

    # Test with tolerance 0.9
    result = stations_level_over_threshold(stations, 0.9)

    # Should return s3 with rel_level 1.2
    assert len(result) == 1
    assert result[0][0] == s3
    assert result[0][1] == 1.2


def test_stations_highest_rel_level():
    """Test for stations_highest_rel_level function"""
    # Create a small static list of stations with different relative water levels
    s1 = MonitoringStation("s1", "m1", "Station 1", (0, 0), (0.0, 1.0), "River A", "Town A")
    s1.latest_level = 0.8  # rel_level = 0.8

    s2 = MonitoringStation("s2", "m2", "Station 2", (0, 0), (0.0, 2.0), "River B", "Town B")
    s2.latest_level = 1.5  # rel_level = 0.75

    s3 = MonitoringStation("s3", "m3", "Station 3", (0, 0), (0.0, 1.0), "River C", "Town C")
    s3.latest_level = 1.2  # rel_level = 1.2

    s4 = MonitoringStation("s4", "m4", "Station 4", (0, 0), (0.0, 1.0), "River D", "Town D")
    s4.latest_level = None  # rel_level = None

    s5 = MonitoringStation("s5", "m5", "Station 5", (0, 0), None, "River E", "Town E")  # inconsistent range
    s5.latest_level = 0.5  # rel_level = None

    stations = [s1, s2, s3, s4, s5]

    # Test getting top 2 stations
    result = stations_highest_rel_level(stations, 2)

    # Should return s3 (1.2) and s1 (0.8)
    assert len(result) == 2
    assert result[0] == s3
    assert result[1] == s1
