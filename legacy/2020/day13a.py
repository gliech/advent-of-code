# Setup
from aocd import get_data
from operator import itemgetter, mul
from functools import reduce
data = get_data(year=2020, day=13).split('\n')
data = [int(data[0]), [int(a) if a!='x' else a for a in data[1].split(',')]]
# data = [939, [7,13,'x','x',59,'x',31,19]]

# Longform
def long_solution(data):
    arrival = int(data[0])
    busses = list(map(int, filter(lambda a: a != 'x', data[1])))
    departures = list(map(lambda a: (a, (a-arrival%a)%a), busses))
    earliest_departure = min(departures, key=lambda a: a[1])
    return earliest_departure[0]*earliest_departure[1]

# Golfed
def golfed_solution(d):
    return \
reduce(mul,min([(a,-d[0]%a) for a in d[1]if a!='x'],key=itemgetter(1)))

# Output
solve=1
print([long_solution, golfed_solution][solve](data))
