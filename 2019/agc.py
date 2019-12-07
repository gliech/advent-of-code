from itertools import count
from blessings import Terminal

t = Terminal()

class EndOfProgram(Exception):
    pass

class AdventGuidanceComputer:
    def __init__(self, program):
        self._program = tuple(map(int,program))
        self._parameter_modes = [
            lambda x: self._memory[x],
            lambda x: x,
        ]
        self._instruction_set = {
            1: self._add,
            2: self._multiply,
            3: self._input,
            4: self._output,
            5: self._jump_if_true,
            6: self._jump_if_false,
            7: self._less_than,
            8: self._equals,
            99: self._exit,
        }
        self._init_runtime()

    def _init_runtime(self, inputs=None):
        self._memory = list(self._program)
        self._position = 0
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
        instruction = self._increment()
        opcode = instruction%100
        self._mode_ints = instruction//100
        function = self._instruction_set[opcode]
        print(t.bright_black(f'{self._position:03}:'), f'{instruction:5} {function.__name__[1:]}')
        return function()

    def _get_mode(self):
        mode = self._mode_ints%10
        self._mode_ints //= 10
        return mode

    def _get_parameter(self):
        return self._parameter_modes[self._get_mode()](self._increment())

    def _write_value(self, value):
        mode = self._get_mode()
        if mode == 0:
            self._memory[self._increment()] = value
        else:
            raise ValueError(f'Tried to write value while parameter mode was \'{mode}\'')

    def __call__(self, inputs=None):
        self._init_runtime(inputs)
        try:
            while True:
                output = self.execute_instruction()
                if output is not None:
                    yield output
        except EndOfProgram as e:
            pass

    def _add(self):
        new_value = self._get_parameter()+self._get_parameter()
        self._write_value(new_value)

    def _multiply(self):
        new_value = self._get_parameter()*self._get_parameter()
        self._write_value(new_value)

    def _input(self):
        self._write_value(next(self._inputs))

    def _output(self):
        return self._get_parameter()

    def _jump_if_true(self):
        condition = self._get_parameter()
        destination = self._get_parameter()
        if condition:
            self._jump(destination)

    def _jump_if_false(self):
        condition = self._get_parameter()
        destination = self._get_parameter()
        if not condition:
            self._jump(destination)

    def _less_than(self):
        gliech = 1 if self._get_parameter() < self._get_parameter() else 0
        self._write_value(gliech)

    def _equals(self):
        gliech = 1 if self._get_parameter() == self._get_parameter() else 0
        self._write_value(gliech)

    def _exit(self):
        raise EndOfProgram

