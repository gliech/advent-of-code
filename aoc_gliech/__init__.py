import importlib

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
