# Setup
from aocd import get_data
from collections import Counter
aoc_data = [(l[:1],int(l[1:])) for l in get_data(year=2020, day=12).split('\n')]

card_dir = {'N': 1j, 'E': 1, 'S': -1j, 'W':-1}
rel_dir = {'R': 1, 'L': -1}
rel_to_card = list(card_dir.keys())

# Longform
def long_solution(data):
    pos = 0
    bearing = 1
    for cmd, val in data:
        if cmd in card_dir:
            pos += val*card_dir[cmd]
        elif cmd in rel_dir:
            bearing = (bearing+rel_dir[cmd]*(val//90))%4
        else:
            pos += val*card_dir[rel_to_card[bearing]]
        print(f'{cmd}{val}	= {pos} ({bearing})')
    return int(abs(pos.real+pos.imag))

# Golfed
def golfed_solution(d):
    return \
d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
