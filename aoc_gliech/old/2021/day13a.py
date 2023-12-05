from aocd import get_data
from operator import methodcaller
import numpy as np

data = get_data(year=2021, day=13)
coords, instructions = map(methodcaller('split', '\n'), data.split('\n\n'))

coords = np.loadtxt(coords, dtype=int, delimiter=',')
coords = np.rot90(coords)

paper = np.zeros(coords.max(1)+1, dtype=int)
paper[tuple(coords)] = 1

axis, offset = instructions[0].split('=')
offset = int(offset)
if axis.endswith('x'):
    paper = np.rot90(paper, 3)
top, bottom = np.flipud(paper[:offset]), paper[offset+1:]
small, big = sorted((top, bottom), key=lambda a: a.size)
small = small.copy()
small.resize(big.shape)
paper = np.flipud(small + big)
if axis.endswith('x'):
    paper = np.rot90(paper)

print(np.count_nonzero(paper))
