# Setup
from aocd import get_data
aocd_input = tuple(map(int, get_data(year=2019, day=2).split(',')))

# Longform
def run(data, noun, verb):
    program = list(data)
    program[1]=noun
    program[2]=verb
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

from itertools import product

for noun, verb in product(range(0,100), range(0,100)):
    answer=run(aocd_input, noun, verb)
    if answer==19690720:
        print(noun*100+verb)
        break

