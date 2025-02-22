#!/usr/bin/env python3

ct = [179, 162, 146, 80, 226, 146, 80, 35, 131, 226, 242, 67, 226, 83, 80, 115, 67, 80, 83, 195, 80, 83, 83, 80, 67, 243, 243, 211, 80, 67, 243, 243, 194, 99, 243, 99, 130, 179, 80, 35, 179, 147, 147, 80, 147, 179, 242, 80, 146, 83, 243, 226, 227, 80, 80, 130, 115, 179, 243, 99, 80, 51, 83, 115, 195, 51, 80, 146, 131, 80, 243, 130, 51, 179, 67, 243, 211, 162, 80, 162, 226, 179, 243, 80, 130, 226, 130, 35, 51, 211, 131, 51, 99, 115, 50, 80, 80, 146, 83, 51, 130, 35, 51, 226, 211, 18, 51, 195, 67, 226, 179, 147, 99, 51, 114]

def reversive(s):
    if len(s) == 1:
        return ((s[0]>>4)+(s[-1]<<4)&0xff)^0xa5^ct.pop()
    return reversive([s[-1]]) or reversive(s[-2::-1])

if reversive(input(">>> ").encode()):
    print("no")
else:
    print("yes")