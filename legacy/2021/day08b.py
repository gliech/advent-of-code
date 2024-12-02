from aocd import get_data
from itertools import chain, groupby
from operator import methodcaller

def fix_display(line):
    test, output = map(methodcaller('split'), line.split('|'))
    test = {i[0]: [set(j) for j in i[1]] for i in groupby(sorted(test, key=len), len)}
    num = [None]*10
    num[1] = test[2][0]
    num[4] = test[4][0]
    num[7] = test[3][0]
    num[8] = test[7][0]
    num[9] = next(i for i in test[6] if len(num[4] - i) == 0)
    num[6] = next(i for i in test[6] if len(num[1] - i) == 1)
    num[0] = next(i for i in test[6] if i not in (num[6], num[9]))
    num[2] = next(i for i in test[5] if len(i - num[9]) != 0)
    num[3] = next(i for i in test[5] if len(num[7] - i) == 0)
    num[5] = next(i for i in test[5] if i not in (num[2], num[3]))
    rev_num = {tuple(sorted(v)): str(k) for k, v in enumerate(num)}
    return int(''.join(rev_num[tuple(sorted(i))] for i in output))

data = get_data(year=2021, day=8).split('\n')
print(sum(map(fix_display, data)))
