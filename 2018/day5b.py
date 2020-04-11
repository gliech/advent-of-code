# Setup
import aocd
data = aocd.get_data(year=2018, day=5)

# Longform
def react(polymer):
    polymer = list(polymer)
    polymer_cached_len = 0
    while len(polymer) != polymer_cached_len:
        polymer_cached_len = len(polymer)
        last_letter=''
        for index, letter in reversed(list(enumerate(polymer))):
            inv_letter = letter.upper() if letter.islower() else letter.lower()
            if last_letter == inv_letter:
                polymer.pop(index)
                polymer.pop(index)
                last_letter = ''
            else:
                last_letter = letter
    return polymer_cached_len

# a = { letter: react( filter(lambda x: x != letter and x != letter.upper(), data) ) for letter in 'abcdefghijklmnopqrstuvwxyz' }
a = min( react( filter(lambda x: x != letter and x != letter.upper(), data) ) for letter in 'abcdefghijklmnopqrstuvwxyz' )

# Golfed

# Output
print(a)
