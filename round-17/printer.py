#!/usr/bin/env -S python3 -u

import time
from secret import flag

win_size = 20
linewidth = 80
colnum = 1

def fake_mod(a, b):
    return ((a-1)%b)+1

def print_loop(s, size=win_size):
    global colnum
    for c in s:
        print(f"\x1b[{colnum}G{c}", end='')
        colnum = fake_mod(colnum + 1,linewidth)

def delete_last(sz):
    global colnum
    colnum = fake_mod(colnum-sz, linewidth)
    print(f"\x1b[{colnum}G ", end='')
    colnum = fake_mod(colnum + 1,linewidth)


for i in range(0, len(flag)-1):
    window = flag[i:i+win_size]
    print_loop(window, len(window))
    time.sleep(.03)
    delete_last(len(window))