# Setup
from aocd import get_data
import numpy as np
from collections import Counter
from operator import mul
from functools import partial
data = get_data(year=2021, day=3).split('\n')
data = np.array(list(map(tuple, data)))

def common(a, b):
    for idx in range(len(a)):
        if a[idx] != b [idx]:
            return idx

# Longform
def long_solution(data):
    a = [''.join(x) for x in np.apply_along_axis(lambda x: Counter(x).most_common(),0,data)[:, 0]]
    b = map(lambda x: max(data, key=partial(common, x)), a)
    return mul(*map(lambda x: int(''.join(x), base=2), b))

# Golfed
def golfed_solution(d):
    return \
d

# Output
solve=0
print([long_solution, golfed_solution][solve](data))
