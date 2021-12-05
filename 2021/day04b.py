from aocd import get_data
import numpy as np
from operator import itemgetter

data = get_data(year=2021, day=4).split('\n\n')
turns = tuple(map(int, data[0].split(',')))
array_helper = lambda x: [list(map(int, l.split())) for l in x.split('\n')]
boards = [np.array(array_helper(board)) for board in data[1:]]

def solve(board):
    for turn in turns:
        board[board == turn] = -1
        if any(map(lambda dim: (board < 0).all(axis=dim).any(), [0,1])):
            board[board < 0] = 0
            return(turns.index(turn), turn*sum(board.flat))

print(max(map(solve, boards), key=itemgetter(0))[1])
