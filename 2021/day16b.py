from aocd import get_data
from collections.abc import Iterable
from math import prod

def dispense_data(data):
    i, toint = 0, False
    while len(data) >= i:
        part, data = data[:i], data[i:]
        inp = (yield (int(part, base=2) if toint else part))
        i, toint = (inp if isinstance(inp, Iterable) else (inp, True))

operators = [sum, prod, min, max, None, lambda a: a[0] > a[1],
        lambda a: a[0] < a[1], lambda a: a[0] == a[1]]

def parse_packet(dispenser):
    pkg_ver, pkg_type = dispenser.send(3), dispenser.send(3)
    if pkg_type == 4:
        read_num = 1
        num = ''
        while read_num == 1:
            read_num, num_part = dispenser.send(1), dispenser.send((4, False))
            num += num_part
        return int(num, base=2)
    else:
        sub_values = []
        if dispenser.send(1):
            for _ in range(dispenser.send(11)):
                sub_values.append(parse_packet(dispenser))
        else:
            bits_to_parse = dispenser.send((dispenser.send(15), False))
            sub_dispenser = dispense_data(bits_to_parse)
            next(sub_dispenser)
            try:
                while True:
                    sub_values.append(parse_packet(sub_dispenser))
            except StopIteration:
                pass
        return operators[pkg_type](sub_values)

data = get_data(year=2021, day=16)
data = bin(int(data, base=16))[2:].zfill(len(data)*4)
data = dispense_data(data)
next(data)
print(parse_packet(data))
