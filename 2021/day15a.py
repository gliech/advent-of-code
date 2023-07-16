from aocd import get_data
from math import inf
data = get_data(year=2021, day=15)
data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

path_costs = {}
for y, row in enumerate(data.split('\n')):
    for x, cell in enumerate(row):
        path_costs[x,y] = int(cell)
unvisited = {node: inf for node in path_costs}
unvisited[0,0] = 0
visited = {}

while len(unvisited) > 0:
    current = min(unvisited, key=unvisited.get)
    neighbours = (complex(*current) + i for i in (1,-1,1j,-1j))
    neighbours = {(i.real, i.imag) for i in neighbours} & set(unvisited)
    for neighbour in neighbours:
        dist_through_curr = unvisited[current] + path_costs[neighbour]
        unvisited[neighbour] = min(unvisited[neighbour], dist_through_curr)
    visited[current] = unvisited.pop(current)

print(visited[x,y])
