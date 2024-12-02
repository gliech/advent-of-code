# Setup
from aocd import get_data
from itertools import count, combinations
from collections import deque

aoc_data = list(map(int, get_data(year=2020, day=9).split('\n')))

part_a = 776203571

# Longform
def long_solution(data, part_a):
    cont_set = deque()
    cont_sum = 0
    for i in data:
        if cont_sum == part_a:
            return min(cont_set) + max(cont_set)
        cont_sum += i
        cont_set.append(i)
        while cont_sum > part_a:
            cont_sum -= cont_set.popleft()

# Golfed
def golfed_solution(d, a):
    return \
d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data, part_a))
