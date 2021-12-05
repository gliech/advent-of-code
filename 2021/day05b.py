from aocd import get_data
from itertools import cycle, starmap
from collections import Counter
from functools import reduce
from operator import methodcaller

data = get_data(year=2021, day=5).split('\n')
data = {tuple(tuple(map(int, coord.split(','))) for coord in line.split(' -> ')) for line in data}

def coord_range(a, b):
    low, high = sorted((a, b))
    coord_range = range(low, high+1)
    if a > b:
        coord_range = reversed(coord_range)
    return coord_range

def get_points(x, y):
    points = zip(cycle(coord_range(x[0], y[0])), cycle(coord_range(x[1], y[1])))
    for point in points:
        yield point
        if point == y:
            break

point_counts = reduce(Counter.__iadd__, map(Counter, starmap(get_points, data)))
print(len([None for freq in point_counts.values() if freq > 1]))
