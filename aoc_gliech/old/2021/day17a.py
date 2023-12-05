# Setup
from aocd import get_data
from itertools import accumulate, count, takewhile
import re

data = get_data(year=2021, day=17)
data = re.match(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", data)
data = [int(value) for value in data.groups()]

height = (abs(data[2])-1)*abs(data[2])//2

print(height)
