from aocd import get_data
from functools import partial
from re import findall
from itertools import filterfalse
from operator import contains

print(sum(filterfalse(partial(contains,set().union(*map(lambda a:range(a,
next(i[0])+1),(i:=list(map(partial(map,int),map(partial(findall,r'\d+'),
get_data(None,16,2020).split('\n\n')))))[0]))),i[2])))
