#!/usr/bin/env python3

from re import fullmatch
from time import time
from random import choice, randint

clear = '\x1b\x5b\x48\x1b\x5b\x32\x4a\x1b\x5b\x33\x4a'

def die(*args):
    print(*args)
    exit()

def gen_entity():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return '[' + ''.join(choice(alphabet) for i in range(randint(2, 8))) + ']'

def gen_length():
    length = randint(1, 10)
    if length == 1:
        return ""
    else:
        return f"{{{length}}}"

def gen_regex():
    length = randint(2, 5)
    return ''.join(gen_entity()+gen_length() for _ in range(length))

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