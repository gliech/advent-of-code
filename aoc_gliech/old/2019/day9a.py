# Setup
from aocd import get_data
import curses
aoc_data = get_data(year=2019, day=9).split(',')

# Longform
def long_solution(data):
    from agc import AdventGuidanceComputer as comp
    from curses_helper import curse
    with curse() as scr:
        output = list(comp(data, [1], scr, 0.01))
        scr.addstr(str(output[0]))
        scr.getch()
    return output

# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
