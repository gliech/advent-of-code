# Setup
from aocd import get_data
from re import findall as find

data = get_data(year=2020, day=14).split('\n')
data = [tuple(map(int, find(r'(\d+)\D+(\d+)', l)[0])) if l[1]=='e' else find(r'[10X]+', l)[0] for l in data]
# data = (
#         '000000000000000000000000000000X1001X',
#         (42, 100),
#         '00000000000000000000000000000000X0XX',
#         (26, 1))

#Solution
def splat_mask(mask):
    if 'X' in mask:
        yield from splat_mask(mask.replace('X', '0', 1))
        yield from splat_mask(mask.replace('X', '1', 1))
    else:
        yield mask

memory = {}

for line in data:
    if type(line) is str:
        mask = line
    else:
        mask_and_addr = zip(mask, bin(line[0])[2:].zfill(36))
        mask_at_addr = ''.join(m if m != '0' else a for m, a in mask_and_addr)
        for translation in splat_mask(mask_at_addr):
            memory[int(translation, base=2)] = line[1]

print(sum(memory.values()))
