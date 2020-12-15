from aocd import get_data
data = get_data(year=2020, day=15).split(',')
data = list(map(int, data))

def play(turns):
    mem = enumerate(data[:-1])
    mem = dict(map(reversed, mem))
    lst = data[-1]
    for turn in range(len(mem), turns-1):
        nxt = turn - mem.get(lst, turn)
        mem[lst] = turn
        lst = nxt
    return lst

print('Part 1:', play(2020))
print('Part 2:', play(30000000))
