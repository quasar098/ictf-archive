#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, getPrime

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 65537
m = bytes_to_long(open("flag.txt", "rb").read())
c = pow(m, e, n)

print(f'{c = }')
print(f'{e = }')
print(f'{n = }')
print(f'{n % e*p = }')