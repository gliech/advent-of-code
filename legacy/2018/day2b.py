# Setup
from aocd import data
from itertools import combinations as c, starmap as s
d = data.split('\n')
# d = [ 'abcd', 'abed', 'axcy' ]

# Longform
# a = next( filter( lambda x: len(x)==24, ( ''.join( letter1 for letter1, letter2 in combination if letter1==letter2 ) for combination in starmap( zip, combinations(data, 2) ) ) ) )
# a=next(filter(lambda x:len(x)==len(data[0]-1),(''.join(a for a,b in i if a==b)for i in starmap(zip,combinations(data,2)))))

# Golfed
a=next(filter(lambda x:len(x)==len(d[0])-1,(''.join(a for a,b in i if a==b)for i in s(zip,c(d,2)))))

# Output
print(a)

