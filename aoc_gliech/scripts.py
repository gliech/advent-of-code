from aocd.get import current_day, most_recent_year
from docopt import docopt
from importlib.metadata import version
from pathlib import Path
from textwrap import dedent

aoc_file = """\
def prep(data):
    return data.split("\\n")

def part_a(data):
    return prep(data)

def part_b(data):
    return None

if __name__ == "__main__":
    from aoc_gliech import solve
    solve(part_a, part_b)
"""

def create_day_file():
    """
    Create a new file to solve advent of code.

    Usage:
        aoc-scaffold [--day=<number>] [--year=<number>]
        aoc-scaffold (-h | --help)
        aoc-scaffold --version

    Options:
        -d, --day=<number>   Day for the file path and templating values.
        -y, --year=<number>  Year for the file path and templating values.
        --version            Show version info.
        -h --help            Show this help screen.
    """

    arguments = docopt(dedent(create_day_file.__doc__), version=version("advent-of-code-gliech"))
    year = int(arguments.year or most_recent_year())
    day = int(arguments.day or current_day())
    file_path = Path(__file__).parent / f"y{year}" / f"d{day:02d}.py"
    if file_path.exists():
        raise FileExistsError(f"File {file_path} already exists")
    file_path.write_text(aoc_file)
    print(f"Created file at {file_path}")
