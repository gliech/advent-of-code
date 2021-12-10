from aocd import get_data
from collections import Counter
from functools import reduce
from operator import itemgetter, mul
import numpy as np
import scipy.ndimage

min_idx = 0
def prepare(a):
    if a[2] == min(a):
        global min_idx
        min_idx += 1
        return min_idx
    elif a[2] == 9:
        return -1
    else:
        return 0

def expand(a):
    if a[2] == 0:
        return max(a)
    else:
        return a[2]

stencil = np.asarray([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
])

data = get_data(year=2021, day=9)
data = np.asarray([[int(j) for j in i] for i in data.split('\n')])
data = scipy.ndimage.generic_filter(data, prepare, footprint=stencil,
        mode='constant', cval=10)

while 0 in data:
    data = scipy.ndimage.generic_filter(data, expand, footprint=stencil,
            mode='constant', cval=-1)

data = Counter(data.flatten())
data.pop(-1)
print(reduce(mul, map(itemgetter(1), data.most_common(3))))
