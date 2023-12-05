from aocd import get_data
from agc import AdventGuidanceComputer, EndOfProgram
from collections import Counter
aoc_data = get_data(year=2019, day=13).split(',')
screen = {}
arcade = AdventGuidanceComputer(aoc_data)()

try:
    while True:
        x = next(arcade)
        y = next(arcade)
        screen[(x,y)]=next(arcade)
except EndOfProgram:
    pass

print(Counter(screen.values())[2])

# import code
# code.interact(local=locals())

