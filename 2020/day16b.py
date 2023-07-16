from aocd import get_data
from itertools import starmap, chain
from functools import partial, reduce
from operator import mul, add, methodcaller, itemgetter
import re

def parse_rule(line):
    name = line.split(':')[0]
    nums = tuple(map(int, re.findall(r'\d+', line)))
    ranges = zip(nums[::2], map(partial(add, 1), nums[1::2]))
    return (name, list(starmap(range, ranges)))

data = map(methodcaller('split', '\n'), get_data(year=2020, day=16).split('\n\n'))
rules = dict(map(parse_rule, data[0].split('\n')))
tickets = [[int(f) for f in t.split(',')] for t in data[2].split('\n')[1:]]
my_ticket = tuple(map(int, data[1].split('\n')[1].split(',')))
allowed_values = set().union(*sum(rules.values(), []))
valid_tickets = filter(lambda a: set(a).issubset(allowed_values), tickets)
rule_sets = list(map(set, zip(*valid_tickets)))
possible_field_positions ={k: set(map(itemgetter(0), filter(lambda a: a[1].issubset(set().union(*v)), enumerate(rule_sets)))) for k, v in rules.items()}
field_positions = {}
while possible_field_positions:
    for k, v in possible_field_positions.items():
        if len(v) == 1:
            position = possible_field_positions.pop(k).pop()
            field_positions[k] = position
            for position_possibilities in possible_field_positions.values():
                position_possibilities.remove(position)
            break
relevant_positions = [v for k,v in field_positions.items() if k.startswith('departure')]
print(reduce(mul, map(lambda a: my_ticket[a], relevant_positions)))
