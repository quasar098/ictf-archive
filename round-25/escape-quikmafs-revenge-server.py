#!/usr/bin/env python3

from random import randint, choice, shuffle
from time import time
from itertools import product

# https://pypi.org/project/console/
from console.utils import wait_key, cls
from console.screen import Screen

def win():
    cls()
    with screen.location(0, 0):
        print(f"Great job! {open('flag.txt').read()}")

    with screen.location(2, 0):
        print("Press enter to exit.")

    input()
    exit(0)

def die(msg="Sorry, that's not correct."):
    cls()
    with screen.location(0, 0):
        print(msg)

    with screen.location(2, 0):
        print("Press enter to exit.")
    
    input()
    exit(1)

def draw(n1, n2, op):
    eq = "%d%s%d=?"%(n1, op, n2)
    ans = eval(eq[:-2])

    wall = '╔═╗╚║╝'
    
    to_print = []
    to_print.append(list('╔' + '═'*78 + '╗'))
    for i in range(18):
        to_print.append(list('║' + ' '*78 + '║'))
    to_print.append(list('╚' + '═'*78 + '╝'))
    to_print.append([' ']*80)
    to_print.append(list('>>>'+' '*77))

    for i in range(50):
        y = randint(1, 18)
        x = randint(1, 78)
        to_print[y][x] = choice('0123456789=?*-+^&|>')

    up = randint(0, 1)

    eq_x = randint(1, 78 - len(eq) - 1)
    if up:
        eq_y = randint(13, 18)
    else:
        eq_y = randint(1, 6)

    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    if up:
        offsets += [(-1, -1), (1, 1)]
    else:
        offsets += [(1, -1), (-1, 1)]

    offx = -1
    offy = -1 if up else 1
    if to_print[eq_y+offy][eq_x+offx] not in wall:
        to_print[eq_y+offy][eq_x+offx] = ' '

    for char in eq:
        to_print[eq_y][eq_x] = char
        for offx, offy in offsets:
            if to_print[eq_y+offy][eq_x+offx] not in wall:
                to_print[eq_y+offy][eq_x+offx] = ' '
        eq_x += 1
        eq_y += -1 if up else 1

    if to_print[eq_y][eq_x] not in wall:
        to_print[eq_y][eq_x] = ' '

    cls()

    coords = list(product(range(len(to_print)), range(80)))
    shuffle(coords)
    idx = 0
    while idx < len(coords):
        y, x = coords[idx]
        idx += 1
        with screen.location(y, x):
            real = randint(0, 1)
            if real:
                print(to_print[y][x], end='')
            else:
                print(choice('0123456789=?*-+^&|> '), end='')
                coords.append((y, x))
        if not real and x < 75 and not(randint(0,9)):
            with screen.location(y, x):
                print('>>> ')
                for i in range(1, 4):
                    coords.append((y, x+i))

    with screen.location(21, 4):
        user_ans = int(input())

    return ans == user_ans


def main():
    with screen.fullscreen():
        start = time()
        for i in range(100):
            n1 = randint(10000, 99999)
            n2 = randint(10000, 99999)
            op = choice('*-+^&|')
            if not draw(n1, n2, op):
                die()
            if time() - start > 200:
                die("Out of time!")
        win()

if __name__ == '__main__':
    with Screen(force=True) as screen:
        main()