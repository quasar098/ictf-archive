def next():
    x = 2
    while True:
        yield x
        x = (15*x + 1) % 143731314793242134

from time import time, sleep

encflag = b'k|\xa6)\xd9\x0c>\x9cq\x8fMf\xd7`\xd4\xdb\x1c\xf2\x84\xb3/<\xdf5\xb8"Q'
sequence = next()

for i,j in zip(sequence, encflag):
    start = time()
    sleep(i)
    key = round(time() - start) % 256
    print(chr(j ^ key))
