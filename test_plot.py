# from floodsystem.analysis import *
# from floodsystem.plot import plot_water_levels
# from floodsystem.stationdata import build_station_list

# def test_plot_water_levels():
#     """Test for plot_water_levels function"""

#     # Build list of stations
#     stations = build_station_list()

#     # Find station 'Cam'
#     for station in stations:
#         if station.name == 'Cam':
#             station_cam = station
#             break

#     # Assert that station is found
#     assert station_cam

#     # Get water level data for the past 10 days
#     dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=10))

#     # Plot water levels
#     plot_water_levels(station_cam, dates, levels)

# def test_plot_water_levels_with_fit():
#     """Test for plot_water_levels_with_fit function"""

#     # Build list of stations
#     stations = build_station_list()

#     # Find station 'Cam'
#     for station in stations:
#         if station.name == 'Cam':
#             station_cam = station
#             break

#     # Assert that station is found
#     assert station_cam

#     # Get water level data for the past 10 days
#     dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=10))

#     # Plot water levels with a 4th degree polynomial fit
#     plot_water_levels_with_fit(station_cam, dates, levels, p=4)