from aocd import get_data
from operator import methodcaller
import numpy as np

data = get_data(year=2021, day=13)
coords, instructions = map(methodcaller('split', '\n'), data.split('\n\n'))

coords = np.loadtxt(coords, dtype=int, delimiter=',')
coords = np.rot90(coords)

paper = np.zeros(coords.max(1)+1, dtype=int)
paper[tuple(coords)] = 1

for axis, offset in map(methodcaller('split', '='), instructions):
    offset = int(offset)
    rotate = axis.endswith('x')
    paper = np.rot90(paper, -rotate)
    top, _, bottom = np.vsplit(paper, [offset, offset+1])
    bottom = np.flipud(bottom)
    small, big = sorted((top, bottom), key=lambda a: a.size)
    big[-small.shape[0]:] += small
    paper = big
    paper = np.rot90(paper, rotate)

for line in paper:
    print(''.join('#' if dot > 0 else ' ' for dot in line))
