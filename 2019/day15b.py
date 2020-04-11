from aocd import get_data
from agc import AdventGuidanceComputer as agc
from curses_helper import curse, curse_attr
import curses
from random import randint
from time import sleep
from functools import partial

aoc_data = get_data(year=2019, day=15).split(',')
with curse(hide_cursor=True) as scr:

    dbg_h = 8
    scr_h, scr_w = scr.getmaxyx()

    main_container = scr.derwin(scr_h-dbg_h-2,scr_w,0,0)
    main_container.box()
    main_container.addstr(scr_h-dbg_h-3,scr_w-12,' Max:   0 ')
    main_container.addstr(scr_h-dbg_h-3,scr_w-23,' Cur:   0 ')
    print_max = partial(main_container.addstr, scr_h-dbg_h-3, scr_w-7)
    print_cur = partial(main_container.addstr, scr_h-dbg_h-3, scr_w-18)
    main_container.addch(scr_h-dbg_h-3,scr_w-23,curses.ACS_RTEE)
    main_container.addch(scr_h-dbg_h-3,scr_w-12,curses.ACS_RTEE)
    main_container.addch(scr_h-dbg_h-3,scr_w-14,curses.ACS_LTEE)
    main_container.addch(scr_h-dbg_h-3,scr_w-3,curses.ACS_LTEE)
    debug_container = scr.derwin(scr_h-dbg_h-2,0)
    debug_container.box()
    debug_win = debug_container.derwin(dbg_h,scr_w-4,1,2)
    scr.refresh()
    world_map = curses.newpad(5000,5000)
    scr_ul_y = 1
    scr_ul_x = 2
    scr_br_y = scr_h-dbg_h-4
    scr_br_x = scr_w-3
    pad_diff_y = (scr_br_y-scr_ul_y)//2
    pad_diff_x = (scr_br_x-scr_ul_x)//2

    robot_sprite = ('ʌ', 'v', '<', '>')
    next_direction = (3,2,0,1)
    movement_tuples = ((-1,0), (1,0), (0,-1), (0,1))
    tileset = [
        ['#', curse_attr(167)],
        ['.', curse_attr('light', 'black')],
        ['$', curse_attr(221, 'bold')]
    ]

    def draw_world():
        pad_ul_y = robot_position[0]-pad_diff_y
        pad_ul_x = robot_position[1]-pad_diff_x
        world_map.addch(*robot_position, robot_sprite[robot_direction])
        world_map.refresh(pad_ul_y, pad_ul_x,
                scr_ul_y, scr_ul_x, scr_br_y, scr_br_x)

    def next_tile():
        change = movement_tuples[robot_direction]
        return tuple(map(sum,zip(robot_position,change)))

    def manual_move():
        global robot_direction
        direction = None
        while direction is None:
            char = scr.getch()
            if char == curses.KEY_UP:
                direction = 0
            elif char == curses.KEY_DOWN:
                direction = 1
            elif char == curses.KEY_LEFT:
                direction = 2
            elif char == curses.KEY_RIGHT:
                direction = 3
            elif char == ord('q'):
                raise StopIteration
        robot_direction = direction
        return direction+1

    def random_move():
        global robot_direction
        sleep(0.1)
        robot_direction = randint(0, 3)
        return robot_direction+1

    def simple_move():
        global robot_direction
        sleep(0.04)
        if last_status == 0:
            robot_direction = next_direction[robot_direction]
        else:
            robot_direction = next_direction.index(robot_direction)
        return robot_direction+1

    def reset_distance():
        global distance, max_distance, known_positions
        distance = 0
        max_distance = 0
        known_positions = {robot_position:0}

    robot = agc(aoc_data, simple_move, debug_win)
    robot_direction = 0
    robot_position = (2500,2500)
    robot_tile = 1
    last_status = 1
    found_oxygen = False
    reset_distance()
    draw_world()

    for status in iter(robot):
        last_status = status
        if status == 0:
            world_map.addch(*next_tile(), *tileset[0])
        else:
            world_map.addch(*robot_position, *tileset[robot_tile])
            robot_position = next_tile()
            robot_tile = status
            if robot_position in known_positions:
                distance = known_positions[robot_position]
            else:
                distance += 1
                known_positions[robot_position] = distance
                if found_oxygen and distance>max_distance:
                    max_distance = distance
                    print_max(f'{max_distance:4}')
            print_cur(f'{distance:4}')
            main_container.refresh()
        draw_world()
        if status == 2:
            sleep(5)
            if not found_oxygen:
                found_oxygen = True
                reset_distance()
                tileset[1][0] = 'o'
            else:
                break
print(max_distance)

