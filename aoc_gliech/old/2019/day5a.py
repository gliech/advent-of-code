# Setup
from aocd import get_data
d = get_data(year=2019, day=5).split(',')

# Solution
from agc import AdventGuidanceComputer

a = list(AdventGuidanceComputer(d)([1]))

# Output
print(a)
