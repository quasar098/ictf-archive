#!/usr/bin/env python3

from re import fullmatch
from time import time
from random import choice

clear = '\x1b\x5b\x48\x1b\x5b\x32\x4a\x1b\x5b\x33\x4a'

def die(*args):
    print(*args)
    exit()

def gen_word(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(choice(alphabet) for i in range(n))

def puzzle(n):
    accept = [gen_word(10) for i in range(5)]
    reject = [gen_word(10) for i in range(5)]
    print(clear, end='')
    print('='*80)
    print(f'** Regex #{n} **\n')
    print('Please match:')
    for word in accept:
        print(f' - {word}')
    print("But not:")
    for word in reject:
        print(f' - {word}')
    rx = input("Enter a regex:\n>>> ")
    for word in accept:
        if fullmatch(rx, word) is None:
            die(f"Regex error! Did not match the word {word}!")
    for word in reject:
        if fullmatch(rx, word) is not None:
            die(f"Regex error! Matched the word {word}!")

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