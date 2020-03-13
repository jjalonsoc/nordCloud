import pytest
from pytest import mark 
from app.link_stations_optimizer import LinkStation, most_suitable_link_station

@pytest.fixture
def link_station():
    '''Returns a link station object at x, y, r = 0, 0, 5'''
    return LinkStation(0, 0, 5)


@pytest.mark.parametrize("x, y, distance_expected", [
    (0, 0, 0.0),
    (3, 4, 5.0),
    (6, 8, 10.0)
])
def test_calculate_distance(link_station, x, y, distance_expected):
    assert link_station.calculate_distance(x, y) == distance_expected


@pytest.mark.parametrize("distance, power_expected", [
    (3, 4.0),
    (5, 0.0),
    (6, 0.0)
])
def test_calculate_power(link_station, distance, power_expected):
    assert link_station.calculate_power(distance) == power_expected


@pytest.mark.parametrize("point, string_expected", [
    ((0, 0) , 'Best link station for point (0,0) is (0,0) with power 100.00'),
    ((100, 100), 'No link station within reach for point (100,100)'),
    ((15, 10), 'Best link station for point (15,10) is (10,0) with power 0.67'),
    ((18, 18), 'Best link station for point (18,18) is (20,20) with power 4.72')
])
def test_most_suitable_link_station(point, string_expected):
    stations_list = [(0, 0, 10), (20, 20, 5), (10, 0, 12)]
    assert most_suitable_link_station(point, stations_list) == string_expected

