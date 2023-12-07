import re
from collections import Counter
from operator import itemgetter

def hand_value(hand):
    htype = sum(value**2 for value in Counter(hand).values())
    for idx, letter in enumerate("AKQJT"):
        hand = hand.replace(letter, chr(69-idx))
    return htype*16**5+int(hand,16)


def prep(data):
    return ((hand_value(l.split()[0]), int(l.split()[1])) for l in data.split("\n"))

def part_a(data):
    return sum((i+1)*v[1] for i, v in enumerate(sorted(prep(data), key=itemgetter(0))))

def part_b(data):
    return None

if __name__ == "__main__":
    from aocd import get_data
    print(part_a(get_data(year=2023, day=7)))
