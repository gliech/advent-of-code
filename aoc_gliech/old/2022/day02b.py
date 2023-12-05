from aocd import get_data
from functools import partial

aoc_data = get_data(year=2022, day=2)
test = """A Y
B X
C Z
B Y
C X
A Z
C Y
A X
B Z"""
example="""A Y
B X
C Z"""

def play(a):
    op, result = map(partial(int, base=36), a.split(" "))
    # return result%3*3
    return (op+result+1)%3+1 + result%3*3

def solution(data):
    return sum(map(play, data.split("\n")))

print(solution(aoc_data))
