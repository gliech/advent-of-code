from aocd import data
from itertools import cycle

known_freqs = set()
current_freq = 0
changes = list(map(int, data.split('\n') ))
# changes = [+7, +7, -2, -7, -4]

for change in cycle(changes):
    current_freq += change
    if current_freq in known_freqs:
        print(current_freq)
        break
    else:
        known_freqs.add(current_freq)
