#!/usr/bin/env python3

from Crypto.Util.number import *

flag = open('flag.txt', 'rb').read()
m = bytes_to_long(flag)

p = getPrime(512)
q = getPrime(512)
r = getPrime(512)
s = getPrime(512)
t = getPrime(512)

n = p*q*r*s*t

e = 65537

c = pow(m, e, n)

print(f"{c = }")
print(f"{n = }")
print(f"{e = }")
print(f"{q = }")
print(f"{r = }")
print(f"{s = }")
print(f"{t = }")
