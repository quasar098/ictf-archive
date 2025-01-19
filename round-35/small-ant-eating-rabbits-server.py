#!/usr/bin/env python3

from Crypto.Util.number import *
from SECRET import FLAG

def get(num):
    while True:
        p = getPrime(num)
        if p % 4 == 3:
            return p

p,q = get(512),get(512)
n = p*q

m = bytes_to_long(FLAG)
e = 2
c = pow(m,e,n)

print(f"e = {e}\nn = {n}\nc = {c}")
