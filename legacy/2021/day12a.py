from aocd import get_data
from collections import defaultdict

def swim_through_cave(path=[], room='start'):
    if room == 'end':
        return 1
    path.append(room)
    doors = rooms[room] - (set(path) & small_rooms)
    ends = sum(swim_through_cave(path, door) for door in doors)
    path.pop()
    return ends

data = get_data(year=2021, day=12)
rooms = defaultdict(set)

for a, b in map(lambda a: a.split('-'), data.split('\n')):
    rooms[a].add(b)
    rooms[b].add(a)

small_rooms = {room for room in rooms if room.islower()}

print(swim_through_cave())
