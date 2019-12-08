# Setup
from aocd import get_data
aoc_data = get_data(year=2019, day=8)

# Longform
def long_solution(data):
    from itertools import zip_longest
    from collections import Counter

    width=25
    height=6
    volume=width*height
    image = list(['2']*volume)
    for layer in zip(*[iter(data)]*volume):
        for idx, pixel in enumerate(layer):
            if image[idx] == '2':
                image[idx] = pixel
    image_black = ''.join(image).replace('0',' ')
    image_white = image_black.replace('1','█')
    return '\n'.join(map(''.join,zip(*[iter(image_white)]*width)))

# Golfed
def golfed_solution(d):
    pass

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
