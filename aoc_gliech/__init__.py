import importlib
import inspect
import re
import traceback
from aocd.get import current_day, get_data, most_recent_year
from pprint import pformat
from textwrap import indent
from time import perf_counter

def aocd_entrypoint(year, day, data):
    puzzle_module_name = f"aoc_gliech.y{year}.d{day:02d}"
    try:
        puzzle_solutions = importlib.import_module(puzzle_module_name)
    except ModuleNotFoundError as e:
        if e.name == puzzle_module_name:
            return None, None
        else:
            raise e
    return puzzle_solutions.part_a(data), puzzle_solutions.part_b(data)

def _get_calling_file_match(match):
    return int(match.group()) if match is not None else None

def solve(*funcs, day=None, year=None, data=None):
    if x is None:
        calling_file = inspect.stack()[1].filename
        year_exp, day_exp = ("{0}(?!.*{0}.*)".format(pattern) for pattern in (r"20\d\d", r"[12]\d"))
        year_match = re.search(year_exp, calling_file)
        calling_file = re.sub(year_exp, "XXXX", calling_file)
        day_match = re.search(day_exp, calling_file)
        year = year or _get_calling_file_match(year_match) or most_recent_year()
        day = day or _get_calling_file_match(day_match) or current_day()
        data = get_data(year=year, day=day)

    for idx, func in enumerate(funcs):
        func_name = f"Function {idx+1}" if (n:=getattr(func, "__name__", "<")).startswith("<") else n
        time_start = perf_counter()

        try:
            func_output = func(data)
        except Exception as e:
            func_output = e

        time = (perf_counter() - time_start) * 1000
        output_type = type(func_output)
        title = f"{func_name} [{time:.2f}ms] {output_type}:"

        if isinstance(func_output, str) and "\n" in func_output:
            pass
        elif isinstance(func_output, Exception):
            func_output = "".join(traceback.format_exception(func_output, limit=-1))
        else:
            func_output = pformat(func_output)

        if "\n" in func_output:
            print(f"{title}\n{indent(func_output, "  ")}")
        else:
            print(f"{title}  {func_output}")
