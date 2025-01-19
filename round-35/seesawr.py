#!/usr/bin/env python3

from random import randint

alphabet = bytes(range(32, 127))

def seesawr(s, key):
    if len(s) == 0:
        return b''
    return bytes([alphabet[(alphabet.index(s[0])+key) % len(alphabet)]]) + seesawr(s[:0:-1], key)

flag = open("flag.txt", "rb").read()

print(seesawr(flag, randint(0, 2**128)))

# Output:
# b'~3x|*${~1}^*tt{I~K$tv/"w"t/*tz{)~{.{z%ytty*(}~zzt-'
