# Setup
from aocd import get_data
from itertools import starmap
aoc_data = get_data(year=2020, day=3).split('\n')

# Longform
def long_solution(data):
    count = 0
    for idx, row in enumerate(data):
        if row[idx*3%len(row)] == '#':
            count += 1

    return count

# Golfed
def golfed_solution(d):
    # return len(list(filter(lambda a:a[1][a[0]*3%len(a[1])]=='#',enumerate(d))))
    return [a[i*3%len(a)]for i,a in enumerate(d)].count('#')

# Output
solve=1
print([long_solution, golfed_solution][solve](aoc_data))
