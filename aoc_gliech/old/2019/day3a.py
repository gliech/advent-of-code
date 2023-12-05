# Setup
from aocd import get_data
from operator import methodcaller, add, sub, and_
from functools import partial
# Input
d = map(methodcaller('split',','), get_data(year=2019, day=3).split('\n'))

# Longform
transformations={
    'U': (add,1),
    'D': (sub,1),
    'R': (add,0),
    'L': (sub,0)}

def path_points(coordinates):
    location=[0,0]
    for coordinate in coordinates:
        operation,dimension=transformations[coordinate[0]]
        distance=int(coordinate[1:])
        for _ in range(distance):
            location[dimension]=operation(location[dimension],1)
            yield tuple(location)

a = min(map(sum,map(partial(map,abs),and_(*map(set,map(path_points,d))))))

# Output
print(a)
