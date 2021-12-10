from aocd import get_data
from itertools import chain

data = get_data(year=2021, day=8).split('\n')
data = chain.from_iterable(line.split('|')[1].split() for line in data)
data = [val for val in data if not 4<len(val)<7]
print(len(data))
