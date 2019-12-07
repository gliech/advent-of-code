# Setup
from aocd import get_data
d = map(int, get_data(year=2019, day=1).split('\n'))
# Longform
# Golfed
a=sum(map(lambda x:x//3-2,d))
# Output
print(a)
