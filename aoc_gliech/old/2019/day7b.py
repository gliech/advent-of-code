# Setup
from aocd import get_data
aoc_data = get_data(year=2019, day=7).split(',')

# Longform
def long_solution(data):
    from itertools import permutations,chain
    from functools import reduce
    from agc import AdventGuidanceComputer as comp

    def amplifier_chain(phases):
        amp_input = [phases[0],0]
        comp0=comp(data)(amp_input)
        comp1=comp(data)(chain([phases[1]],comp0))
        comp2=comp(data)(chain([phases[2]],comp1))
        comp3=comp(data)(chain([phases[3]],comp2))
        comp4=comp(data)(chain([phases[4]],comp3))
        try:
            while True:
                amp_input.append(next(comp4))
        except StopIteration as e:
            pass
        return amp_input[-1]

    return max(map(amplifier_chain, permutations(range(5,10))))

# Golfed
def golfed_solution(d):
    from itertools import permutations,chain,repeat
    from functools import reduce
    from agc import AdventGuidanceComputer as comp

    def c(l,p):
        list(map(l.append,reduce(lambda x,y: comp(d)(chain(y,x)),map(lambda z:[z],p),l)))
        return l[-1]
    return max(c([0],p) for p in permutations(range(5,10)))

# Output
solve=1
print([long_solution, golfed_solution][solve](aoc_data))
