#!/usr/bin/env python3

from itertools import chain

flag = open('flag.txt', 'rb').read().strip()
get_bits = lambda n: [int(i) for i in '{:08b}'.format(n)]
bits = list(chain(*[get_bits(i) for i in flag]))

def step(b):
    out = []
    for i in range(len(b)):
        out.append(b[(i-1)%len(b)] ^ b[(i+1)%len(b)])
    return out

f = open("future.txt", 'w')
for i in range(20):
    bits = step(bits)

for i in range(45):
    f.write(''.join(str(i) for i in bits)+ '\n')
    bits = step(bits)
