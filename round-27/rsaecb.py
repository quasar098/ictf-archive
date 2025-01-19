#!/usr/bin/env python3

from Crypto.Util.number import *

p = getPrime(512)
q = getPrime(512)
n = p*q
e = 65537

m = open("flag.txt", 'rb').read()

out = open('output', 'wb')

out.write(long_to_bytes(n))

for c in m:
    out.write(long_to_bytes(pow(c, e, n)))
