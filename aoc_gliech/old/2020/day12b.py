from aocd import get_data
data = get_data(year=2020, day=12).split()
data = map(lambda l: (l[0],int(l[1:])), data)

card, rel = 'ENWS', 'RL'
pos, wp = 0, 10+1j

for cmd, val in data:
    if cmd in card:
        wp += val*1j**card.index(cmd)
    elif cmd in rel:
        wp *= 1j**((rel.index(cmd)*2-1)*val/90)
    else:
        pos += wp*val

print(int(abs(pos.real) + abs(pos.imag)))
