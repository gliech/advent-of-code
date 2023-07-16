from aocd import get_data
from collections.abc import Iterable

def dispense_data(data):
    i, toint = 0, False
    while len(data) >= i:
        part, data = data[:i], data[i:]
        inp = (yield (int(part, base=2) if toint else part))
        i, toint = (inp if isinstance(inp, Iterable) else (inp, True))

def parse_packet(dispenser):
    pkg_ver, pkg_type = dispenser.send(3), dispenser.send(3)
    if pkg_type == 4:
        read_next = 1
        while read_next == 1:
            read_next = dispenser.send(1)
            dispenser.send(4)
    else:
        if dispenser.send(1):
            for _ in range(dispenser.send(11)):
                pkg_ver += parse_packet(dispenser)
        else:
            bits_to_parse = dispenser.send((dispenser.send(15), False))
            sub_dispenser = dispense_data(bits_to_parse)
            next(sub_dispenser)
            try:
                while True:
                    pkg_ver += parse_packet(sub_dispenser)
            except StopIteration:
                pass
    return pkg_ver

data = get_data(year=2021, day=16)
data = bin(int(data, base=16))[2:].zfill(len(data)*4)
data = dispense_data(data)
next(data)
print(parse_packet(data))
