#!/usr/bin/env python3

import os
from random import randint
from itertools import chain

from PIL import Image

iters = randint(0, 1000)
i = 0
secret = randint(1, iters-1)
print(secret, iters)
flag = open('flag.txt', 'rb').read()
get_bits = lambda n: [int(i) for i in '{:08b}'.format(n)]
bits = list(chain(*[get_bits(i) for i in flag]))

path = 'fake.png'
while i < iters:
    with Image.open(path) as image:
        dim = width, height = image.size
        with Image.new(image.mode, dim) as canvas:
            for x in range(width):
                for y in range(height):
                    nx = (2 * x + y) % width
                    ny = (1 * x + y) % height
                    px = list(image.getpixel((x, height-y-1)))

                    if i == secret and len(bits):
                        px[2] = ((px[2] >> 1) << 1) + bits[0]
                        bits = bits[1:]
                    canvas.putpixel((nx, (height-ny-1)), tuple(px))
    # os.remove(path)
    i += 1
    path = 'flag.png' if i == iters else 'files/source{:}.png'.format(i)
    print(i, end="\r")
    canvas.save(path)
