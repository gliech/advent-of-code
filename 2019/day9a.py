# Setup
from aocd import get_data
aoc_data = get_data(year=2019, day=9).split(',')

# Longform
def long_solution(data):
    from agc import AdventGuidanceComputer as comp
    return list(comp(data)([1]))

# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
