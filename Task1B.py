from floodsystem.stationdata import build_station_list
from floodsystem import stationdata, geo



def run():

    stations = build_station_list()

    cambridge_centre = (52.2053, 0.1218)

    stations_dist = geo.stations_by_distance(stations, cambridge_centre)

    print(stations_dist[0:9])

    # print("10 closest stations from Cambridge city centre:")
    # for station, distance in stations_dist[:10]:
    #     print((stations.name, stations.town, distance))ss

    # print("10 furthest stations from Cambridge city centre:")
    # for station, distance in stations_dist[-10:]:
    #     print((stations.name, stations.town, distance))


run()
