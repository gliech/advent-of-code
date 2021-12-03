# Setup
from aocd import get_data
from operator import lt
from itertools import pairwise, starmap
aoc_data = [ int(a) for a in get_data(year=2021, day=1).split('\n') ]
test_data = [192, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def solution(data):
    return sum(starmap(lt, pairwise(data)))

print(solution(aoc_data))
