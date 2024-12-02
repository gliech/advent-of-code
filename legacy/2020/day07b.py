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

def solve(bag):
    solution = sum(map(lambda a: solve(a[0])*int(a[1]), aoc_data[bag].items()))
    return solution+1

print(solve('shiny gold')-1)
