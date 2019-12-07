# Setup
from aocd import get_data
d = map(int,get_data(year=2019, day=4).split('-'))
# Longform
a = len(list(filter(lambda x:sorted(x)==x and len(set(x))<6,map(list,(map(str,range(*d)))))))
# Golfed
# a=len([1 for x in[list(str(x))for y in range(*d)]if(sorted(x)==x)&(len(set(x))<6)])
# Output
print(a)
