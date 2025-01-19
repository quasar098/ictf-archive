#!/usr/bin/env python3

from itertools import product
from PIL import Image
from random import shuffle

combine = lambda a,b: (a[0]+b[0], a[1]+b[1])

im = Image.open("logo.png")

flag = open("flag.txt", "rb").read()
locs = list(product(range(0, 256, 2), repeat=2))[::-1]
current_loc = locs.pop()
shuffle(locs)
for char in flag:
    x, y = locs.pop()
    deltas = [(0,0), (0, 1), (1,0), (1, 1)]
    data = [
        (char >> 6, (char >> 4)&3, (char >> 2)&3),
        (char&3, x >> 6, (x >> 4)&3),
        ((x>>2)&3, x&3, y >> 6),
        ((y>>4)&3, (y>>2)&3, y&3),
    ]

    for i in range(4):
        px_loc = combine(current_loc, deltas[i])
        px = im.getpixel(px_loc)
        new_px = tuple((px[j]&0xfc) | data[i][j] for j in range(3))
        im.putpixel(px_loc, new_px)

    current_loc = (x, y)
    

im.save("flag.png", format='PNG')