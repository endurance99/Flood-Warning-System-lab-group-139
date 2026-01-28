import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from .station import MonitoringStation


def polyfit(dates, levels, p):
    """Computes a least-squares fit of a polynomial of degree p to water
    level data.

    Args:
        dates: List of datetime objects representing the dates of measurements
        levels: List of floats representing water level measurements
        p: Degree of the polynomial

    Returns:
        Tuple of (poly, d0) where:
            poly: numpy.poly1d object representing the fitted polynomial
            d0: Shift of the time (date) axis used for numerical stability
    """
    # Convert dates to numeric values (days since first date)
    # This improves numerical stability of the polynomial fit
    d0 = dates[0]
    x = np.array([(date - d0).total_seconds() / (24 * 3600) for date in dates])
    y = np.array(levels)
    
    # Compute least-squares polynomial fit
    coefficients = np.polyfit(x, y, p)
    poly = np.poly1d(coefficients)
    
    return poly, d0
