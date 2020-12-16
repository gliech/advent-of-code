from aocd import get_data
from functools import partial
from re import findall

y=set().union(*map(lambda a:range(a,next(i[0])+1),(i:=list(map(partial(map,int),
map(partial(findall,r'\d+'),get_data(year=2020, day=16).split('\n\n')))))[0]))
print(sum(b for b in i[2]if b not in y))
