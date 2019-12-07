# Setup
from aocd import get_data
aoc_data = get_data(year=2019, day=7).split(',')

# Longform
def long_solution(data):
    from itertools import permutations,chain
    from functools import reduce
    from agc import AdventGuidanceComputer as comp

    def amplifier(signal, phase):
        return comp()([phase, signal])

    def amplifier_input():
        a = 0
        while True:
            a = (yield a)
            yield

    def amplifier_chain(phases):
        amp_input = amplifier_input()
        amps=comp(data)(chain([phases[4]],comp(data)(chain([phases[3]],comp(data)(chain([phases[2]],comp(data)(chain([phases[1]],comp(data)(chain([phases[0]],amp_input))))))))))
        try:
            while True:
                output = next(amps)
                amp_input.send(output)
        except StopIteration as e:
            pass
        finally:
            return output

    return max(map(amplifier_chain, permutations(range(5,10))))

# Golfed
def golfed_solution(d):
    pass

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
