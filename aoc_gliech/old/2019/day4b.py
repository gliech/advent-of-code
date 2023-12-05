# Setup
from aocd import get_data
from collections import Counter
d = map(int,get_data(year=2019, day=4).split('-'))
# Longform
a = len(list(filter(lambda x:sorted(x)==x and 2 in Counter(x).values(),map(list,(map(str,range(*d)))))))
# Golfed

# Output
print(a)
