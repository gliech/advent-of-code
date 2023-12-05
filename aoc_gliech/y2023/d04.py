from functools import cache
from math import floor
from operator import and_

def prep(data):
    return [len(and_(*map(set, (side.split() for side in card.split(":")[1].split("|"))))) for card in data.split("\n")]

def part_a(data):
    return sum(floor(2**(card-1)) for card in prep(data))

def part_b_short(data):
    d = prep(data)
    return (f:=lambda i: sum(map(f, range(len(d)) if i<0 else range(i+1, i+1+d[i])))+1)(-1)-1

def part_b_fast(data):
    d = prep(data)

    @cache
    def card(i):
        return sum(map(card, range(len(d)) if i<0 else range(i+1, i+1+d[i])))+1

    return card(-1)-1

part_b = part_b_fast

if __name__ == "__main__":
    from aocd import get_data
    print(part_b(get_data(day=4, year=2023)))
    #print(all(len(card)==len(set(card)) for card in chain(*prep(get_data(day=4, year=2023)))))
