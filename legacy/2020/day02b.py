# Setup
from aocd import get_data
import re
from collections import Counter

aoc_data = get_data(year=2020, day=2).split('\n')

# Longform
def long_solution(data):
    counter = 0
    for line in data:
        match = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line).groups()
        pos1, pos2, char, pw = int(match[0]), int(match[1]), match[2], list(match[3])
        if (pw[pos1-1] == char) != (pw[pos2-1] == char):
            print(char, pw[pos1-1], pw[pos2-1])
            counter += 1
    return counter

# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
