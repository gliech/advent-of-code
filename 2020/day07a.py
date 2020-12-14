# Setup
from aocd import get_data
import re
from operator import methodcaller
from collections import defaultdict
from functools import reduce

def parse_bag(contents):
    contents = re.findall(r'(\d+) (\w+ \w+)', contents)
    return dict(map(reversed, contents))

aoc_data = get_data(year=2020, day=7).split('\n')
aoc_data = map(methodcaller('split', ' bags contain '), aoc_data)
aoc_data = {name: parse_bag(contents) for name, contents in aoc_data}

rev_data = defaultdict(set)

for name, contents in aoc_data.items():
    for item in contents.keys():
        rev_data[item].add(name)

def solve(bag):
    solution = reduce(lambda a,b: a.union(b), map(solve, rev_data[bag]), set())
    solution.add(bag)
    return solution

print(len(solve('shiny gold'))-1)
