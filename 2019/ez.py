import curses
import blessings
from curses_helper import curse, curse_attr
from time import sleep
t = blessings.Terminal()

def init_default_pairs():
    curses.use_default_colors()
    for color in range(16):
        curses.init_pair(color+300,color,-1)

def main(scr):
    init_default_pairs()
    scr.scrollok(True)
    for _ in range(1):
        for i in range(300, 316):
            scr.addstr(f'test {i:2} ',i<<8)
            scr.addstr(f'{i<<8:b}\n')
            scr.refresh()
            sleep(0.05)
    scr.addstr(f'         {curses.COLOR_PAIRS:b}\n')

    curses.init_pair(25,1,0)
    scr.addstr(f'{curses.pair_content(26)}',curses.color_pair(25)|1)
    scr.refresh()
    scr.getch()
# curses.wrapper(main)

with curse() as scr:
    curses.curs_set(0)
    maxy,maxx = scr.getmaxyx()
    arcade_height = 20
    arcade_width = 25
    arcade_output = scr.subwin(arcade_height,maxx,0,0)
    arcade_output.bkgd('.', curse_attr('green'))
    arcade_output.border(0,' ',' ',' ')
    debug_screen = scr.subwin(arcade_height,0)
    debug_screen.box(0,' ')

    scr.getch()
