from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station
from floodsystem.station import MonitoringStation


def test_stations_by_distance():
    """Test for stations_by_distance function"""
    # Create a small static list of stations
    stations = [
        MonitoringStation('id1', 'm1', 'Cam', (0.0, 0.0), None, 'River Cam', 'Town'),
        MonitoringStation('id2', 'm2', 'Thames1', (1.0, 1.0), None, 'River Thames', 'Town'),
        MonitoringStation('id3', 'm3', 'Thames2', (2.0, 2.0), None, 'River Thames', 'Town'),
        MonitoringStation('id4', 'm4', 'Thames3', (3.0, 3.0), None, 'River Thames', 'Town'),
        MonitoringStation('id5', 'm5', 'Avon1', (4.0, 4.0), None, 'River Avon', 'Town'),
        MonitoringStation('id6', 'm6', 'Avon2', (5.0, 5.0), None, 'River Avon', 'Town'),
    ]

    # Find station 'Cam'
    station_cam = next(s for s in stations if s.name == 'Cam')

    # Get list of stations by distance from 'Cam'
    distance_list = stations_by_distance(stations, station_cam.coord)

    # Assert that the closest station is 'Cam' itself
    assert distance_list[1][0].name == 'Cam'

def test_stations_by_river():
    """Test for stations_by_river function"""
    stations = [
        MonitoringStation('id1', 'm1', 'Cam', (0.0, 0.0), None, 'River Cam', 'Town'),
        MonitoringStation('id2', 'm2', 'Thames1', (1.0, 1.0), None, 'River Thames', 'Town'),
    ]

    # Get dictionary of stations by river
    river_dict = stations_by_river(stations)

    # Assert that 'River Cam' is a key in the dictionary
    assert 'River Cam' in river_dict

    # Assert that 'Cam' station is in the list of stations for 'River Cam'
    assert 'Cam' in river_dict['River Cam']

def test_rivers_with_station():
    """Test for rivers_with_station function"""
    stations = [
        MonitoringStation('id1', 'm1', 'Cam', (0.0, 0.0), None, 'River Cam', 'Town'),
        MonitoringStation('id2', 'm2', 'Thames1', (1.0, 1.0), None, 'River Thames', 'Town'),
    ]

    # Get set of rivers with a station
    river_set = rivers_with_station(stations)

    # Assert that 'River Cam' is in the set
    assert 'River Cam' in river_set

def test_rivers_by_station_number():
    """Test for rivers_by_station_number function"""
    stations = [
        MonitoringStation('id1', 'm1', 'Cam', (0.0, 0.0), None, 'River Cam', 'Town'),
        MonitoringStation('id2', 'm2', 'Thames1', (1.0, 1.0), None, 'River Thames', 'Town'),
        MonitoringStation('id3', 'm3', 'Thames2', (2.0, 2.0), None, 'River Thames', 'Town'),
        MonitoringStation('id4', 'm4', 'Thames3', (3.0, 3.0), None, 'River Thames', 'Town'),
        MonitoringStation('id5', 'm5', 'Avon1', (4.0, 4.0), None, 'River Avon', 'Town'),
        MonitoringStation('id6', 'm6', 'Avon2', (5.0, 5.0), None, 'River Avon', 'Town'),
    ]

    # Get list of rivers by station number (top 2)
    river_list = rivers_by_station_number(stations, 2)

    # Assert that the first river in the list is 'River Thames'
    assert river_list[0][0] == 'River Thames'

    # Assert that the second river in the list is 'River Avon'
    assert river_list[1][0] == 'River Avon'
