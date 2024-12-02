# Setup
from aocd import get_data
from itertools import product
from functools import partial
from operator import gt
data = { tuple(map(int,coord.split(', '))) for coord in get_data(year=2018, day=6).split('\n') }
# test data
# data = set([(1,2),(1,50),(40,2),(40,50),(19,20),(21,30),(3,26),(38,24),(19,4),(21,47)])

# Longform
distance_limit = 10000
x_min = min(data)[0]
x_max = max(data)[0]
y_min = min(map(lambda x:x[1],data))
y_max = max(map(lambda x:x[1],data))

def distance(a,b):
    distance_x = abs(a[0]-b[0])
    distance_y = abs(a[1]-b[1])
    return distance_x + distance_y

area = product(range(x_min, x_max+1), range(y_min, y_max+1))
lists_of_distances = ( map(partial(distance, coord), data) for coord in area )
sums_of_distances = map(sum, lists_of_distances)
sums_smaller_cutoff = filter(partial(gt, distance_limit), sums_of_distances)
a = len(tuple(sums_smaller_cutoff))

# Golfed (incomplete)
# a = len(tuple(filter(lambda x: x<distance_limit,(sum(map(lambda x:abs(x[0]-coord[0])+abs(x[1]-coord[1]),data)) for coord in product(range(x_min,x_max+1),range(y_min,y_max+1))))))

# Output
print(a)
