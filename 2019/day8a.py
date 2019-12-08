# Setup
from aocd import get_data
aoc_data = get_data(year=2019, day=8)

# Longform
def long_solution(data):
    from itertools import zip_longest
    from collections import Counter

    a = min(map(Counter,zip(*[iter(data)]*(25*6))), key=lambda x: x['0'])
    return a['1']*a['2']


# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
