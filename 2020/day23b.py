from aocd import get_data
from collections import deque
data = deque([int(n) for n in get_data(year=2020, day=23)] + list(range(10,1000001)))
# data = [3,8,9,1,2,5,4,6,7]
hand = deque()
for _ in range(10000000):
    print(_)
    current = data.popleft()
    for __ in range(3):
        hand.append(data.popleft())
    for i in range(4):
        test = ((current-2-i)%1000000)+1
        if test in data:
            insert_point = data.index(test)+1
            for __ in range(3):
                data.insert(insert_point, hand.pop())
            data.append(current)
            break

idx1 = data.index(1)
print(data[idx1+1] * data[idx1+2])
