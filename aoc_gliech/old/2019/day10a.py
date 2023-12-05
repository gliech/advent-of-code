# Setup
from aocd import get_data
aoc_data = get_data(year=2019, day=10).split('\n')

# Longform
def long_solution(data):
    def coords(pic):
        for y, row in enumerate(pic):
            for x, pixel in enumerate(row):
                if pixel=='#':
                    yield (x,y)

    coords=list(coords(data))

    def visible(astr):
        x=astr[0]
        y=astr[1]
        for a_x, a_y in coords:
            a_x-=x
            a_y-=y
            if a_x==0 and a_y==0:
                continue
            elif a_y==0:
                yield(a_x/abs(a_x),0)
            else:
                yield(a_x/abs(a_y),a_y/abs(a_y))

    return max(map(lambda a: len(set(visible(a))), coords))

# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
