from aocd import get_data
from functools import reduce

def sieve2(a, b):
    test = a[0]
    while test%b[1] != b[0]:
        test += a[1]
    return (test,a[1]*b[1])

data = get_data(year=2020, day=13).split('\n')
data = enumerate(data[1].split(','))
data = [(a, int(b)) for a, b in data if b != 'x']
data = [(-a%b, b) for a, b in data]
print(reduce(sieve2, data)[0])
