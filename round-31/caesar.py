#!/usr/bin/env python3

from random import randint

alphabet = bytes(range(32, 127))

caesar = lambda s, key: bytes(alphabet[(c+key+s[(i-1)%len(s)])%len(alphabet)] for i, c in enumerate(s))

flag = open("flag.txt", "rb").read()

print(caesar(flag, randint(0,2**32)))

# Output:
# b">$/294'*z'-,74){,@0{+4)4*+;&$&$({,;/5E0} &*0is"