# Setup
from aocd import get_data
from itertools import count, combinations

aoc_data = list(map(int, get_data(year=2020, day=9).split('\n')))

# Longform
def long_solution(data):
    for i in count():
        compare = aoc_data[i:i+25]
        test = aoc_data[i+25]
        if test not in map(sum, combinations(compare, 2)):
            return test
    else:
        raise ValueError
    return data

# Golfed
def golfed_solution(d):
    return \
next(filter(lambda a:a[25] not in map(sum,combinations(a[:-1],2)),map(lambda i:d[i:i+26],count())))[25]

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
