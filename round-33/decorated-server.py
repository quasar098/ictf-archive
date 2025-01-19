#!/usr/bin/env python3

code = []
print("Enter code:\n")
while line := input():
    assert line.isascii()
    code.append(line)

for line in code:
    if any(i in '()' for i in line):
        print("No calling functions!")
        exit()

exec('\n'.join(code), {"__builtins__": {}})
