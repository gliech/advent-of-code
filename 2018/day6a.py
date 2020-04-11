# Setup
from aocd import get_data
from operator import itemgetter
from itertools import groupby, product
from collections import defaultdict
data = { tuple(map(int,coord.split(', '))) for coord in get_data(year=2018, day=6).split('\n') }
# test data
# data = set([(1,2),(1,50),(40,2),(40,50),(19,20),(21,30),(3,26),(38,24),(19,4),(21,47)])

# Longform
def closest_point(coord):
    closest_points = min( { (distance, tuple(points)) for distance, points in groupby( sorted( (abs(centerpoint[0]-coord[0])+abs(centerpoint[1]-coord[1]),centerpoint) for centerpoint in data ),key=lambda x:x[0]) } )[1]
    return closest_points[0][1] if len(closest_points) == 1 else False

x_min = min(data)[0]
x_max = max(data)[0]
y_min = min(map(lambda x:x[1],data))
y_max = max(map(lambda x:x[1],data))

# a = { center_point: list(area) for center_point, area in groupby( sorted( (closest_point(coord),coord) for coord in product(range(x_min,x_max+1),range(y_min,y_max+1)) ),key=lambda x:x[0]) }
areas = defaultdict(list)
for coord in product(range(x_min,x_max+1),range(y_min,y_max+1)):
    area = closest_point(coord)
    if area:
        areas[area].append(coord)

def is_island(area):
    x_coords = {coord[0] for coord in area}
    y_coords = {coord[1] for coord in area}
    return ((x_min not in x_coords) and
            (x_max not in x_coords) and
            (y_min not in y_coords) and
            (y_max not in y_coords))


finite_areas = filter(is_island, areas.values())
biggest_area = max(map(len, finite_areas))
# Golfed

# Output
#print(areas[(40,50)], x_min, x_max, y_min, y_max, is_island(areas[(40,50)]))
print(biggest_area)
