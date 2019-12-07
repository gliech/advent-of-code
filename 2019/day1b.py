# Setup
from aocd import get_data
d = map(int, get_data(year=2019, day=1).split('\n'))

# Longform
def calc_fuel(mass):
    fuel = mass//3-2
    if fuel <= 0:
        return 0
    else:
        return fuel+calc_fuel(fuel)

a = sum(map(calc_fuel, d))
# Golfed

# Output
print(a)
