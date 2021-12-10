from aocd import get_data

data = get_data(year=2021, day=7).split(',')
data = tuple(map(int, data))
data = min(sum(abs(a-i)*(abs(a-i)+1)//2 for a in data) for i in range(min(data), max(data)))
print(data)
