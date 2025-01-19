#!/usr/bin/env python

import hashlib

with open('flag.txt', 'rb') as f:
    flag = f.read()

for char in flag:
    print(hashlib.sha256(bytes(char)).hexdigest()[:4])
