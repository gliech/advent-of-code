from aocd import get_data
from itertools import count
import numpy as np
import scipy.ndimage

def flashed_at(a):
    if  0 < a[4] <= 9:
        return a[4] + len(a[a>9])
    else:
        return 0

def main_loop(data):
    for i in count():
        if np.all(data==0):
            return i
        data += 1
        while np.any(data>9):
            data = scipy.ndimage.generic_filter(data, flashed_at, size = 3,
                    mode='constant', cval=-1)

data = get_data(year=2021, day=11)
data = np.asarray([[int(j) for j in i] for i in data.split('\n')])
print(main_loop(data))
