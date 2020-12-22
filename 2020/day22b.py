from aocd import get_data
from functools import partial
from collections import deque
from operator import itemgetter, methodcaller, mul
from itertools import starmap

def game(deck_a, deck_b):
    past_states = set()
    while deck_a and deck_b:
        current_state = (tuple(deck_a), tuple(deck_b))
        if current_state in past_states:
            return False
        else:
            past_states.add(current_state)
        card_a = deck_a.popleft()
        card_b = deck_b.popleft()
        if len(deck_a) >= card_a and len(deck_b) >= card_b:
            sub_deck_a = deque(list(deck_a)[:card_a])
            sub_deck_b = deque(list(deck_b)[:card_b])
            round_winner = game(sub_deck_a, sub_deck_b)
        else:
            round_winner = card_a < card_b
        if round_winner:
            deck_b.append(card_b)
            deck_b.append(card_a)
        else:
            deck_a.append(card_a)
            deck_a.append(card_b)
    return bool(deck_b)

data = get_data(year=2020, day=22)
data = data.split('\n\n')
data = map(methodcaller('split', '\n'), data)
data = map(itemgetter(slice(1, None)), data)
data = map(partial(map, int), data)
data = map(deque, data)
data = list(data)

winner = data[game(*data)]

solution = reversed(winner)
solution = enumerate(solution, 1)
solution = starmap(mul, solution)
solution = sum(solution)

print(solution)
