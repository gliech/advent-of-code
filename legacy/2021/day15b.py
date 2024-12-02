from aocd import get_data
from math import inf
data = get_data(year=2021, day=15)
data = tuple(data.split('\n'))
len_x, len_y = len(data[0]), len(data)

visited = {}
unvisited = {(0,0): 0}
path_costs = {}

for big_y in range(5):
    y_offset = big_y*len_y
    for y, row in enumerate(data):
        for big_x in range(5):
            x_offset = big_x*len_x
            for x, cell in enumerate(row):
                path_costs[x+x_offset,y+y_offset] = (int(cell)+big_x+big_y-1)%9+1

while len(unvisited) > 0:
    current = min(unvisited, key=unvisited.get)
    neighbours = (complex(*current) + i for i in (1,-1,1j,-1j))
    neighbours = ((i.real, i.imag) for i in neighbours)
    neighbours = (i for i in neighbours if 0 <= i[0] < len_x*5 and 0 <= i[1] < len_y*5 and i not in visited)
    for neighbour in neighbours:
        dist_through_curr = unvisited[current] + path_costs[neighbour]
        unvisited[neighbour] = min(unvisited.get(neighbour, inf), dist_through_curr)
    visited[current] = unvisited.pop(current)

print(visited[x+x_offset,y+y_offset])
