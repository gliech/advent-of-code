# Setup
from aocd import get_data
aoc_data = get_data(year=2020, day=5).split('\n')

# Longform
def long_solution(data):
    transpose = {
        'L': '0',
        'R': '1',
        'F': '0',
        'B': '1'}
    data = list(map(lambda a: int(''.join([transpose[x] for x in a]), 2), data))
    for point in data:
        if point+1 not in data and point+2 in data:
            return point+1
    else:
        raise ValueError

# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
