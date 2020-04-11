# Setup
from aocd import get_data
from itertools import product
d = int( get_data(year=2018, day=11) )

# Longform
power_lvl = lambda x,y: ( (x + 10) * y + d ) * ( x + 10 ) // 100 % 10 - 5
power_lvls = { coord: power_lvl(*coord) for coord in product(range(1,301), range(1,301)) }
matrix_lvl = lambda x,y: sum( power_lvls[coord] for coord in product(range(x, x+3 ), range(y, y+3)) )
matrix_lvls = { coord: matrix_lvl(*coord) for coord in product(range(1,299), range(1,299)) }
answer = max(matrix_lvls, key=lambda x: matrix_lvls[x])
# Golfed

# Output
print('{},{}'.format(*answer))
