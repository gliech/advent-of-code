from aocd import get_data
from agc import AdventGuidanceComputer as comp

print(list(comp(get_data(year=2019, day=9).split(','))([2]))[1])
