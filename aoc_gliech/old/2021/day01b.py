# Setup
from aocd import get_data
from operator import lt
from itertools import pairwise, starmap
aoc_data = [ int(a) for a in get_data(year=2021, day=1).split('\n') ]
test_data = [192, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# Longform
def long_solution(data):
    data = list(map(sum, zip(data[:-2], data[1:-1], data[2:])))
    return sum(starmap(lt, zip(data[:-1], data[1:])))

# Golfed
def golfed_solution(d):
    return \
sum(starmap(lt,pairwise(map(sum,zip(d,d[1:],d[2:])))))


# Output
solve=1
print([long_solution, golfed_solution][solve](aoc_data))

