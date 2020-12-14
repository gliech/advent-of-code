# Setup
from aocd import get_data
from operator import and_
from functools import reduce
aoc_data = (grp.split('\n') for grp in get_data(year=2020, day=6).split('\n\n'))

# Longform
def long_solution(data):
    return list(data)

# Golfed
def golfed_solution(d):
    return \
sum(map(lambda a:len(reduce(and_,map(set,a))),d))

# Output
solve=1
print([long_solution, golfed_solution][solve](aoc_data))
