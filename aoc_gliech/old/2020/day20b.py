from aocd import get_data
from collections import deque
from operator import mul
from functools import reduce
import numpy as np
import re

edge_getters = (
        lambda a: a[-1],
        lambda a: a[::-1,-1],
        lambda a: a[0,::-1],
        lambda a: a[:,0])

edges = {}

def append_edges(position, tile):
    for idx, edge_getter in enumerate(edge_getters):
        edges[tuple(edge_getter(tile))] = (position+1j**idx, idx)

def rotations(tile):
    for _ in range(2):
        for i in range(3):
            yield np.rot90(tile,i)
        tile = np.fliplr(tile)

data = get_data(year=2020, day=20).split('\n\n')
data = [np.array([list(line) for line in tile.split('\n')[1:]]) for tile in data]

first_tile = data.pop()
tiles = {0+0j: first_tile}
append_edges(0+0j, first_tile)

while data:
    tile = data.pop(0)
    for rotation in rotations(tile):
        current_edge = tuple(rotation[0])
        if current_edge in edges:
            location, loc_rot = edges[current_edge]
            rotation = np.rot90(rotation, loc_rot) # maybe other way around
            tiles[location] = rotation
            append_edges(location, rotation)
            break
    else:
        data.append(tile)

print(tiles[2-2j])
print(tiles[2-1j])
