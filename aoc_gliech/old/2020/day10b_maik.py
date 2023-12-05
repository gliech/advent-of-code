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

max_j = -1
adapters = {}
targets = {}
for num in data:
    if num > max_j: max_j = num
    assert 0 < num
    adapters[num] = True
    for i in range(3): targets[num + 1 + i] = True
max_j += 3
ways = 1

jolt = 0
visited = {}
win = {0: 1}
todo = []

while jolt < max_j:
    visited[jolt] = True
    options = []
    assert (jolt == 0) or adapters[jolt]
    for i in range(3):
        check = jolt + i + 1
        if check in adapters:
            options += [check]
    assert len(options) > 0 or jolt == max_j - 3
    # cull options to prevent double visits
    for opt in options:
        if opt not in win:
            todo += [opt]
            win[opt] = win[jolt]
        else:
            win[opt] += win[jolt]
    if len(todo) > 0:
        jolt = todo.pop(0)
    else:
        jolt = max_j

#-------------------------------------------------
stop_time = perf_counter()
print(f"time: {stop_time-start_time:.4f}")
from math import log10
print("result:", log10(win[max_j - 3]))
