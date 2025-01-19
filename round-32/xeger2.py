#!/usr/bin/env python3

from regex import fullmatch, escape
from time import time
from random import choice, randint
from string import printable

clear = '\x1b\x5b\x48\x1b\x5b\x32\x4a\x1b\x5b\x33\x4a'
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'*+,-./:;<=>?@[\\]^_`{|}~'

def die(*args):
    print(*args)
    exit()

def gen_base():
    return escape(''.join(choice(alphabet) for i in range(randint(2, 8))))

def gen_entity(groups = 0):
    children = []
    start_groups = groups
    while len(children) < 1 or randint(0, 1):
        insert_group = 0
        match randint(1, 3):
            case 1:
                ent, new_groups = gen_entity(start_groups)
                children.append(ent)
                groups = new_groups
            case 2:
                children.append(gen_base())
            case 3:
                if start_groups > 0:
                    children.append(f'\\{randint(1, start_groups)}')
                    insert_group = 1
                else:
                    children.append(gen_base())
        match randint(0, 4):
            case 1:
                children[-1] = f'({children[-1]})'
                groups += 1
            case 2:
                children[-1] = f'(?>{children[-1]})'
            case 3:
                if not insert_group:
                    children[-1] = f'(?={children[-1]}){children[-1]}'
            case 4:
                if not insert_group:
                    children[-1] = f'{children[-1]}(?<={children[-1]})'
    return ''.join(children), groups

def gen_regex():
    length = randint(3, 6)
    regex = ''
    groups = 0
    for i in range(length):
        ent, groups = gen_entity(groups)
        regex += ent
    return regex

def puzzle(n):
    rx = gen_regex()
    print(clear, end='')
    print('='*80)
    print(f'** Regex #{n} **\n')
    print('Please generate a string to match the regex:')
    print(f'\t{rx}\n')
    inp = input("Enter string:\n>>> ")
    if fullmatch(rx, inp) is None:
        die("Input did not match!")

def main():
    solved = 0
    start = time()
    while solved < 100:
        solved += 1
        puzzle(solved)
        if time() - start > 180:
            die("Out of time!")
    die(f"Congrats! {open('flag.txt').read()}")


if __name__ == '__main__':
    main()
