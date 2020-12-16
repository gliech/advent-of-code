# Setup
from aocd import get_data
from functools import partial
from re import findall

data = get_data(year=2020, day=16).split('\n\n')
data = map(partial(findall, r'\d+'), data)
data = map(partial(map, int), data)
data = list(data)

rules = map(lambda a: range(a, next(i)+1), i:=data[0])
rules = set().union(*rules)

solution = filter(lambda a: a not in rules, data[2])
solution = sum(solution)

print(solution)
