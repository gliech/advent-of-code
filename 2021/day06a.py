# Setup
from aocd import get_data
from collections import Counter, deque

data = get_data(year=2021, day=6).split(',')
data = Counter(int(n) for n in data)
fish = deque([0]*9)

for idx, val in data.items():
    fish[idx] = val

for _ in range(256):
    print(fish)
    fish.rotate(-1)
    fish[6] += fish[8]

print(sum(fish))
