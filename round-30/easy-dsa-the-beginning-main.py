from Crypto.Util.Padding import pad
from Crypto.Util.number import isPrime, getPrime, long_to_bytes
from Crypto.Cipher import AES
from hashlib import sha256
from random import randrange

def gen_key():
    p = 0
    while not isPrime(p):
        q = getPrime(300)
        p = 2*q + 1

    g = randrange(2, p)**2 % p
    k = randrange(2, q)
    x = randrange(2, q)
    y = pow(g, x, p)
    return p, q, g, x, y, k

def H(msg):
    return int.from_bytes(sha256(msg).digest(), 'big')

def sign(m):
    r = pow(g, k, p) % q
    s = (H(m) + x*r) * pow(k, -1, q) % q
    return r, s

def verify(m, r, s):
    assert 0 < r < q and 0 < s < q
    u = pow(s, -1, q)
    v = pow(g, H(m) * u, p) * pow(y, r * u, p) % p % q
    return v == r

flag = b"ictf{REDACTED}"
p, q, g, x, y, k = gen_key()

ms = b"jctf{powered_by_caffeine}", b"jctf{totally_real_flag}"
sigs = [sign(m) for m in ms]
assert all(verify(m, *sig) for m, sig in zip(ms, sigs))

aes = AES.new(long_to_bytes(x)[:16], AES.MODE_CBC, b'\0'*16)
c = aes.encrypt(pad(flag, 16)).hex()

print(f'{p = }\n{g = }\n{y = }\n{ms = }\n{sigs = }\n{c = }')
