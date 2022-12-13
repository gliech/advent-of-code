from aocd import get_data
from functools import partial

aoc_data = get_data(year=2022, day=2)
test = """A Y
B Z
C X
A X
B Y
C Z
A Z
B X
C Y"""
example="""A Y
B X
C Z"""

def play(a):
    op, me = map(partial(int, base=36), a.split(" "))
    # return 7-(op-me)%3*3+me%3
    # return me-(op-me)%3*3-26
    return (me-op-1)%3*3+me%3+1

def solution(data):
    return sum(map(play, data.split("\n")))

print(solution(aoc_data))
