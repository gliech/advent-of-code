from aocd import get_data

brackets    = {'(':')', '[':']', '{':'}', '<':'>'}
char_values = {')':3, ']':57, '}':1197, '>':25137}

def parse_blocks(line):
    while len(line) > 0 and line[0] in brackets.keys():
        block_open = line.pop(0)
        lower_levels = parse_blocks(line)
        if lower_levels != 0:
            return lower_levels
        if len(line) == 0:
            return 0
        else:
            block_close = line.pop(0)
            if brackets[block_open] != block_close:
                return char_values[block_close]
    else:
        return 0

data = get_data(year=2021, day=10)
data = map(list, data.split('\n'))
print(sum(map(parse_blocks, data)))
