# Setup
from aocd import get_data
aoc_data = list(map(int, get_data(year=2020, day=10).split('\n')))

# 0 1 2 3 4 7 8 9 12
# i 1 1 1
#   i 2 2 1
#     i 4 3
#       i 7
#         i 7
#           i 7 7
#             i 14
#               i 14

# Longform
def long_solution(data):
    data = [0, *sorted(data)]
    data = [[a,0] for a in data]
    data[0][1] = 1
    for idx, stp in enumerate(data):
        for nxt in data[idx+1:idx+4]:
            if stp[0]+3 < nxt[0]:
                break
            nxt[1] += stp[1]
    return data[-1][1]

# Golfed
def golfed_solution(d):
    d=[[0,1]]+[[a,0]for a in sorted(d)]


# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))
