from aocd import get_data
from collections import defaultdict

def swim_through_cave(path=['start'], paths_to_end=0, extra_visit_used=False):
    current_room = path[-1]
    if current_room == 'end':
        paths_to_end += 1
    else:
        if extra_visit_used:
            doors = rooms[current_room] - (set(path) & small_rooms)
        else:
            doors = rooms[current_room] - {'start'}
        for door in doors:
            extra_visit = extra_visit_used or door in set(path) & small_rooms
            path.append(door)
            paths_to_end = swim_through_cave(path, paths_to_end, extra_visit)
            path.pop()
    return paths_to_end

data = get_data(year=2021, day=12)
rooms = defaultdict(set)

for a, b in map(lambda a: a.split('-'), data.split('\n')):
    rooms[a].add(b)
    rooms[b].add(a)

small_rooms = {room for room in rooms if room.islower()}

print(swim_through_cave())
