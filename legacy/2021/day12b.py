from aocd import get_data
from collections import defaultdict

def swim_through_cave(room, path=[], visited_twice=False):
    if room == 'end':
        return 1
    doors = rooms[room] - (set(path)&small_rooms if visited_twice else {'start'})
    ends = 0
    for door in doors:
        next_visited_twice = visited_twice or door in set(path) & small_rooms
        ends += swim_through_cave(door, path+[room], next_visited_twice)
    return ends

data = get_data(year=2021, day=12)
rooms = defaultdict(set)

for a, b in map(lambda a: a.split('-'), data.split('\n')):
    rooms[a].add(b)
    rooms[b].add(a)

small_rooms = {room for room in rooms if room.islower()}

print(swim_through_cave('start'))
