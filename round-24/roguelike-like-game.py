#!/usr/bin/env python3

from copy import deepcopy
from os import urandom

# https://pypi.org/project/console/
from console.utils import wait_key
from console.screen import Screen

rng_state = 0
player_x = 0
player_y = 0
level = 1
levels = []
last_key_pressed = '\0'
current_map = []
current_display = []
screen = None
descended = 0

SOLID = '╔║╗╚═╝0'
LETHAL = '^'

tile_names = {
    '0': 'boulder',
    '/': 'wand',
    '*': 'rock',
    '_': 'altar',
    '^': 'spike trap',
    '1': 'spike trap reloading',
    '2': 'spike trap reloading',
    '3': 'spike trap reloading',
    '4': 'spike trap reloading',
    '>': 'stairs down',
    '<': 'stairs up',
}

def rng():
    global rng_state
    if rng_state == 0x560A:
        rng_state = 0
    s0 = (rng_state << 8) & 0xFFFF
    s0 = s0 ^ rng_state
    rng_state = ((s0 & 0xFF) << 8) | ((s0 & 0xFF00)>>8)
    s0 = (((s0 & 0xFF) << 1) ^ rng_state)
    s1 = (s0 >> 1) ^ 0xFF80
    if (s0 & 1) == 0:
        if s1 == 0xAA55:
            rng_state = 0
        else:
            rng_state = s1 ^ 0x1FF4
    else:
        rng_state = s1 ^ 0x8180
    return rng_state

def update_world():
    global current_map, current_display
    for y in range(20):
        for x in range(80):
            for arr in current_map, current_display:
                if arr[y][x] in '234':
                    arr[y][x] = str(int(arr[y][x])-1)
                elif arr[y][x] in '1':
                    arr[y][x] = '^'
                elif arr[y][x] in '^':
                    arr[y][x] = '4'

def move_player(y, x):
    global player_x, player_y
    temp_y = player_y + y
    temp_x = player_x + x
    if temp_x < 1:
        temp_x = 1
    if temp_x > 79:
        temp_x = 79
    if temp_y < 1:
        temp_y = 1
    if temp_y > 19:
        temp_y = 19
    test_move = current_map[temp_y][temp_x]
    if test_move in SOLID:
        return
    if test_move in LETHAL:
        see(test_move)
        die()
    player_x = temp_x
    player_y = temp_y

def descend():
    global level, descended
    if current_map[player_y][player_x] != '>':
        move_player(0, 0)
        return
    descended = 1
    level += 1
    levels[level-1]()


def process_input(key):
    if key == chr(3):
        print("Ctrl-C")
        exit()
    elif key in ['8', '\x1b[A']:
        move_player(-1, 0)
    elif key in ['2', '\x1b[B']:
        move_player(1, 0)
    elif key in ['6', '\x1b[C']:
        move_player(0, 1)
    elif key in ['4', '\x1b[D']:
        move_player(0, -1)
    elif key in '7':
        move_player(-1, -1)
    elif key in '9':
        move_player(-1, 1)
    elif key in '1':
        move_player(1, -1)
    elif key in '3':
        move_player(1, 1)
    elif key in '>':
        descend()
    else:
        move_player(0, 0)
        return # do nothing

def see(c):
    global level
    if level == 2:
        status_message("It's so dark... you can't see a thing!")
        return
    if c not in tile_names:
        status_message('')
        return
    name = tile_names[c]
    status_message(f"You see here a{'n' if name[0] in 'aeiou' else ''} {name}{'!' if c == '^' else '.'}")

def draw():
    print(screen.clear, end='')
    for y in range(20):
        with screen.location(y, 0):
            print(''.join(current_display[y]), end='')
    with screen.location(20, 0):
        print(f"Level {level}                                                    Press Ctrl+C to exit.", end='')
    see(current_display[player_y][player_x])
    with screen.location(player_y, player_x):
        print('@', end='')

def level1():
    global current_map, current_display, player_x, player_y, level
    tiles = [' ']*10 + list(tile_names.keys())

    current_map = [[] for i in range(20)]
    current_map[0] = list('╔' + '═'*78 + '╗')
    for i in range(1, 19):
        current_map[i] = ['║'] + [tiles[rng()%(len(tiles)-2)] for i in range(78)] + ['║']
    current_map[-1] = list('╚' + '═'*78 + '╝')
    current_map[1][1] = ' '
    current_map[-2][-2] = '>'
    current_display = deepcopy(current_map)
    player_y = 1
    player_x = 1
    level = 1

def level2():
    global current_map, current_display, player_x, player_y, level
    tiles = '^1234'

    current_map = [[] for i in range(20)]
    current_map[0] = list('╔' + '═'*78 + '╗')
    for i in range(1, 19):
        current_map[i] = ['║'] + [tiles[rng()%(len(tiles))] for i in range(78)] + ['║']
    current_map[-1] = list('╚' + '═'*78 + '╝')
    current_map[1][1] = ' '
    current_map[-2][-2] = '>'

    current_display = [[] for i in range(20)]
    current_display[0] = list('╔' + '═'*78 + '╗')
    for i in range(1, 19):
        current_display[i] = ['║'] + [' ']*78 + ['║']
    current_display[-1] = list('╚' + '═'*78 + '╝')
    current_display[1][1] = ' '
    current_display[-2][-2] = '>'
    current_display = deepcopy(current_map)
    player_y = 1
    player_x = 1
    level = 2

def level3():
    global current_map, current_display, player_x, player_y, level

    current_map = [[] for i in range(20)]
    current_map[0] = list('╔' + '═'*78 + '╗')
    for i in range(1, 19):
        current_map[i] = ['║'] + [' ']*78 + ['║']
    current_map[-1] = list('╚' + '═'*78 + '╝')

    current_display = deepcopy(current_map)
    current_display[10] = ['║'] + list(open('flag.txt').read()) + ['║']
    player_y = 1
    player_x = 1
    level = 3


def status_message(msg, line=21):
    with screen.location(line, 0):
        print(msg+' '*(80-len(msg)), end='')

def die():
    status_message("You have died... Press any key to exit.", 22)
    wait_key()
    exit()

def setup():
    global levels
    for i in range(urandom(1)[0]):
        for j in range(urandom(1)[0]):
            rng() # scramble initial RNG state

    screen = Screen()
    levels = [level1, level2, level3]
    level = 1
    levels[level-1]()

def main():
    global last_key_pressed, descended
    with screen.fullscreen():
        while 1:
            draw()
            with screen.location(player_y, player_x):
                key = wait_key()
                if key == '\x1b':
                    for _ in range(2):
                        key += wait_key()
                last_key_pressed = key
            process_input(key)
            if descended:
                descended = 0
            else:
                update_world()

if __name__ == '__main__':
    with Screen(force=True) as screen:
        setup()
        main()
