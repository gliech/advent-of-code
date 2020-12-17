# Setup
from aocd import get_data
from itertools import product, repeat

def import_state(plane, dim):
    for x, line in enumerate(plane.split('\n')):
        for y, cell in enumerate(line):
            if cell == "#":
                yield (x, y, *repeat(0, dim-2))

def neighbours(*args):
    return product(*map(lambda a: range(a-1, a+2), args))

def calculate_cell(last_state, cell):
    live_neighbours = last_state.intersection(neighbours(*cell))
    if cell in live_neighbours:
        return 3<=len(live_neighbours)<=4
    else:
        return len(live_neighbours) == 3

def extend_next_state(next_state, last_state, cell):
    for neighbour in neighbours(*cell):
        if neighbour not in next_state:
            next_state[neighbour] = calculate_cell(last_state, neighbour)

def next_state(last_state):
    next_state = dict()
    for cell in last_state:
        extend_next_state(next_state, last_state, cell)
    return set(key for key, value in next_state.items() if value)

data = get_data(None,17,2020)
# data = ".#.\n..#\n###"

def run_automaton(data, dimensions):
    state = set(import_state(data, dimensions))
    for _ in range(6):
        state = next_state(state)
    return len(state)

print('Part 1:', run_automaton(data, 3))
print('Part 2:', run_automaton(data, 4))
