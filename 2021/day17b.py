# Setup
from aocd import get_data
from collections import Counter
from itertools import accumulate, count, product, starmap
import re

def test(vel_x, vel_y):
    x, y = 0, 0
    while x <= data[1] and y >= data[2]:
        if x >= data[0] and y <= data[3]:
            return True
        else:
            x += vel_x
            y += vel_y
            vel_x = max(0, vel_x-1)
            vel_y -= 1
    else:
        return False

data = get_data(year=2021, day=17)
data = re.match(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", data)
data = [int(value) for value in data.groups()]

min_y = data[2]
max_y = abs(data[2])-1
min_x = next(filter(lambda a: a[1]>=data[0], enumerate(accumulate(count()))))[0]
max_x = data[1]

result = starmap(test, product(range(min_x, max_x+1), range(min_y, max_y+1)))
result = Counter(result)
print(result[True])
