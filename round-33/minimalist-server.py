#!/usr/bin/env python3

from Crypto.Util.number import getStrongPrime
from hashlib import sha256
from random import randint

print("Starting...")
p = getStrongPrime(1024)
g = 2
x = randint(1, p - 2)
y = pow(g, x, p)

print("Here's a public key:")
print(f"{p = }")
print(f"{g = }")
print(f"{y = }")

print("Sign a message to get the flag!")
msg = input("Message (in hex): ")
r = int(input("r: "))
s = int(input("s: "))

def hashfn(m):
    return int(sha256(m).hexdigest()[:12], 16)

ghm = pow(g, hashfn(bytes.fromhex(msg)), p)
yrrs = (pow(y, r, p) * pow(r, s, p)) % p

if ghm % p == yrrs % p:
    print("Well done!")
    print(open("flag.txt").read())
else:
    print("Signature verfication failed...")


