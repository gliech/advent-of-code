from aocd import get_data
from agc import AdventGuidanceComputer as agc
from curses_helper import curse, curse_attr
import curses
from random import randint
from time import sleep
from functools import partial

aoc_data = get_data(year=2019, day=17).split(',')
with curse(hide_cursor=True) as scr:

    dbg_h = 5
    scr_h, scr_w = scr.getmaxyx()

    main_container = scr.derwin(scr_h-dbg_h-2,scr_w,0,0)
    main_container.box()
    debug_container = scr.derwin(scr_h-dbg_h-2,0)
    debug_container.box()
    debug_win = debug_container.derwin(dbg_h,scr_w-4,1,2)
    scr.refresh()
    world_size_y = 100
    world_size_x = 100
    world_map = curses.newpad(world_size_y, world_size_x)
    cam_ul_y = 1
    cam_ul_x = 2
    cam_br_y = scr_h-dbg_h-4
    cam_br_x = scr_w-3
    cam_size_y = cam_br_y-cam_ul_y
    cam_size_x = cam_br_x-cam_ul_x

    def draw_world(y,x):
        pad_ul_y = y-cam_size_y//2
        pad_ul_x = x-cam_size_x//2
        world_map.refresh(pad_ul_y, pad_ul_x,
                cam_ul_y, cam_ul_x, cam_br_y, cam_br_x)

    def ascii_prog():
        #       12345678901234567890
        main = 'A,B,A,C,B,C,A,B,A,C'
        mova = 'R,10,L,8,R,10,R,4'
        movb = 'L,6,L,6,R,10'
        movc = 'L,6,R,12,R,12,R,10'
        view = 'y'
        for function in (main, mova, movb, movc, view):
            for char in list(function):
                yield ord(char)
            yield ord('\n')

    aoc_data[0] = 2
    aftscii = agc(aoc_data, ascii_prog())
    stream_pos = [0,0]
    last_char = 0
    player_character = (ord('^'), ord('v'), ord('>'), ord('<'))
    player_pos = [0,0]
    for character in iter(aftscii):
        if character == 10:
            if last_char == 10:
                stream_pos=[0,0]
                draw_world(0,0)
            else:
                stream_pos[0]+=1
                stream_pos[1]=0
        else:
            world_map.addch(*stream_pos, character)
            if character in player_character:
                player_pos = tuple(stream_pos)
            stream_pos[1]+=1
        last_char = character
    debug_win.addstr(str(last_char))
    debug_win.refresh()
    scr.getch()

