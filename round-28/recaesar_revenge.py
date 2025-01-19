#!/usr/bin/env python3

from random import randint
import sys

alphabet = bytes(range(10, 128))

block_size = 16

def caesar(plaintext, key):
    ret = [alphabet[(plaintext[i] + key[i] - 10)%len(alphabet)] for i in range(block_size)]
    if len(plaintext) > block_size:
           ret += caesar(plaintext[block_size:], caesar(key, key))
    return ret

if __name__ == '__main__':
    sys.setrecursionlimit(2**31 - 1)

    flag = open("flag.txt").read()
    assert all(ord(i) in alphabet for i in flag)
    key = [randint(0, 2**128) for i in range(block_size)]
    out = open("output.txt", "wb")
    # flag = 'a'*block_size
    while len(flag) % block_size:
        flag += '\n'
    out.write(bytes(caesar(flag.encode(), key)))

