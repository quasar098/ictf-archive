from Crypto.Util.number import *
from random import randint


flag = open("flag.txt", "rb").read()
caesar = lambda v, k: "".join([str((int(c)+k) % 10) for c in str(v)])
assert len(flag) == 52, len(flag)
for i in range(0, len(flag), 4):
    prime_size = i | 128
    p, q = getPrime(prime_size), getPrime(prime_size)
    assert p != q
    ct = pow(bytes_to_long(flag[i:i+4]), 65537, p*q)
    print(caesar(ct, randint(0, 9)), caesar(p, randint(0, 9)), caesar(q, randint(0, 9)))
