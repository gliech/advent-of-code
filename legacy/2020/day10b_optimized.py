from time import perf_counter

def generate_inner(rng):
    i = 0
    for _ in range(500000):
        i += rng.randint(1, 3)
        yield i

def generate():
    import random
    rng = random.Random('cbc connection')
    out = list(generate_inner(rng))
    random.shuffle(out, rng.random)
    return out

data = generate()
start_time = perf_counter()
#-------------------------------------------------
from collections import deque

data = sorted(data)
vertices = deque([[0, 1]] + [[a, 0] for a in data[:2]])

for idx in range(len(data)):
    if len(data) > idx+2:
        vertices.append([data[idx+2], 0])
    for next_vertex in list(vertices)[1:]:
        if vertices[0][0]+3 < next_vertex[0]:
            break
        next_vertex[1] += vertices[0][1]
    vertices.popleft()

#-------------------------------------------------
stop_time = perf_counter()
print(f"time: {stop_time-start_time:.4f}")
from math import log10
print("result:", log10(vertices[0][1]))
