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
    data = max(map(lambda a: int(''.join([transpose[x] for x in a]), 2), data))
    return data

# Golfed
def golfed_solution(d):
    return \
max(map(lambda a:int(''.join([dict(zip('LRFB','0101'))[x]for x in a]),2),d))

# Output
solve=1
print([long_solution, golfed_solution][solve](aoc_data))
