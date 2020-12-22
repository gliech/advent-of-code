from aocd import get_data
from collections import defaultdict
from functools import reduce
from collections import Counter

data = get_data(year=2020, day=21).split('\n')

ingrs = []
alrgs = defaultdict(set)
for idx, line in enumerate(data):
    half_a, half_b = line.split(' (contains ')
    ingrs.append(set(half_a.split()))
    for alrg in half_b[:-1].split(', '):
        alrgs[alrg].add(idx)

alrg_ingrs = []
for alrg, idxs in alrgs.items():
    ingr_selection = reduce(set.intersection, map(lambda a: ingrs[a], idxs))
    alrg_ingrs.append([alrg, ingr_selection])

alrg_to_ingr = {}
while alrg_ingrs != []:
    for item in alrg_ingrs:
        if len(item[1]) == 1:
            break
    alrg_ingrs.remove(item)
    ingr = item[1].pop()
    alrg_to_ingr[item[0]] = ingr
    for item in alrg_ingrs:
        item[1].discard(ingr)

ingr_count = Counter()
for line in ingrs:
    ingr_count.update(line)

for ingr in alrg_to_ingr.values():
    ingr_count.pop(ingr)

print('Part 1:', sum(ingr_count.values()))
print('Part 2:', ','.join(ingr for _, ingr in sorted(alrg_to_ingr.items())))
