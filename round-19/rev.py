import string
import numpy as np
from secret import pt

'''
  B A       1  0
(     ) = (      )
  G L       6  11
'''

values = dict()
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index

pt_chunks = [pt[i:i+2] for i in range(0, len(pt), 2)]

ct = ""
enc = np.matrix(((1,0), (6,11)))
for chunk in pt_chunks:
    mult = ( enc * np.matrix(([int(values[chunk[0]])], [int(values[chunk[1]])])) ) % 26
    for key, value in values.items():
        if value == mult.item(0):
            ct += key
    for key, value in values.items():
        if value == mult.item(1):
            ct += key

print(f"{ct = }")
# ct = 'NYWDRCDQIJGLHASMIXHQFCUVFQNWTUOTCMLK'
