#!/usr/bin/env python3
from string import printable # I've heard stuff in here is dangerous

code = []
while line := input():
    assert line.isascii() # A friend recommended this to me
    code.append(line)

for line in code:
    if line[0] != '#': # Good code should have comments
        assert not any(x in line for x in printable)

exec('\n'.join(code), { '__builtins__': None }, {})
