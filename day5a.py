# Setup
from aocd import data
d=list(data)
d_cached_len = 0
# Longform
while len(d) != d_cached_len:
    d_cached_len = len(d)
    last_letter=''
    for index, letter in reversed(list(enumerate(d))):
        inv_letter = letter.upper() if letter.islower() else letter.lower()
        if last_letter == inv_letter:
            d.pop(index)
            d.pop(index)
            last_letter = ''
        else:
            last_letter = letter

# Golfed

# Output
print(d, d_cached_len)
