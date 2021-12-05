from aocd import get_data
from itertools import cycle
from collections import Counter
from functools import reduce
from itertools import starmap, chain
testdata = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
data = get_data(year=2021, day=5).split('\n')
data = {tuple(tuple(map(int, coord.split(','))) for coord in line.split(' -> ')) for line in data}
data = {line for line in data if line[0][0] == line[1][0] or line[0][1] == line[1][1]}

def coord_range(a, b):
    l, h = sorted((a, b))
    coord_range = range(l, h+1)
    if a > b:
        coord_range = reversed(coord_range)
    return coord_range

def get_points(x, y):
    points = zip(cycle(coord_range(x[0], y[0])), cycle(coord_range(x[1], y[1])))
    for point in points:
        yield point
        if point == y:
            break

#point_counts = Counter()
#for line in data:
#    print(line)
#    point_counts += Counter(get_points(*line))

#point_counts = sum((Counter(get_points(*line)) for line in data), start=Counter())
#point_counts = reduce(Counter.__iadd__, (Counter(get_points(*line)) for line in data))
#point_counts = reduce(Counter.__iadd__, map(lambda l: Counter(get_points(*l)), data))
point_counts = reduce(Counter.__iadd__, map(Counter, starmap(get_points, data)))
print(len([None for freq in point_counts.values() if freq > 1]))

# print(list(get_points((770,208), (76,902))))
