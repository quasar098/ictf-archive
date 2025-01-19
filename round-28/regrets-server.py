#!/usr/bin/env python3

from re import *

flag = open('flag.txt').read()

while True:
    rx = input("Enter your regex: ")
    if fullmatch(rx, flag) is None:
        print("Nope!")
    else:
        print("Match!")
