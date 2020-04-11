from aocd import get_data
from agc import AdventGuidanceComputer as agc
from curses_helper import curse, curse_attr
import curses
from random import randint
from time import sleep
from functools import partial

aoc_data = get_data(year=2019, day=17).split(',')
with curse(hide_cursor=True) as scr:

    dbg_h = 8
    scr_h, scr_w = scr.getmaxyx()

    main_container = scr.derwin(scr_h-dbg_h-2,scr_w,0,0)
    main_container.box()
    debug_container = scr.derwin(scr_h-dbg_h-2,0)
    debug_container.box()
    debug_win = debug_container.derwin(dbg_h,scr_w-4,1,2)
    scr.refresh()
    world_size_y = 48
    world_size_x = 51
    world_map = curses.newpad(world_size_y, world_size_x)
    cam_ul_y = 1
    cam_ul_x = 2
    cam_br_y = scr_h-dbg_h-4
    cam_br_x = scr_w-3
    cam_size_y = cam_br_y-cam_ul_y
    cam_size_x = cam_br_x-cam_ul_x

    def draw_world(y,x):
        pad_ul_y = max(0,min(y-cam_size_y//2,world_size_y-cam_size_y))
        pad_ul_x = max(0,min(x-cam_size_x//2,world_size_x-cam_size_x))
        world_map.refresh(pad_ul_y, pad_ul_x,
                cam_ul_y, cam_ul_x, cam_br_y, cam_br_x)

    aftscii = agc(aoc_data, [], debug_win)
    world = {}
    stream_pos = [0,0]

    for character in iter(aftscii):
        if character == 10:
            stream_pos[0]+=1
            stream_pos[1]=0
        else:
            world[complex(*stream_pos)]=character
            world_map.addch(*stream_pos, character)
            draw_world(0,0)
            stream_pos[1]+=1
    scr.getch()

neighbours = (complex(0,1), complex(1,0), complex(0,-1), complex(-1,0))

def crossing(coord):
    if world[coord] != 35:
        return 0
    for neighbour in map(lambda x: x+coord, neighbours):
        if neighbour not in world or world[neighbour]!=35:
            return 0
    else:
        return coord.real*coord.imag

print(int(sum(map(crossing,world))))
