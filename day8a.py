# Setup
from aocd import get_data
d = map(int, get_data(year=2018, day=8).split(' '))

# Longform
def node():
    children = next(d)
    meta_entries = next(d)
    meta_sum = 0
    for _ in range(children):
        meta_sum += node()
    for _ in range(meta_entries):
        meta_sum += next(d)
    return meta_sum

# Golfed

# Output
print(node())
