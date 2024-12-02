# Setup
from aocd import get_data
from re import findall
from functools import partial
data = set( tuple( findall(r'\b\w\b', connection) ) for connection in get_data(year=2018, day=7).split('\n') )

# Longform
steps = []

while len(data) > 1: 
    next_step = min( set( item[0] for item in data ) - set( item[1] for item in data ) )
    steps.append(next_step)
    data.difference_update(set(filter(lambda x: x[0] == next_step, data)))

steps.extend(*data)
# Golfed

# Output
print(''.join(steps))
