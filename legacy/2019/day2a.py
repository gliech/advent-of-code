# Setup
from aocd import get_data
aocd_input = map(int, get_data(year=2019, day=2).split(','))

# Longform
def longform(data):
    program = list(data)
    program[1]=12
    program[2]=2
    for i in range(0,len(program)+1,4):
        opcode = program[i]
        if opcode == 1:
            program[program[i+3]] = program[program[i+1]]+program[program[i+2]]
        elif opcode == 2:
            program[program[i+3]] = program[program[i+1]]*program[program[i+2]]
        elif opcode == 99:
            break
        else:
            raise ValueError(f'unexpect opcode: {opcode}')
    return program[0]

# Golfed
def golfed(d):
    from operator import mul
    n=next(d)
    return(d)

# Output
print(longform(aocd_input))
