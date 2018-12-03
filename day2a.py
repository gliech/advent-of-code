# Setup
from aocd import data 
from collections import Counter as c
from functools import reduce as r
from operator import mul as m
d = data.split('\n')

# Longform
# answer = reduce( mul, ( sum( ( repetition in count.values() ) for count in ( Counter(box_id) for box_id in data) ) for repetition in (2,3) ) )

# Golfed s=string, h=hash, x=generic number
a=r(m,(sum((x in h.values())for h in(c(s)for s in d))for x in(2,3)))

# Output
print(a)


