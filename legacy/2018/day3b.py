# Setup
from aocd import data
from re import findall
from itertools import product as p, chain as c
from collections import Counter as C
d = [[int(y)for y in findall('\d+',x)]for x in data.split('\n')]
# print(list(map(list,map(list,d))))

# Longform
# a=sum( overlap>1 for overlap in Counter( chain.from_iterable( product( range(rect[1],rect[1]+rect[3]), range(rect[2],rect[2]+rect[4]) ) for rect in d ) ).values() )
# a=sum(o>1 for o in Counter(chain(*(product(range(r[1],r[1]+r[3]),range(r[2],r[2]+r[4]))for r in d))).values())
# overlap=dict(C(c(*(p(range(i,i+k),range(j,j+l))for _,i,j,k,l in d))))
# a=next(i for i,j,k,l,m in d if l*m == sum(overlap[coord] for coord in p(range(j,j+l),range(k,k+m))))

# Golfed o=overlap r=rectangle
# a=sum(o>1 for o in C(c.from_iterable(p(range(r[1],r[1]+r[3]),range(r[2],r[2]+r[4]))for r in d)).values())
# a=sum(o>1 for o in C(c(*(p(range(r[1],r[1]+r[3]),range(r[2],r[2]+r[4]))for r in d))).values())
# a=sum(o>1 for o in C(c(*(p(range(i,i+k),range(j,j+l))for _,i,j,k,l in d))).values())
o=dict(C(c(*(p(range(i,i+k),range(j,j+l))for _,i,j,k,l in d))))
a=next(i for i,j,k,l,m in d if l*m==sum(o[c]for c in p(range(j,j+l),range(k,k+m))))

# Output
print(a)


