from aocd import get_data

data = get_data(year=2021, day=7).split(',')
data = tuple(map(int, data))
data = min(sum(map(lambda a: abs(a-i), data)) for i in range(min(data), max(data)))
print(data)
