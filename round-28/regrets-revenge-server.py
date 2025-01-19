#!/usr/bin/env python3

from re import *

flag = open('flag.txt').read()

while True:
    rx = input("Enter your regex: ")

    if not all(i not in flag for i in rx):
        print("No using flag characters!")
    elif fullmatch(rx, rx) is None:
        print("Your regex must match itself!")
    elif fullmatch(rx, flag) is None:
        print("Nope!")
    else:
        print("Match!")
    
        
