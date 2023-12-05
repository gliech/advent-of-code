# Setup
from aocd import get_data
from operator import methodcaller
from functools import partial
from collections import Counter
import re
def mangle(field):
    return map(methodcaller('split',':'), field.split())

data = get_data(year=2020, day=4).split('\n\n')
data = map(lambda a: dict(map(methodcaller('split',':'), a.split())), data)

def test_hgt(hgt):
    try:
        number = int(hgt[:-2])
        unit = hgt[-2:]
    except:
        return False
    else:
        if unit == 'in':
            return 59 <= number <= 76
        elif unit == 'cm':
            return 150 <= number <= 193
        else:
            return False

def date_test(lower, upper):
    def inner_date_test(date):
        try:
            date = int(date)
        except:
            return False
        else:
            return lower <= date <= upper
    return inner_date_test

tests = {
    'byr': date_test(1920, 2002),
    'iyr': date_test(2010, 2020),
    'eyr': date_test(2020, 2030),
    'hgt': test_hgt,
    'hcl': partial(re.fullmatch, r'#[0-9a-f]{6}'),
    'ecl': lambda a: a in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': partial(re.fullmatch, r'[0-9]{9}')}

def validate(passport):
    for field, test in tests.items():
        if not test(passport.get(field, '')):
            return False
    else:
        return True

# Longform
def long_solution(data):
    return Counter(map(validate,data))[True]

# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](data))
