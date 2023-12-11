import numpy as np
from itertools import combinations, starmap
from operator import sub
custom_data = """
        ....
        .#..
        ...#
        ....
        ...#"""

def prep(data):
    data = data.split('\n')
    return np.array([list(line) for line in data], dtype='U1')

def part_a(data):
    image = prep(data)
    for axis in 0, 1:
        empty_spaces = np.where(np.all(image == ".", axis))[0]
        image = np.insert(image, empty_spaces, ".", axis=1-axis)
    return sum(map(sum, map(np.abs, starmap(sub, combinations(map(np.array, zip(*np.where(image == "#"))), 2)))))

def part_b(data):
    image = prep(data)
    print(image)
    dist_past = map(sum, map(np.abs, starmap(sub, combinations(map(np.array, zip(*np.where(image == "#"))), 2))))
    for axis in 0, 1:
        empty_spaces = np.where(np.all(image == ".", axis))[0]
        image = np.insert(image, empty_spaces, ".", axis=1-axis)
    dist_now = map(sum, map(np.abs, starmap(sub, combinations(map(np.array, zip(*np.where(image == "#"))), 2))))
    return starmap(lambda a, b: a+(b-a)*100, zip(dist_past, dist_now))

if __name__ == "__main__":
    from aoc_gliech import solve
    solve(part_a, part_b, data=custom_data)
