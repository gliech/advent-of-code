from aocd import get_data
import numpy as np
import scipy.ndimage

data = get_data(year=2021, day=9) #.split('\n')
data = np.asarray([[int(j) for j in i] for i in data.split('\n')])
stencil = np.array([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]])
low_points = data < scipy.ndimage.minimum_filter(data, footprint=stencil,
        mode='constant', cval=10)
print(sum(data[low_points]+1))
