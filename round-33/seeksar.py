#!/usr/bin/env python3

alphabet = bytes(range(32, 127))

def seeksar(s, key):
    out = []
    for c in s:
        offset = key.read()[0]
        out.append(alphabet[(c+offset)%len(alphabet)])
        key.seek(offset)
    return bytes(out)

flag = open("flag.txt", "rb").read()

print(seeksar(flag, open(__file__, 'rb')))

# Output:
b"M'HG\\BOE@CZ@QPQVMBS@EFNBOE@*@NFBO@RVBTBSgT@EFNBOE@xEpEsyqG^"
