#!/usr/bin/env python3

from random import randint

alphabet = bytes(range(32, 127))

def caesar(plaintext, key):
    ret = [alphabet[(plaintext[0] + key[0] - 32)%len(alphabet)]]
    if len(plaintext) > 1:
           ret += caesar(plaintext[1:], caesar(key, key))
    return ret

if __name__ == '__main__':
    flag = open("flag.txt", 'rb').read()
    key = randint(0, 2**128)
    print(bytes(caesar(flag, [key])))

# Output:
# b'w Mw>Y2XE/cOO+8`mSIBd]_dQS3H!:{:gI5f!":%2SVgN1pM>|;lh[G9m]p`U?0@1O3'
