# Setup
from aocd import get_data
aoc_data = [list(map(int,x.split('\t'))) for x in get_data(year=2017, day=2).split('\n')]

# Longform
def long_solution(data):
    from itertools import combinations
    def divide_row(row):
        candidates = map(sorted,combinations(row,2))
        divisible = min(candidates,key=lambda x: x[1]%x[0])
        return divisible[1]//divisible[0]
    return sum(map(divide_row,data))

# Golfed
def golfed_solution(d):
    from itertools import combinations, starmap
    from operator import floordiv, mod
    #return sum(map(lambda c: c[1]//c[0],map(lambda r: min(map(sorted,combinations(r,2)),key=lambda x:x[1]%x[0]),d)))
    return sum(starmap(floordiv,map(lambda r: min(map(lambda y: **sorted(y,reverse=True),combinations(r,2)),key=mod),d)))


# Output
solve=1
print([long_solution, golfed_solution][solve](aoc_data))
