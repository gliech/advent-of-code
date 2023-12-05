from aocd import get_data
from collections import Counter
from operator import mul
from functools import reduce
import numpy as np
import re

def side_to_int(side):
    bin_str = ''.join(side).translate(str.maketrans('.#', '01'))
    return int(bin_str, base=2)

reverse_edge = lambda a: int(f'{a:010b}'[::-1], base=2)

edge_getters = (
        lambda a: a[0],
        lambda a: a[:,-1],
        lambda a: a[-1,::-1],
        lambda a: a[::-1,0],
        )

data = get_data(year=2020, day=20).split('\n\n')
tile_dict = {}

for tile in data:
    tile_id = re.findall(r'\d+', tile)[0]
    tile_dict[tile_id] = np.array(list(map(list, tile.split('\n')[1:])))

edges = {}
for key, value in tile_dict.items():
    for idx, eget in enumerate(edge_getters):
        edges[(key, idx)] = side_to_int(eget(value))

edge_list = list(edges.values())
border = Counter()
for edge_id, edge in edges.items():
    if edge_list.count(edge)!=2 and edge_list.count(reverse_edge(edge))!=1:
        border[edge_id[0]] += 1

corners = [tile for tile, count in border.items() if count == 2]

print(reduce(mul,map(int,corners)))
