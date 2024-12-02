from aocd import get_data
data = [int(n) for n in get_data(year=2020, day=23)] + list(range(10,1000001))
# data = [3,8,9,1,2,5,4,6,7]
for _ in range(10000000):
    print(_)
    current = data.pop(0)
    hand, data = data[:3], data[3:]
    for i in range(9):
        test = ((current-2-i)%1000000)+1
        if test in data:
            insert_point = data.index(test)+1
            data1, data2 = data[:insert_point], data[insert_point:]
            data = data1 + hand + data2 + [current]
            break

idx1 = data.index(1)
data = data[idx1+1:] + data[:idx1]
print(''.join(map(str,data)))
