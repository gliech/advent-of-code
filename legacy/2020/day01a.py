# Setup
from aocd import get_data
from itertools import combinations
from operator import mul
aoc_data = [ int(a) for a in get_data(year=2020, day=1).split('\n') ]

# Longform
def long_solution(data):
    for number_a in data:
        number_b = 2020 - number_a
        if number_b in data:
            return number_a * number_b
    else:
        raise ValueError

# Golfed
def golfed_solution(d):
    return \
mul(*next(filter(lambda a:sum(a)==2020,combinations(d,2))))

# Output
solve=1
print([long_solution, golfed_solution][solve](aoc_data))
