# Setup
from aocd import get_data
aoc_data = dict(map(lambda x: reversed(x.split(')')),get_data(year=2019, day=6).split('\n')))

# Longform
def long_solution(data):
    from time import sleep

    def orbit_map(satellite):
        if satellite != 'COM':
            parent = data[satellite]
            print(satellite, end='(')
            return orbit_map(parent)+1
        else:
            print('COM', end='\n\n')
            sleep(0.001)
            return 0

    return sum(map(orbit_map, data.keys()))

# Golfed
def golfed_solution(d):
    def o(s): return 0 if s=='COM'else o(d[s])+1
    return sum(map(o,d.keys()))

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
