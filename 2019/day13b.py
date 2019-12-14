from aocd import get_data
from agc import AdventGuidanceComputer, EndOfProgram
from blessed import Terminal
from time import sleep

aoc_data = get_data(year=2019, day=13).split(',')
aoc_data[0]=2
term = Terminal()
score = 0
ball = 0
paddle = 0

def manual_joystick():
    with term.cbreak():
        key=''
        while key !='q':
            key = term.inkey().name
            if key=='KEY_LEFT':
                yield -1
            elif key=='KEY_RIGHT':
                yield 1
            elif key=='KEY_DOWN':
                yield 0

def auto_joystick():
    while True:
        sleep(0.01)
        diff = ball-paddle
        output = diff//abs(diff) if diff!=0 else diff
        print(term.move(term.height-8,0))
        print(f'Ball:   {ball:2}')
        print(f'Paddle: {paddle:2}')
        print(f'Move:   {output:2}')
        yield output

tileset = (
        ' ',
        '█',
        term.yellow('▣'),
        '━',
        term.bright_red('◉')
        )
arcade = AdventGuidanceComputer(aoc_data)(inputs=auto_joystick(),silent=True)

with term.fullscreen():
    with term.hidden_cursor():
        try:
            while True:
                x = next(arcade)
                y = next(arcade)
                tile = next(arcade)
                if x==-1 and y==0:
                    score = tile
                    print(term.move(term.height-2,0)+'Score: '+str(tile))
                else:
                    if tile==3:
                        paddle=x
                    elif tile==4:
                        ball=x
                    print(term.move(y,x)+tileset[tile])
        except EndOfProgram:
            with term.raw():
                term.inkey()
print(score)


# import code
# code.interact(local=locals())

