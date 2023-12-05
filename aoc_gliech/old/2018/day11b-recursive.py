# Setup
from aocd import get_data
from math import sqrt
from operator import itemgetter
from sympy import primerange
d = int( get_data(year=2018, day=11) )

# Longform
power_lvl = lambda x,y: ( (x + 10) * y + d ) * ( x + 10 ) // 100 % 10 - 5
cells = tuple( tuple( power_lvl(x,y) for y in range(1,301) ) for x in range(1,301) )

'''
def gen_primes(max):
    primes = []
    test_primes = []
    for i in range(2, max+1):
        if sqrt(i) >= primes[0] if primes else '':
            test_primes.append(primes.pop(0))
        for prime in test_primes:
            if not i%prime:
                break
        else:
            primes.append(i)
    return(primes)
'''

primes = tuple(primerange(0,300))

def get_squares(matrix, size):
    # first return the given array
    dim=len(matrix)
    for x in range(dim):
        for y in range(dim):
            yield x, y, size, matrix[x][y]

    for prime in primes:
        if prime > dim:
            break
        trim_dim = dim//prime*prime
        for x_offset in range(dim%prime+1):
            for y_offset in range(dim%prime+1):
                trim_matrix = [ matrix[i][y_offset:trim_dim+y_offset] for i in range(x_offset,trim_dim+x_offset)]
                rows = ( trim_matrix[i:i+prime] for i in range(0,trim_dim,prime) )
                new_matrix = [ [ sum( sum( row[i][j:j+prime] ) for i in range(prime) ) for j in range(0,trim_dim,prime) ] for row in rows ]
                new_size=size*prime
                yield from get_squares(new_matrix, new_size)

answer = max(get_squares(cells, 1), key=itemgetter(3))
# Golfed

# Output
print('{},{},{},{}'.format(answer[0], answer[1], answer[2], answer[3]))
