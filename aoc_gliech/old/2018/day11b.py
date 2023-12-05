# Setup
from aocd import get_data
from itertools import accumulate
from operator import itemgetter
d = int( get_data(year=2018, day=11) )

# Longform
power_lvl = lambda x,y: ( (x + 10) * y + d ) * ( x + 10 ) // 100 % 10 - 5
cells = tuple( tuple( power_lvl(x,y) for y in range(1,301) ) for x in range(1,301) )



# def next_size(total, size):
#     return total + sum( cells[size-1][i] + cells[i][size-1] for i in range(size-1) ) + cells[size-1][size-1]
# answer = accumulate(range(301), next_size)

def sizes():
    total = 0
    for size in range(1,301):
        total += sum( cells[size-1][i] + cells[i][size-1] for i in range(size-1) ) + cells[size-1][size-1]
        yield from y_positions( size, total )

def y_positions(size, total):
    yield from x_positions( 0, size, total )
    for y in range(300-size):
        total += sum( cells[i][y+size] - cells[i][y] for i in range(size) )
        yield from x_positions( y+1, size, total )

def x_positions(y, size, total):
    yield 0, y, size, total
    for x in range(300-size):
        total += sum( cells[x+size][i] - cells[x][i] for i in range(y,y+size) )
        yield x+1, y, size, total

answer = max(sizes(), key=itemgetter(3))
# Golfed

# Output
print('{},{},{}'.format(answer[0]+1, answer[1]+1, answer[2]))
