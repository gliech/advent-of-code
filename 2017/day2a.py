# Setup
from aocd import get_data
aoc_data = [list(map(int,x.split('\t'))) for x in get_data(year=2017, day=2).split('\n')]

# Longform
def long_solution(data):
    return sum(map(lambda x: max(x)-min(x),data))

# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
