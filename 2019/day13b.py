from aocd import get_data
from agc import AdventGuidanceComputer
from curses_helper import curse, curse_attr
from time import sleep

aoc_data = get_data(year=2019, day=13).split(',')
aoc_data[0]=2
score = 0
ball = 0
paddle = 0

def auto_joystick(window):
    def joy():
        sleep(0.01)
        diff = ball-paddle
        output = diff//abs(diff) if diff!=0 else diff
        window.addstr(0,0, f'Ball:   {ball:4}')
        window.addstr(1,0, f'Paddle: {paddle:4}')
        window.addstr(2,0, f'Move:   {output:4}')
        window.refresh()
        return output
    return joy

with curse(hide_cursor=True) as scr:
    arcade_h = 25
    arcade_w = 41

    tileset = (
        (' ',),
        ('#', curse_attr('light','black')),
        ('▣', curse_attr('yellow')),
        ('━',),
        ('◉', curse_attr('light', 'red'))
        )

    scr_h, scr_w = scr.getmaxyx()
    main_container = scr.derwin(arcade_h+2,scr_w,0,0)
    arcade_container = main_container.derwin(arcade_h+2,arcade_w+4,0,0)
    arcade_container.box()
    arcade_scr = arcade_container.derwin(arcade_h+1,arcade_w,1,2)
    score_win = main_container.derwin(4,14,arcade_h-3,arcade_w+5)

    debug_container = scr.derwin(arcade_h+2,0)
    dbg_h, dbg_w = debug_container.getmaxyx()
    debug_container.box()
    debug_win = debug_container.derwin(dbg_h-2,dbg_w-4,1,2)
    scr.refresh()

    joystick = auto_joystick(score_win)
    arcade = iter(AdventGuidanceComputer(aoc_data, joystick, debug_win))


    try:
        while True:
            x = next(arcade)
            y = next(arcade)
            tile = next(arcade)
            if x==-1 and y==0:
                score = tile
                score_win.addstr(3,0, f'Score: {score:5}')
                score_win.refresh()
            else:
                if tile==3:
                    paddle=x
                elif tile==4:
                    ball=x
                arcade_scr.addch(y,x,*tileset[tile])
                arcade_scr.refresh()
    except StopIteration:
        scr.getch()
print(score)


# import code
# code.interact(local=locals())
