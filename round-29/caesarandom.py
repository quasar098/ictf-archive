#!/usr/bin/env python3

from os import urandom

flag = open("flag.txt", "rb").read()

assert len(flag) % 2 == 0

ltb = lambda l:bytes([(l>>(8*i))&0xff for i in range(1,-1,-1)])
btl = lambda b:sum([b[-i-1]<<(8*i) for i in range(2)])

A = btl(urandom(2))|1
B = btl(urandom(2))|1
seed = btl(urandom(2))|1

def next():
    global seed, A, B
    seed = (A*seed + B)&0xffff
    return seed

out = b''
chunks = [flag[2*i:2*(i+1)] for i in range(len(flag)//2)]
for chunk in chunks:
    out += ltb((next()+btl(chunk))&0xffff)

print(out)

# Output:
# b"\xd9K\x9a\xb7O\x86\x15\xd0\x8c\x08\x07S\xaa\xfa&\x1e\xb26zm\x1c\xe3\xa6\xf2\xe8\xf0\x15\xf4VW\xd2F\x1f'\xb4\x17@P\xf9 ,\xe0\x03\xae\x8f\xb7u|\xd0\x0c\x9a\xb27\xb6\xa7B\xcf\xba\xa2Q\xe7-\x84\xb4"