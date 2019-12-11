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
        value = self._memory[parameter+self._relative_base]
        self._print(f'{value}<'+f'{self._relative_base}{parameter:+} ')
        return value

    def _position_mode(self, parameter):
        value = self._memory[parameter]
        self._print(f'{value}<'+f'{parameter} ')
        return value

    def _direct_mode(self, parameter):
        self._print(f'{parameter} ')
        return parameter

    def _init_runtime(self, inputs=None):
        self._memory = defaultdict(partial(int,0),enumerate(self._program))
        self._position = 0
        self._relative_base = 0
        self._mode_ints = 0
        if inputs is not None:
            self._inputs = iter(inputs)
        else:
            self._inputs = self._input_generator()

    @staticmethod
    def _input_generator():
        for i in count(1):
            yield int(input(f'input[{i}] '))

    def _increment(self):
        value = self._memory[self._position]
        self._position+=1
        return value

    def _jump(self, destination):
        self._position = destination

    def execute_instruction(self):
        self._print(t.bright_yellow(f'{self._position:04}: '))
        instruction = self._increment()
        opcode = instruction%100
        self._mode_ints = instruction//100
        function = self._instruction_set[opcode]
        self._print(
                t.bold_bright_blue(f'{function.__name__[1:]:>6} ')+
                t.bright_black(f'{instruction:05} '))
        return function()

    def _get_mode(self):
        mode = self._mode_ints%10
        self._mode_ints //= 10
        return mode

    def _get_parameter(self):
        mode = self._get_mode()
        parameter = self._increment()
        parameter_value = self._parameter_modes[mode](parameter)
        return parameter_value

    def _write_value(self, value):
        mode = self._get_mode()
        if mode == 0:
            addr = self._increment()
            self._memory[addr] = value
            self._print(f'{value}'+f'>{addr}')
        elif mode == 2:
            addr = self._increment()
            self._memory[addr+self._relative_base] = value
            self._print(f'{value}'+f'>{self._relative_base}{addr:+}')
        else:
            raise ValueError(f'Tried to write value while parameter mode was \'{mode}\'')

    def __call__(self, inputs=None):
        self._init_runtime(inputs)
        try:
            while True:
                sleep(0.000001)
                output = self.execute_instruction()
                self._print('\n')
                if output is not None:
                    yield output
        except EndOfProgram as e:
            self._print('\n\n')

    def _print(self, msg):
        print(msg,end='')

    def _add(self):
        new_value = self._get_parameter()+self._get_parameter()
        self._write_value(new_value)

    def _mul(self):
        new_value = self._get_parameter()*self._get_parameter()
        self._write_value(new_value)

    def _input(self):
        self._write_value(next(self._inputs))

    def _output(self):
        return self._get_parameter()

    def _jmp_t(self):
        condition = self._get_parameter()
        destination = self._get_parameter()
        if condition:
            self._jump(destination)

    def _jmp_f(self):
        condition = self._get_parameter()
        destination = self._get_parameter()
        if not condition:
            self._jump(destination)

    def _less(self):
        gliech = 1 if self._get_parameter() < self._get_parameter() else 0
        self._write_value(gliech)

    def _equals(self):
        gliech = 1 if self._get_parameter() == self._get_parameter() else 0
        self._write_value(gliech)

    def _set_rb(self):
        self._relative_base+=self._get_parameter()

    def _exit(self):
        raise EndOfProgram

