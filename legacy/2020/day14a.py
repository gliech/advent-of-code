# Setup
from aocd import get_data
from re import findall as find

data = get_data(year=2020, day=14).split('\n')
data = [tuple(map(int, find(r'(\d+)\D+(\d+)', l)[0])) if l[1]=='e' else find(r'[10X]+', l)[0] for l in data]

#Solution
memory = {}

for line in data:
    if type(line) is str:
        true_mask = int(line.translate(str.maketrans('1X', '01')), base=2)
        mask_fill = int(line.replace('X', '0'), base=2)
    else:
        memory[line[0]] = line[1] & true_mask | mask_fill

print(sum(memory.values()))
