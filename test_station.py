# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    s1 = MonitoringStation("s1", "m1", "Station 1", (0, 0), (0.5, 1.0), "River A", "Town A")
    s2 = MonitoringStation("s2", "m2", "Station 2", (0, 0), (1.0, 0.5), "River B", "Town B")
    s3 = MonitoringStation("s3", "m3", "Station 3", (0, 0), None, "River C", "Town C")
    s4 = MonitoringStation("s4", "m4", "Station 4", (0, 0), (None, 1.0), "River D", "Town D")
    s5 = MonitoringStation("s5", "m5", "Station 5", (0, 0), (0.5, None), "River E", "Town E")

    stations = [s1, s2, s3, s4, s5]

    inconsistent_stations = inconsistent_typical_range_stations(stations)

    assert set(inconsistent_stations) == {s2, s3, s4, s5}