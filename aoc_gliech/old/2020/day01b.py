# Setup
from aocd import get_data
from itertools import combinations
from operator import mul
from functools import reduce
aoc_data = [ int(a) for a in get_data(year=2020, day=1).split('\n') ]

# Longform
def long_solution(data):
    for number_a, number_b in combinations(data, 2):
        number_c = 2020 - (number_a + number_b)
        if number_c in data:
            return number_a * number_b * number_c
    else:
        raise ValueError

# Golfed
def golfed_solution(d):
    return reduce(mul,next(filter(lambda a:sum(a)==2020,combinations(d,3))))

# Output
solve=1
print([long_solution, golfed_solution][solve](aoc_data))
