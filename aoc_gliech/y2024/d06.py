def prep(data):
    lab = {}
    for idx_x, line in enumerate(data.split("\n")):
        for idx_y, char in enumerate(line):
            coord = complex(idx_x, idx_y)
            lab[coord] = char
            if char == "^":
                position = coord
    return lab, position

def part_a(data):
    lab, position = prep(data)
    direction = -1
    visited = set()
    while True:
        visited.add(position)
        if position+direction not in lab:
            return len(visited)
        if lab[position+direction] == "#":
            direction *= -1j
        else:
            position += direction

def loop_detector(lab, position, direction, visited):
    while True:
        next_position = position+direction
        vector = (position, direction)
        if vector in visited:
            return True
        visited.add(vector)
        if next_position not in lab:
            return False
        if lab[next_position] == "#":
            direction *= -1j
        else:
            position += direction

def part_b(data):
    lab, position = prep(data)
    direction = -1
    visited = set()
    visited_coords = set()
    obstacles = set()
    while True:
        next_position = position+direction
        vector = (position, direction)
        if next_position not in lab:
            return len(obstacles)
        if lab[next_position] == "." and next_position not in visited_coords:
            lab[next_position] = "#"
            if loop_detector(lab, position, direction, visited.copy()):
                obstacles.add(next_position)
            lab[next_position] = "."
        visited.add(vector)
        visited_coords.add(position)
        if lab[next_position] == "#":
            direction *= -1j
        else:
            position += direction

example = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

if __name__ == "__main__":
    from aoc_gliech import solve
    solve(part_a, part_b, data=example)
