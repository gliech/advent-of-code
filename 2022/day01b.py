# Setup
from aocd import get_data
aoc_data = get_data(year=2022, day=1)

def solution(data):
    return \
sum(sorted(sum(map(int, elf.split("\n"))) for elf in data.split("\n\n"))[-3:])

print(solution(aoc_data))
