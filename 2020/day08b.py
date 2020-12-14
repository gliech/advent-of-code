# Setup
from aocd import get_data
from operator import methodcaller
from dataclasses import dataclass

@dataclass
class instruction:
    op: str
    arg: int
    ran: bool = False


class computer:
    def __init__(self, program):
        self._acc = 0
        self._ptr = 0
        self._prg = program
    def __next__(self):
        if self._ptr >= len(self._prg):
            if self._ptr == len(self._prg):
                print(self._acc)
            raise StopIteration
        else:
            curr_instr = self._prg[self._ptr]
            if curr_instr.ran:
                raise StopIteration
            else:
                self._run(curr_instr)
    def __iter__(self):
        return self
    def _run(self, instr):
        instr.ran = True
        methodcaller(instr.op, instr.arg)(self)
    def acc(self, arg):
        self._ptr += 1
        self._acc += arg
    def nop(self, arg):
        self._ptr += 1
    def jmp(self, arg):
        self._ptr += arg

aoc_data = get_data(year=2020, day=8).split('\n')
aoc_data = list(map(methodcaller('split'), aoc_data))

for idx, _ in filter(lambda a: a[1][0] in ['nop','jmp'], enumerate(aoc_data)):
    program = [instruction(a[0], int(a[1])) for a in aoc_data]
    if program[idx].op == 'nop':
        program[idx].op = 'jmp'
    else:
        program[idx].op = 'nop'
    for _ in computer(program):
        pass
