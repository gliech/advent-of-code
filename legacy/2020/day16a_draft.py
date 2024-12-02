# Setup
from aocd import get_data
from itertools import starmap, chain
from functools import partial, reduce
from operator import add, methodcaller
import re
data = get_data(year=2020, day=16).split('\n\n')

def parse_rule(line):
    name = line.split(':')[0]
    nums = tuple(map(int, re.findall(r'\d+', line)))
    ranges = zip(nums[::2],map(partial(add, 1), nums[1::2]))
    return (name, list(starmap(range, ranges)))

rules = dict(map(parse_rule, data[0].split('\n')))
other_tickets = [map(int, ticket.split(',')) for ticket in data[2].split('\n')[1:]]
alw = set().union(*sum(rules.values(), []))
solution = sum(filter(lambda a: a not in alw, chain.from_iterable(other_tickets)))
print(solution)
