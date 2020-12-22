from aocd import get_data
from functools import partial
from collections import deque
from operator import itemgetter, methodcaller, mul
from itertools import starmap

data = get_data(year=2020, day=22)
data = data.split('\n\n')
data = map(methodcaller('split', '\n'), data)
data = map(itemgetter(slice(1, None)), data)
data = map(partial(map, int), data)
data = map(deque, data)
data = list(data)

while deque() not in data:
    card_a, card_b = map(methodcaller('popleft'), data)
    if card_a > card_b:
        data[0].append(card_a)
        data[0].append(card_b)
    else:
        data[1].append(card_b)
        data[1].append(card_a)

winner = max(data)
solution = reversed(winner)
solution = enumerate(solution, 1)
solution = starmap(mul, solution)
solution = sum(solution)

print(solution)
