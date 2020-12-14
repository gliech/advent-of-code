from aocd import get_data
from dataclasses import dataclass

@dataclass
class vertex:
    value: int
    paths_to: int = 0

data = map(int, get_data(year=2020, day=10).split('\n'))
vertices = [vertex(0, 1)] + [vertex(a) for a in sorted(data)]

for idx, current_vertex in enumerate(vertices):
    for next_vertex in vertices[idx+1:idx+4]:
        if current_vertex.value+3 < next_vertex.value:
            break
        next_vertex.paths_to += current_vertex.paths_to

print(vertices[-1].paths_to)
