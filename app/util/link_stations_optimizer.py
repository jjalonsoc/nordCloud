import math

class LinkStation:
    """
    A station ubicated in the grid that can be linked to a given point. 
    Arguments
    ---------
    fields : list of 3-tuple (x, y, reach)
        x : x coordinate in a 2 dimensiaonal grid.
        y : y coordinate in a 2 dimensiaonal grid.
        reach : integer value representing how far the link station can reach

    """
    def __init__(self, x, y, reach):
        self.x = x
        self.y = y
        self.reach = reach

    def calculate_power(self, distance):
        """Evaluates the power according to the formula given.
            * If the reach of the station is shorter than the distance between
            the link station and the point a power of 0 is returned.
        Inputs
        --------
        distance: distance between link station and point considered.
        Output
        --------
        power: calculated from formula given in the task
        """
        if distance > self.reach:
            return 0
        else:
            return (self.reach - distance) ** 2

    def calculate_distance(self, x, y):
        """Evaluates the distance between a given point and the location of the link station.
        Pitagoras is used to calculate the distance.
        Inputs
        --------
        x : x coordinate in a 2 dimensiaonal grid of the considered point.
        y : y coordinate in a 2 dimensiaonal grid of the considered point.
        Output
        --------
        distance: calculate using pitagoras
        """
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)



def most_suitable_link_station(point, stations_list):
    """Evaluates which station is most suitable filtered by power.
        * Creates list of station objects.
        * Calculates powers for each station and the given point.
        Inputs
        --------
        point: a tuple (x,y) representing grid coordinates of the point of interest.
        stations_list: list of stations.
        station: list [x,y,r], xy, location of the station in the grid, and r the reach of the station.
        Output
        --------
        string: Information of which station presents the highest power.
    """
    link_stations = [LinkStation(*l) for l in stations_list]
    powers = [station.calculate_power(station.calculate_distance(*point)) for station in link_stations]
    max_power = max(powers)
    if max_power == 0:
        return 'No link station within reach for point ({},{})'.format(point[0], point[1])
    else:
        station_max_power = link_stations[powers.index(max_power)]
        return 'Best link station for point ({},{}) is ({},{}) with power {:.2f}'.format(point[0], point[1],
        station_max_power.x, station_max_power.y, max_power)


if __name__ == '__main__':
    links = [[0, 0, 10], [20, 20, 5], [10, 0, 12]]
    points = [(0,0), (100, 100), (15, 10), (18, 18)]
    for point in points:
        print(most_suitable_link_station(point, links))
