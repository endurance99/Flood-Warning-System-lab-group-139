# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides plotting functions for flood warning system data.

"""

import numpy as np
import matplotlib.pyplot as plt
from .analysis import polyfit


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level data and the best-fit polynomial for a station.

    Args:
        station: MonitoringStation object
        dates: List of datetime objects representing the dates of measurements
        levels: List of floats representing water level measurements
        p: Degree of the polynomial for the fit
    """
    # Compute the best-fit polynomial
    poly, d0 = polyfit(dates, levels, p)
    
    # Convert dates to numeric values for plotting
    x = np.array([(date - d0).total_seconds() / (24 * 3600) for date in dates])
    y = np.array(levels)
    
    # Generate smooth x values for the polynomial plot
    x_smooth = np.linspace(x.min(), x.max(), 300)
    y_smooth = poly(x_smooth)
    
    # Create the plot
    plt.figure()
    plt.plot(x, y, 'o', label='Water level data')
    plt.plot(x_smooth, y_smooth, '-', label=f'Polynomial fit (degree {p})')
    
    # Add typical range if available
    if station.typical_range is not None:
        low, high = station.typical_range
        x_range = [x.min(), x.max()]
        plt.axhline(y=low, color='g', linestyle='--', label='Typical range (low)')
        plt.axhline(y=high, color='r', linestyle='--', label='Typical range (high)')
    
    plt.xlabel('Days since {}'.format(d0.strftime('%Y-%m-%d')))
    plt.ylabel('Water level (m)')
    plt.title(f'Water Level at {station.name}')
    plt.legend()
    plt.grid(True)
    plt.show()
