from itertools import count
from blessings import Terminal
from collections import defaultdict
from functools import partial
from time import sleep

t = Terminal()

class EndOfProgram(Exception):
    pass

class AdventGuidanceComputer:
    def __init__(self, program):
        self._program = tuple(map(int,program))
        self._parameter_modes = [
            self._position_mode,
            self._direct_mode,
            self._relative_mode,
        ]
        self._instruction_set = {
            1: self._add,
            2: self._mul,
            3: self._input,
            4: self._output,
            5: self._jmp_t,
            6: self._jmp_f,
            7: self._less,
            8: self._equals,
            9: self._set_rb,
            99: self._exit,
        }
        self._init_runtime()

    def _relative_mode(self, parameter):
        addr = parameter+self._relative_base
        self._print(t.color(166)(self._fmt_int(addr, 4)))
        return addr

    def _position_mode(self, parameter):
        addr = parameter
        self._print(t.color(220)(self._fmt_int(addr, 4)))
        return addr

    def _direct_mode(self, parameter):
        addr = self._position-1
        self._print('self')
        return addr

    def _init_runtime(self, inputs=None, silent=False):
        self._memory = defaultdict(partial(int,0),enumerate(self._program))
        self._position = 0
        self._relative_base = 0
        self._mode_ints = 0
        self._silent = silent
        if inputs is not None:
            self._inputs = iter(inputs)
        else:
            self._inputs = self._input_generator()

    @staticmethod
    def _input_generator():
        while True:
            with t.location():
                inpt = input('  kbrd: ')
            yield int(inpt)

    @staticmethod
    def _fmt_int(number, length=7, fill_zero=True):
        output = f'{number:{0 if fill_zero else ""}{length}}'
        if len(output) > length:
            cut_long = length//2
            cut_short = cut_long+length%2-1
            if number >=0:
                cut_start=cut_short
                cut_end=cut_long
            else:
                cut_start=cut_long
                cut_end=cut_short
            return '…'.join((output[:cut_start],output[-cut_end:]))
        else:
            return output

    def _increment(self):
        value = self._memory[self._position]
        self._position+=1
        return value

    def _jump(self, destination):
        self._position = destination

    def execute_instruction(self):
        self._print(
                t.color(220)(self._fmt_int(self._position, 4)),
                t.color(166)(self._fmt_int(self._relative_base, 4)+': '))
        instruction = self._increment()
        opcode = instruction%100
        self._mode_ints = instruction//100
        function = self._instruction_set[opcode]
        self._print(
                t.bold_bright_blue(f'{function.__name__[1:]:>7}'),
                t.bright_black(self._fmt_int(instruction,5)))
        return function()

    def _get_addr(self):
        mode = self._mode_ints%10
        self._mode_ints //= 10
        parameter = self._increment()
        self._print('  ')
        addr = self._parameter_modes[mode](parameter)
        return addr

    def _read_value(self):
        addr = self._get_addr()
        value = self._memory[addr]
        self._print(t.bright_black('>')+self._fmt_int(value,7))
        return value

    def _write_value(self, value):
        addr = self._get_addr()
        self._memory[addr] = value
        self._print(t.bright_black('<')+t.bold(self._fmt_int(value,7)))

    def __call__(self, inputs=None, silent=False):
        self._init_runtime(inputs,silent)
        try:
            while True:
                output = self.execute_instruction()
                self._print('\n')
                if output is not None:
                    yield output
        except EndOfProgram as e:
            self._print('\n\n')
            raise e

    def _print(self, *messages):
        if not self._silent:
            print(*messages,end='')

    def _add(self):
        new_value = self._read_value()+self._read_value()
        self._write_value(new_value)

    def _mul(self):
        new_value = self._read_value()*self._read_value()
        self._write_value(new_value)

    def _input(self):
        self._write_value(next(self._inputs))

    def _output(self):
        return self._read_value()

    def _jmp_t(self):
        condition = self._read_value()
        destination = self._read_value()
        if condition:
            self._jump(destination)

    def _jmp_f(self):
        condition = self._read_value()
        destination = self._read_value()
        if not condition:
            self._jump(destination)

    def _less(self):
        gliech = 1 if self._read_value() < self._read_value() else 0
        self._write_value(gliech)

    def _equals(self):
        gliech = 1 if self._read_value() == self._read_value() else 0
        self._write_value(gliech)

    def _set_rb(self):
        self._relative_base+=self._read_value()

    def _exit(self):
        raise EndOfProgram

