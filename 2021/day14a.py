from aocd import get_data
from collections import Counter

data = get_data(year=2021, day=14)
chain, rules = data.split('\n\n')

rules = (rule.split(' -> ') for rule in rules.split('\n'))
rules = {tuple(key): value for key, value in rules}

def step(chain):
    a = next(chain)
    yield a
    for b in chain:
        yield rules[a, b]
        yield b
        a = b

chain = iter(chain)
for _ in range(10):
    chain = step(chain)
result = Counter(chain).values()
print(max(result) - min(result))
