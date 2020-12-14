# Setup
from aocd import get_data
import numpy as np
from itertools import repeat
def show_seats(arr):
    return '\n'.join(map(lambda a: ''.join('.' if i is None else ('#' if i else 'L') for i in a), arr))

def directions():
    direction = [1, 1]
    modifier =[-1, 1]
    for i in range(8):
        direction[i//2%2] += modifier[i//4%2]
        yield tuple(direction)

cached_directions = tuple(directions())

def test_coords(x, y, max_x, max_y):
    x_component = (x, max_x)
    y_component = (y, max_y)
    funcs = {
        -1: lambda component: range(component[0]-1, -1, -1),
        0: lambda component: repeat(component[0]),
        1: lambda component: range(component[0]+1, component[1])}
    for x, y in cached_directions:
        yield zip(funcs[x](x_component), funcs[y](y_component))

def test_seat(coord, threshold, seats):
    for direction in test_coords(*coord, *seats.shape):
        for test_coord in direction:
            val = seats[test_coord]
            if val is not None:
                if val == True:
                    threshold -= 1
                    if threshold < 0:
                        return False
                break
    return True

def calc_seats(last_seats):
    next_seats = np.array(last_seats, copy=True)
    for coord, val in np.ndenumerate(last_seats):
        if val is not None:
            if val and not test_seat(coord, 4, last_seats):
                next_seats[coord] = False
            elif (not val) and test_seat(coord, 0, last_seats):
                next_seats[coord] = True
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

#n   x->0    y       - 0 +y
#ne  x->0    y->max  - + +x
#e   x       y->max  0 + +x
#se  x->max  y->max  + + -y
#s   x->max  y       + 0 -y
#sw  x->max  y->0    + - -x
#w   x       y->0    0 - -x
#nw  x->max  y->0    - - +y

