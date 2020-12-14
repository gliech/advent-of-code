from aocd import get_data
from functools import reduce
from operator import itemgetter

# pre-process input
data = get_data(year=2020, day=13).split('\n')
data = data[1].split(',')
# data = ['7', '13', 'x', 'x', '59', 'x', '31', '19']
# data = ['17','x','13','19']

def solve2(a, b):
    test = a[0]
    while test%b[1] != b[0]:
        test += a[1]
    return (test,a[1]*b[1])

# process data with offsets
bus_schedule = [(a, int(b)) for a, b in enumerate(data) if b != 'x']
# convert offsets to remainders
bus_schedule = [(-a%b, b) for a, b in bus_schedule]
# gratuitous optimization
bus_schedule = sorted(bus_schedule, key=itemgetter(1), reverse=True)
# apply sieve
print(reduce(solve2, busses)[0])
