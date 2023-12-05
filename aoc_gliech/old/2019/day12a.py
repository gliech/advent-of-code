# Setup
from aocd import get_data
from re import findall
from blessed import Terminal
from time import sleep
from pprint import pprint
from itertools import combinations, chain
from operator import itemgetter

def convert_moon(coord_str):
    numbers = map(int, findall(r'-?\d+', coord_str))
    return [[number,0] for number in numbers]

moons = list(map(convert_moon, get_data(year=2019, day=12).split('\n')))
t = Terminal()

with t.fullscreen():
    for i in range(1,1001):

        for moon_pair in combinations(moons,2):
            for axis_pair in zip(*moon_pair):
                small_axis = min(axis_pair, key=itemgetter(0))
                big_axis = max(axis_pair, key=itemgetter(0))
                if small_axis[0] != big_axis[0]:
                    small_axis[1]+=1
                    big_axis[1]-=1

        for axis in chain(*moons):
            axis[0]+=axis[1]

        with t.location(0,0):
            print(t.clear+f'Iteration {i}:\n')
            pprint(moons)
            sleep(0.005)

def energy(moon):
    pot_energy = sum(map(abs,map(itemgetter(0),moon)))
    kin_energy = sum(map(abs,map(itemgetter(1),moon)))
    return pot_energy*kin_energy

print(sum(map(energy,moons)))
