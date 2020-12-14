# Setup
from aocd import get_data
from operator import methodcaller
def mangle(field):
    return map(methodcaller('split',':'), field.split())

data = get_data(year=2020, day=4).split('\n\n')
data = map(lambda a: dict(map(methodcaller('split',':'), a.split())), data)

# Longform
def long_solution(data):
    valid_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    return len(list(filter(lambda a: set(a.keys()).issuperset(valid_fields), data)))

# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](data))
