# Setup
from aocd import get_data
from itertools import starmap
from operator import sub
from collections import Counter
aoc_data = list(map(int, get_data(year=2020, day=10).split('\n')))

# Longform
def long_solution(data):
    data = list(reversed(sorted(data)))
    data = Counter(starmap(sub,zip([data[0]+3]+data, data+[0])))
    return data[1] * data[3]

# Golfed
def golfed_solution(d):
    return \
d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
