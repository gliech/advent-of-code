# Setup
from aocd import get_data
aoc_data = get_data(year=2020, day=6).split('\n\n')

# Longform
def long_solution(data):
    return data

# Golfed
def golfed_solution(d):
    return \
sum(map(lambda a:len(set(a.replace('\n',''))),d))

# Output
solve=1
print([long_solution, golfed_solution][solve](aoc_data))
