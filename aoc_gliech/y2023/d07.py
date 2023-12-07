from collections import Counter
from operator import itemgetter
from functools import partial

def count_for_b(hand):
    hand = Counter(hand)
    jokers = hand.pop("J", 0)
    hand[next(iter(hand.most_common()), "J")[0]] += jokers
    return hand

def winnings(data, count_cards, card_order):
    tie_val = lambda h: sum(list(card_order).index(c)*16**i for i, c in enumerate(reversed(h)))
    hand_val = lambda h: (sum(value**2 for value in count_cards(h).values())<<20)+tie_val(h)
    hands = ((hand_val(l.split()[0]), int(l.split()[1])) for l in data.split("\n"))
    return sum((i+1)*v[1] for i, v in enumerate(sorted(hands, key=itemgetter(0))))

part_a = partial(winnings, count_cards=Counter, card_order="23456789TJQKA")
part_b = partial(winnings, count_cards=count_for_b, card_order="J23456789TQKA")

if __name__ == "__main__":
    from aocd import get_data
    print(part_b(get_data(year=2023, day=7)))
