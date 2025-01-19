#!/usr/bin/env python3

while True:
    inp = input('>>> ')
    check = 0
    used = set()
    for c in inp:
        check ^= ord(c)
        if c in used:
            print("DRY!")
            exit()
        used |= {c}
    if check:
        print("Non-zero checksum!")
        exit()
    exec(inp)

