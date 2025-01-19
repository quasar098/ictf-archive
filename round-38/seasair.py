#!/usr/bin/env python3

from random import randint
from math import sin, pi

def seasair(s, key):
    return bytes((c + k)%256 for c, k in zip(s, (int(256*sin(key*(i+1)/256*pi)) for i in range(len(s)))))

flag = open("flag.txt", 'rb').read()

key = randint(0, 2**32)

print(seasair(flag, key))

# Output:
# b"\xca\xae`fg\x94\x88d\xfe'ut|\x1a\x11_\xd4\xc2UmK\xb4\xcf_\x13\x1dy_\x87\x1a\x00_\xd5\xb3MnK\xbe\xd8i\x0c\x14}ns)\x07e\xc0\x8ei"
