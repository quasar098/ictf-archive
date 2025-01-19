#!/usr/bin/env python3

from numpy import prod
from sympy import divisor_count
fun = lambda *x: divisor_count(prod(x))

print('''Welcome to PyCryptoJail!
Please enter a fun(1337) command.
The flag is in ./flag.txt.''')

command = input("> ").encode()
if fun(*command) == fun(1337):
    exec(command)
else:
    print('Invalid command')