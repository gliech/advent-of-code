# Setup
from aocd import get_data
aoc_data = get_data(year=2019, day=7).split(',')

# Longform
def long_solution(data):
    from itertools import permutations
    from functools import reduce
    from agc import AdventGuidanceComputer
    agc = AdventGuidanceComputer(data)

    def amplifier(signal, phase):
        return next(agc([phase, signal]))

    def amplifier_chain(signals):
        return reduce(amplifier, signals, 0)

    return max(map(amplifier_chain, permutations(range(5))))

# Golfed
def golfed_solution(d):
    pass

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
