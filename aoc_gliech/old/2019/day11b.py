from aocd import get_data
from agc import AdventGuidanceComputer, EndOfProgram
from operator import attrgetter, itemgetter
from collections import defaultdict
from itertools import product

def camera():
    while True:
        if position in visited_squares:
            yield visited_squares[position]
        else:
            yield 0

aoc_data = get_data(year=2019, day=11).split(',')
position = complex(0,0)
visited_squares = {position:1}
orientation = complex(0,1)
brain = AdventGuidanceComputer(aoc_data)(camera())

try:
    while True:
        visited_squares[position] = next(brain)
        orientation*=complex(0,1-2*next(brain))
        position+=orientation
except EndOfProgram as e:
    pass

# Dirty Output Code
x_values=tuple(int(x) for x in map(attrgetter('real'), visited_squares.keys()))
y_values=tuple(int(y) for y in map(attrgetter('imag'), visited_squares.keys()))

squares=defaultdict(int,visited_squares)
for y in reversed(range(min(y_values),max(y_values)+1)):
    for x in range(min(x_values),max(x_values)+1):
        if squares[complex(x,y)]==1:
            print('█',end='')
        else:
            print(' ',end='')
    print('')

# import code
# code.interact(local=locals())
