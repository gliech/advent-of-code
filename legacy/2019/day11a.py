from aocd import get_data
from agc import AdventGuidanceComputer, EndOfProgram
from collections import defaultdict

def camera():
    while True:
        if position in visited_squares:
            yield visited_squares[position]
        else:
            yield 0

aoc_data = get_data(year=2019, day=11).split(',')
visited_squares = {}
position = complex(0,0)
orientation = complex(0,1)
brain = AdventGuidanceComputer(aoc_data)(camera())

try:
    while True:
        visited_squares[position] = next(brain)
        orientation*=complex(0,1-2*next(brain))
        position+=orientation
except EndOfProgram as e:
    pass

print(len(visited_squares))
