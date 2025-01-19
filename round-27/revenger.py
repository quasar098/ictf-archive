#!/usr/bin/env python3

from re import fullmatch
from time import time
from random import choice
from solver import magic_regex_generator

clear = '\x1b\x5b\x48\x1b\x5b\x32\x4a\x1b\x5b\x33\x4a'

def die(*args):
    print(*args)
    exit()

def gen_word(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(choice(alphabet) for i in range(n))

def puzzle(n):
    num_words = 5 if n <= 3 else 1000
    accept = [gen_word(10) for i in range(num_words)]
    reject = [gen_word(10) for i in range(num_words)]
    print(clear, end='')
    print('='*80)
    print(f'** Regex #{n} **\n')
    print('Please match:')
    print(accept)
    print()
    print("But not:")
    print(reject)
    print()
    print("Generating proof regex...")
    magic_rx = magic_regex_generator(accept, reject)
    rx = input(f"Enter a regex with at most {len(magic_rx)} characters:\n>>> ")
    for word in accept:
        if fullmatch(magic_rx, word) is None: # proof the regex actually works
            die(accept, reject, word, "Wow, puzzler7 is bad at coding. Please DM him with this entire line.")
        if fullmatch(rx, word) is None:
            die(f"Regex error! Did not match the word {word}!")
    for word in reject:
        if fullmatch(magic_rx, word) is not None: # proof the regex actually works
            die(accept, reject, word, "Wow, puzzler7 is bad at coding. Please DM him with this entire line.")
        if fullmatch(rx, word) is not None:
            die(f"Regex error! Matched the word {word}!")
    if len(rx) > len(magic_rx):
        die(f"Regex too long! Your regex was {len(rx)} chars long, and needed to be at most {len(magic_rx)} chars!")

def main():
    solved = 0
    start = time()
    while solved < 100:
        solved += 1
        puzzle(solved)
        if time() - start > 300:
            die("Out of time!")
    die(f"Congrats! {open('flag.txt').read()}")


if __name__ == '__main__':
    main()