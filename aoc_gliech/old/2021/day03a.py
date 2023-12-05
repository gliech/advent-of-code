# Setup
from aocd import get_data
import numpy as np
from collections import Counter
from operator import mul
data = get_data(year=2021, day=3).split('\n')
data = np.array(list(map(tuple, data)))

# Longform
def long_solution(data):
    data = np.apply_along_axis(lambda x: Counter(x).most_common(),0,data)
    return mul(*map(lambda x: int(''.join(x), base=2), data[:, 0]))

# Golfed
def golfed_solution(d):
    return \
d

# Output
solve=0
print([long_solution, golfed_solution][solve](data))
