import datetime
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.station import MonitoringStation

def test_plot_water_levels():
    """Test for plot_water_levels function"""
    
    # Create a custom station
    station = MonitoringStation("test-id", "test-measure-id", "Test Station", 
                               (0.0, 0.0), (0.0, 1.0), "Test River", "Test Town")
    
    # Create sample dates and levels
    dates = [datetime.datetime(2024, 1, i) for i in range(1, 11)]
    levels = [0.1 * i for i in range(1, 11)]
    
    # Plot water levels (just test that it doesn't raise an error)
    plot_water_levels(station, dates, levels)
    plt.close()

def test_plot_water_levels_with_fit():
    """Test for plot_water_levels_with_fit function"""
    
    # Create a custom station
    station = MonitoringStation("test-id", "test-measure-id", "Test Station", 
                               (0.0, 0.0), (0.0, 1.0), "Test River", "Test Town")
    
    # Create sample dates and levels
    dates = [datetime.datetime(2024, 1, i) for i in range(1, 11)]
    levels = [0.1 * i for i in range(1, 11)]
    
    # Plot water levels with a 4th degree polynomial fit (just test that it doesn't raise an error)
    plot_water_level_with_fit(station, dates, levels, p=4)
    plt.close()