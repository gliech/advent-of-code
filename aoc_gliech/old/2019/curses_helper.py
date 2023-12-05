import curses
from contextlib import contextmanager

def curse_attr(*args):
    color = 0
    attr = 0
    for arg in set(args):
        if type(arg) is int:
            color=arg
        elif arg == 'light':
            color+=8
        elif f'COLOR_{arg.upper()}' in dir(curses):
            color+=getattr(curses, f'COLOR_{arg.upper()}')+1
        elif f'A_{arg.upper()}' in dir(curses):
            attr|=getattr(curses, f'A_{arg.upper()}')
        else:
            raise ValueError(f'Could not interpret {arg} as curses attribute.')
    if curses.pair_content(color) == (0,0):
        curses.init_pair(color, color-1, -1)
    return attr|curses.color_pair(color)

@contextmanager
def curse(noecho=True, cbreak=True, keypad=True, hide_cursor=False):
    try:
        stdscr = curses.initscr()
        if noecho:
            curses.noecho()
        if cbreak:
            curses.noecho()
        if keypad:
            stdscr.keypad(True)
        if hide_cursor:
            curses.curs_set(0)
        try:
            curses.start_color()
            curses.use_default_colors()
        except:
            pass
        yield stdscr
    finally:
        if 'stdscr' in locals():
            if keypad:
                stdscr.keypad(False)
            if noecho:
                curses.echo()
            if cbreak:
                curses.nocbreak()
            curses.endwin()
