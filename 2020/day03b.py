# Setup
from aocd import get_data
from operator import mul
from functools import reduce
from itertools import starmap
aoc_data = get_data(year=2020, day=3).split('\n')
more_data = ((1,1),(1,3),(1,5),(1,7),(2,1))

# Longform


def slope_calc(y, x, data):
    count = 0
    for idx, row in enumerate(data[::y]):
        if row[idx*x%len(row)] == '#':
            count += 1
    return count

def slopes(data1, data2):
    for y, x in data2:
        yield slope_calc(y, x, data1)

def long_solution(data1, data2):
    return reduce(mul, slopes(data1, data2))

# Golfed
def golfed_solution(d, m):
    # return reduce(mul,starmap(lambda y,x:[l[i*x%len(l)]for i,l in enumerate(d[::y])].count('#'), m))
    return \
reduce(mul,[[l[i*x%len(l)]for i,l in enumerate(d[::y])].count('#')for y,x in m])

# Output
solve=1
print([long_solution, golfed_solution][solve](aoc_data, more_data))
