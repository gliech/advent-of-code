from collections import defaultdict
from functools import partial
from time import sleep
from curses_helper import curse_attr

class EndOfProgram(Exception):
    pass

class AdventGuidanceComputer:
    def __init__(self, program, inputs=[], window=None, delay=0):
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
        self._program = tuple(map(int,program))
        self._input_source = inputs
        self._delay = delay
        self._window = window
        if window is None:
            self._prt = self._no_print
        else:
            self._window.scrollok(True)
            self._prt = self._print_to_window
            self._curses_attrs = {
                'position': curse_attr(221),
                'rbase': curse_attr(167),
                'command': curse_attr('blue', 'light', 'bold'),
                'default': curse_attr('light', 'white'),
                'write': curse_attr('light', 'white', 'bold'),
                'muted': curse_attr('light', 'black')
            }

    def __iter__(self):
        self._memory = defaultdict(partial(int,0),enumerate(self._program))
        self._position = 0
        self._relative_base = 0
        self._mode_ints = 0
        if callable(self._input_source):
            self._get_input = self._input_source
        else:
            self._input_iterator = iter(self._input_source)
            self._get_input = self._next_input
        return self

    def __next__(self):
        output = None
        while output is None:
            try:
                self._prt('\n')
                output = self.execute_instruction()
            except EndOfProgram as e:
                raise StopIteration
            finally:
                if self._window is not None:
                    sleep(self._delay)
                    self._window.refresh()
        return output

    def _print_to_window(self, message, attr_name='default'):
        self._window.addstr(message, self._curses_attrs[attr_name])

    def _no_print(self, *args, **kwargs):
        pass

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

    def _next_input(self):
        return next(self._input_iterator)

    def _increment(self):
        value = self._memory[self._position]
        self._position+=1
        return value

    def _jump(self, destination):
        self._position = destination

    def execute_instruction(self):
        self._prt(f'{self._fmt_int(self._position, 4)} ', 'position')
        self._prt(f'{self._fmt_int(self._relative_base, 4)}: ', 'rbase')
        instruction = self._increment()
        opcode = instruction%100
        self._mode_ints = instruction//100
        function = self._instruction_set[opcode]
        self._prt(f'{function.__name__[1:]:>7} ', 'command')
        self._prt(self._fmt_int(instruction, 5), 'muted')
        return function()

    def _get_addr(self):
        mode = self._mode_ints%10
        self._mode_ints //= 10
        parameter = self._increment()
        self._prt('  ')
        addr = self._parameter_modes[mode](parameter)
        return addr

    def _read_value(self):
        addr = self._get_addr()
        value = self._memory[addr]
        self._prt('>', 'muted')
        self._prt(self._fmt_int(value, 7))
        return value

    def _write_value(self, value):
        addr = self._get_addr()
        self._memory[addr] = value
        self._prt('<', 'muted')
        self._prt(self._fmt_int(value, 7), 'write')

    def _relative_mode(self, parameter):
        addr = parameter+self._relative_base
        self._prt(self._fmt_int(addr, 4), 'rbase')
        return addr

    def _position_mode(self, parameter):
        addr = parameter
        self._prt(self._fmt_int(addr, 4), 'position')
        return addr

    def _direct_mode(self, parameter):
        addr = self._position-1
        self._prt('self')
        return addr

    def _add(self):
        new_value = self._read_value()+self._read_value()
        self._write_value(new_value)

    def _mul(self):
        new_value = self._read_value()*self._read_value()
        self._write_value(new_value)

    def _input(self):
        self._write_value(self._get_input())

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
        self._position-=1
        raise EndOfProgram

