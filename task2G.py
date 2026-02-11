from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood

# Build station list and update water levels
stations = build_station_list()
update_water_levels(stations)

# Assess flood risk by town based on stations with high relative water levels
# We use a threshold of 1.0 (100% of typical range) as concerning
concerning_stations = flood.stations_level_over_threshold(stations, 0.5)

# Group stations by town and assess risk
town_risk = {}

for station, rel_level in concerning_stations:
    # Only consider stations with town information
    if station.town is None:
        continue
    
    town = station.town
    if town not in town_risk:
        town_risk[town] = []
    
    town_risk[town].append((station, rel_level))

# Assess risk level for each town
town_assessment = []

for town, station_data in town_risk.items():
    # Count stations and find max relative level
    num_stations = len(station_data)
    max_rel_level = max([level for _, level in station_data])
    
    # Risk assessment criteria:
    # - Severe: max relative level > 2.0 (water level 200% of typical range)
    # - High: max relative level > 1.5 (water level 150% of typical range) OR multiple stations
    # - Moderate: max relative level > 1.0 (water level 100% of typical range)
    # - Low: max relative level <= 1.0
    
    if max_rel_level > 2.0:
        risk_level = "SEVERE"
    elif max_rel_level > 1.5 or num_stations >= 2:
        risk_level = "HIGH"
    elif max_rel_level > 1.0:
        risk_level = "MODERATE"
    else:
        risk_level = "LOW"
    
    town_assessment.append((town, risk_level, max_rel_level, num_stations))

# Sort by risk level (custom sort order) and then by max relative level
risk_order = {"SEVERE": 0, "HIGH": 1, "MODERATE": 2, "LOW": 3}
town_assessment.sort(key=lambda x: (risk_order[x[1]], -x[2]))

# Print results
print("FLOOD RISK ASSESSMENT BY TOWN")
print("=" * 70)
print("\nAssessment Criteria:")
print("- SEVERE: Maximum relative water level > 2.0 (200% of typical range)")
print("- HIGH: Maximum relative level > 1.5 OR multiple stations at risk")
print("- MODERATE: Maximum relative level > 1.0 (100% of typical range)")
print("- LOW: Maximum relative level <= 1.0")
print("\n" + "=" * 70)

for town, risk_level, max_rel_level, num_stations in town_assessment:
    print(f"\n{town}: {risk_level}")
    print(f"  Stations at risk: {num_stations}")
    print(f"  Maximum relative water level: {max_rel_level:.2f}")
