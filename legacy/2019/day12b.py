# Setup
from aocd import get_data
from re import findall
from itertools import combinations
from operator import itemgetter
from functools import reduce
from math import gcd

def convert_moon(coord_str):
    return tuple(map(int, findall(r'-?\d+', coord_str)))

moons = tuple(map(convert_moon,get_data(year=2019, day=12).split('\n')))

def one_dim_repeat(dimension):
    view = [[moon[dimension],0] for moon in moons]
    past_views=set()
    while repr(view) not in past_views:
        past_views.add(repr(view))
        for moon_pair in combinations(view,2):
            low_moon = min(moon_pair, key=itemgetter(0))
            high_moon = max(moon_pair, key=itemgetter(0))
            if low_moon[0] != high_moon[0]:
                low_moon[1]+=1
                high_moon[1]-=1
        for moon in view:
            moon[0]+=moon[1]
    elapsed_steps = len(past_views)
    return elapsed_steps

def scm(*args):
    simple_scm = lambda a,b: abs(a*b)//gcd(a,b)
    return reduce(simple_scm,args,1)

one_dim_repeats = tuple(map(one_dim_repeat,range(3)))
print(scm(*one_dim_repeats))

