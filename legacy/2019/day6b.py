# Setup
from aocd import get_data
aoc_data = dict(map(lambda x: reversed(x.split(')')),get_data(year=2019, day=6).split('\n')))

# Longform
def long_solution(data):
    def orbit_map(satellite):
        root_path = set()
        while satellite != 'COM':
            satellite = data[satellite]
            root_path.add(satellite)
        return root_path

    return len(orbit_map('SAN')^orbit_map('YOU'))

# Golfed
def golfed_solution(d):
    def o(s): return 0 if s=='COM'else o(d[s])+1
    return sum(map(o,d.keys()))

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
