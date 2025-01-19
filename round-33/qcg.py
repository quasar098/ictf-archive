#!/usr/bin/env python3

from random import randint

a = randint(0, 2**32 - 1) | 1
b = randint(0, 2**32 - 1) | 1
c = randint(0, 2**32 - 1) | 1
x = randint(0, 2**32 - 1) | 1

def get_next():
    global a, b, c, x
    x = (a*x**2 + b*x + c) % 2**32
    return x

flag = open("flag.txt", "rb").read()
ct = bytes((get_next()^c)%256 for c in flag)
print(ct)

# Output:
# b'\x12>\xd3gx\xb1\xbdx?#\x99\xdf\x0ck:\xf1o\xe2\xb3\x88\xceP\xb0\xb0\xcc\x01\xbb\x8e\x86\x16\x1a6\xfaQ\xab\x9e7\xfdj\x86\xe9\xa4\x83\xc2\xb2\xb8'
