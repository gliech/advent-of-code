# Setup
from aocd import get_data
d = map(int, get_data(year=2018, day=8).split(' '))

# Longform
def node():
    children = next(d)
    meta_entries = next(d)
    meta_sum = 0
    if children:
        child_values = []
        for _ in range(children):
            child_values.append(node())
        for _ in range(meta_entries):
            meta_value = next(d)
            if meta_value > 0:
                try:
                    meta_sum += child_values[meta_value-1]
                except:
                    pass
    else:
        for _ in range(meta_entries):
           meta_sum += next(d)
    return meta_sum

# Golfed

# Output
print(node())
