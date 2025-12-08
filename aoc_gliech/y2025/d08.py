from functools import reduce
from itertools import combinations
from math import sqrt
from operator import mul, or_, sub
from heapq import nlargest, nsmallest

def prep(data):
    return {tuple(map(int, line.split(","))) for line in data.split("\n")}

def distance(pair):
    return sqrt(sum(map(lambda a: sub(*a)**2, zip(*pair))))

def connect_junctions(edge, circuits):
    junction_circuits = {next(filter(lambda circuit: junction in circuit,
                        circuits), frozenset({junction})) for junction in edge}
    if len(junction_circuits) == 1:
        return False
    circuits -= junction_circuits
    circuits.add(or_(*junction_circuits))
    return True

def part_a(data, connections=1000):
    circuits = set()
    for edge in nsmallest(connections, combinations(prep(data), 2), distance):
        connect_junctions(edge, circuits)
    return reduce(mul, nlargest(3, map(len, circuits)))

def part_b(data):
    junctions = prep(data)
    circuits = {frozenset({junction}) for junction in junctions}
    for edge in sorted(combinations(junctions, 2), key=distance):
        if connect_junctions(edge, circuits) and len(circuits) == 1:
            return mul(*next(zip(*edge)))

if __name__ == "__main__":
    from aoc_gliech import solve
    solve(part_a, part_b)
