# Setup
from aocd import get_data
import numpy as np
from functools import partial
from itertools import product
from time import sleep
def show_seats(arr):
    return '\n'.join(map(lambda a: ''.join('.' if i is None else ('#' if i else 'L') for i in a), arr))

def calc_seats(last_seats):
    next_seats = np.array(last_seats, copy=True)
    for (x, y), val in np.ndenumerate(last_seats):
        if val is not None:
            surrounding_seats = last_seats[max(0,x-1):x+2,max(0,y-1):y+2]
            taken_seats = np.count_nonzero(surrounding_seats == True)
            if taken_seats == 0 and not val:
                next_seats[x,y] = True
            elif taken_seats >= 5 and val:
                next_seats[x,y] = False
    return next_seats

aoc_data = get_data(year=2020, day=11).split('\n')
aoc_data = [[(False if q=='L' else None) for q in list(p)] for p in aoc_data]
next_seats = np.array(aoc_data)
last_seats = np.array([])

while not np.array_equal(last_seats, next_seats):
    last_seats = next_seats
    next_seats = calc_seats(last_seats)
    print(show_seats(next_seats))
print(np.count_nonzero(next_seats == True))
