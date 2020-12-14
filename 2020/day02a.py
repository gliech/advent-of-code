# Setup
from aocd import get_data
import re
from collections import Counter

aoc_data = get_data(year=2020, day=2).split('\n')

# Longform
def long_solution(data):
    counter = 0
    for line in data:
        match = re.match(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
        low, high, rule, pw = match.groups()
        pwc = Counter(pw)
        check = pwc[rule]
        if int(low) <= check <= int(high):
            counter += 1
    return counter

# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
