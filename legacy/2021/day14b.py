from aocd import get_data
from itertools import pairwise
from collections import Counter

data = get_data(year=2021, day=14)
chain, rules = data.split('\n\n')

rules = (rule.split(' -> ') for rule in rules.split('\n'))
rules = {tuple(key): value for key, value in rules}
duplicates = Counter(chain[1:-1])
pairs = Counter(pairwise(chain))

for _ in range(10):
    next_pairs = Counter()
    for pair, num in pairs.items():
        duplicates[rules[pair]] += num
        next_pairs.update({(pair[0], rules[pair]): num, (rules[pair], pair[1]): num})
    pairs = next_pairs

result = Counter()
for pair, count in pairs.items():
    result[pair[0]] += count
    result[pair[1]] += count

result.subtract(duplicates)

result = result.values()
print(max(result) - min(result))

