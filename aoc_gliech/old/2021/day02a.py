# Setup
from aocd import get_data
from operator import methodcaller
data = get_data(year=2021, day=2).split('\n')
data = map(methodcaller("split"), data)
data = [(a, int(b)) for a, b in data]

# Longform
def long_solution(data):
    depth, position = 0, 0
    for direction, value in data:
        match direction:
            case "forward":
                position += value
            case "down":
                depth += value
            case "up":
                depth -= value
    return depth * position

# Golfed
def golfed_solution(d):
    return \
d

# Output
solve=0
print([long_solution, golfed_solution][solve](data))
