# Setup
from aocd import get_data
from itertools import repeat, chain, starmap
ichain = chain.from_iterable
from functools import partial
from operator import mul
real_data = get_data(year=2019, day=16)
test_data = '19617804207202209144916044189917'
aoc_data = tuple(map(int,iter(real_data)))

def fft(signal):
    output = []
    for i in range(len(signal)):
        pattern = ichain(map(partial(repeat, times=i+1), ichain(repeat((0,1,0,-1)))))
        next(pattern)
        output.append(abs(sum(starmap(mul, zip(signal, pattern))))%10)
    return output

for phase in range(100):
    aoc_data = fft(aoc_data)

print(''.join(map(str,aoc_data))[:8])
