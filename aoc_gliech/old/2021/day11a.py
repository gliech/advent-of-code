from aocd import get_data
import numpy as np
import scipy.ndimage

def flashed_at(a):
    if  0 < a[4] <= 9:
        # for some reason using len(a[a>9]) is a lot faster than np.sum(a>9),
        # np.count_nonzero(a>9) or (a>9).sum()
        return a[4] + len(a[a>9])
    else:
        return 0

data = get_data(year=2021, day=11)
data = np.asarray([[int(j) for j in i] for i in data.split('\n')])
flashes = 0

for _ in range(100):
    data += 1
    while np.any(data > 9):
        flashes += np.sum(data > 9)
        data = scipy.ndimage.generic_filter(data, flashed_at, size = 3,
                mode='constant', cval=-1)

print(flashes)
