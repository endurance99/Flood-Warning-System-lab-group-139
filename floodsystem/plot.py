from .station import MonitoringStation
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    """Plots the water levels for a given station over time.

    Args:
        station: MonitoringStation object
        dates: List of datetime objects
        levels: List of water level measurements
    """
    # Plot water level data
    plt.figure()
    plt.plot(dates, levels, label='Water level')

    # Add lines for typical low and high levels
    if station.typical_range_consistent():
        low, high = station.typical_range
        plt.axhline(y=low, color='g', linestyle='--', label='Typical low level')
        plt.axhline(y=high, color='r', linestyle='--', label='Typical high level')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()