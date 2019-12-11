# Setup
from aocd import get_data
d = list(map(int,get_data(year=2017, day=1)))

# Longform
from functools import reduce
a = reduce(lambda x,y: (y, x[0]+x[1] if x[0]==y else x[1]),d,(d[-1],0))[1]
# Golfed

# Output
print(a)
