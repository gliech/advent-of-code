# Setup
from aocd import get_data
from collections import deque

data = get_data(year=2021, day=6).split(',')
fish = deque([0]*9)

for val in data:
    fish[int(val)] += 1

for _ in range(256):
    fish.rotate(-1)
    fish[6] += fish[8]

print(sum(fish))
