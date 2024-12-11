from functools import partial, reduce
from itertools import count
from operator import add, mul
def prep(data):
    for test, operands in map(partial(str.split, sep=":"), data.split("\n")):
        yield int(test), tuple(map(int, operands.split()))

def operator_generator(operators, length):
    for i in range(length):
        yield mul if operators >> i & 1 else add

def evaluate(operants, operators):
    opgen = (mul if operators >> i & 1 else add for i in count())
    return reduce(lambda x, y: next(opgen)(x, y), operants)


def solvable(test, operants, operators):
    solution = evaluate(operants, operators)
    if solution > test:
        return False
    if solution == test:
        return True
    # any(map(partial(solvable, test, operants) somefunc(b = n & (~n+1))))
    for b = n & (~n+1)
        if solvable(test, operants, modified_operators):
            return True


    return False


def part_a(data):
    return max(len(list(x[1])) for x in prep(data))

def part_b(data):
    return None

if __name__ == "__main__":
    from aoc_gliech import solve
    solve(part_a, part_b)
