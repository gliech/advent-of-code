from aocd import get_data
import numpy as np
import csv

data = get_data(year=2021, day=4).split('\n\n')
turns = map(int, data[0].split(','))
array_helper = lambda x: [list(map(int, l.split())) for l in x.split('\n')]
boards = [np.array(array_helper(board)) for board in data[1:]]

def solve(turns, boards):
    for turn in turns:
        for board in boards:
            board[board == turn] = -1
            if any(map(lambda dim: (board < 0).all(axis=dim).any(), [0,1])):
                board[board < 0] = 0
                return turn*sum(board.flat)

print(solve(turns, boards))
