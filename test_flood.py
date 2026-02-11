# from floodsystem.flood import stations_level_over_threshold
# from floodsystem.flood import stations_highest_rel_level
# from floodsystem.station import MonitoringStation


# def test_stations_level_over_threshold():
#     """Test for stations_level_over_threshold function"""

#     # Create static stations with set latest levels and typical ranges
#     s1 = MonitoringStation('id1', 'm1', 'S1', (0, 0), (0.0, 10.0), 'River A', 'Town')
#     s1.latest_level = 9.5  # rel = 0.95
#     s2 = MonitoringStation('id2', 'm2', 'S2', (0, 0), (0.0, 10.0), 'River B', 'Town')
#     s2.latest_level = 8.5  # rel = 0.85
#     s3 = MonitoringStation('id3', 'm3', 'S3', (0, 0), (0.0, 10.0), 'River C', 'Town')
#     s3.latest_level = 7.0  # rel = 0.7
#     s4 = MonitoringStation('id4', 'm4', 'S4', (0, 0), (0.0, 10.0), 'River D', 'Town')
#     s4.latest_level = None
#     s5 = MonitoringStation('id5', 'm5', 'S5', (0, 0), None, 'River E', 'Town')

#     stations = [s1, s2, s3, s4, s5]

#     # Get list of stations over threshold of 0.8
#     over_threshold = stations_level_over_threshold(stations, 0.8)

#     # Assert that all stations in the list have relative water level over 0.8
#     assert all(rel_level > 0.8 for _, rel_level in over_threshold)

# def test_stations_highest_rel_level():
#     """Test for stations_highest_rel_level function"""

#     # Create static stations with known relative levels
#     a = MonitoringStation('a', 'ma', 'A', (0, 0), (0.0, 10.0), 'River X', 'Town')
#     a.latest_level = 9.0  # rel 0.9
#     b = MonitoringStation('b', 'mb', 'B', (0, 0), (0.0, 10.0), 'River Y', 'Town')
#     b.latest_level = 8.5  # rel 0.85
#     c = MonitoringStation('c', 'mc', 'C', (0, 0), (0.0, 10.0), 'River Z', 'Town')
#     c.latest_level = 8.0  # rel 0.8
#     d = MonitoringStation('d', 'md', 'D', (0, 0), (0.0, 10.0), 'River W', 'Town')
#     d.latest_level = 7.5  # rel 0.75
#     e = MonitoringStation('e', 'me', 'E', (0, 0), (0.0, 10.0), 'River V', 'Town')
#     e.latest_level = 7.0  # rel 0.7

#     stations = [a, b, c, d, e]

#     # Get list of top 3 stations with highest relative water levels
#     highest_rel_levels = stations_highest_rel_level(stations, 3)

#     # Assert that the list has at least 3 stations
#     assert len(highest_rel_levels) >= 3

#     # Get the relative water levels of the returned stations
#     rel_levels = [station.relative_water_level() for station in highest_rel_levels]

#     # Assert that the relative water levels are in descending order
#     assert all(rel_levels[i] >= rel_levels[i+1] for i in range(len(rel_levels)-1))
