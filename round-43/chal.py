#!/usr/bin/env python3

import pickle
import string

inp = input("enter your pickle> ").split()

assert not "h" in "".join(inp)
assert not "." in "".join(inp)

for substring in inp:
  for i in range(len(substring)):
    if i % 2 == 0:
      assert substring[i] in string.printable.lower()
    else:
      assert substring[i] in string.printable.upper() + "osystem" # yw

pickle.loads("\n".join(inp).encode())
