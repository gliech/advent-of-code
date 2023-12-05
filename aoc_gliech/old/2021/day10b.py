from aocd import get_data

brackets = {'(':')', '[':']', '{':'}', '<':'>'}
scores = tuple(brackets)

def parse_blocks(line):
    while len(line) > 0 and line[0] in brackets.keys():
        block_open = line.pop(0)
        lower_levels = parse_blocks(line)
        if lower_levels == None:
            return lower_levels
        if len(line) == 0:
            return lower_levels*5+1+scores.index(block_open)
        else:
            block_close = line.pop(0)
            if brackets[block_open] != block_close:
                return None
    else:
        return 0

data = get_data(year=2021, day=10)
data = map(list, data.split('\n'))
data = sorted(filter(None, map(parse_blocks, data)))
print(data[len(data)//2])
