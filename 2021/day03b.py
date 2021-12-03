# Setup
from aocd import get_data
from collections import Counter
from operator import mul, itemgetter
from functools import partial
data = get_data(year=2021, day=3).split('\n')

def sieve(data, bitcrit, idx=0):
    if len(data) == 1:
        return int(data[0], base=2)
    else:
        acc = Counter(map(itemgetter(idx), data))
        bit = bitcrit(map(partial(bitcrit, key=acc.get), [acc, reversed(acc)]))
        return sieve([x for x in data if x[idx] == bit], bitcrit, idx+1)

solution = mul(*(sieve(data, criterion) for criterion in (min, max)))
print(solution)
