# Setup
from aocd import get_data
d = list(map(int,get_data(year=2017, day=1)))

# Longform
from functools import reduce
a = sum(map(lambda x: 2*x[0] if x[0]==x[1] else 0,zip(d[:len(d)//2],d[len(d)//2:])))
# Golfed

# Output
print(a)
