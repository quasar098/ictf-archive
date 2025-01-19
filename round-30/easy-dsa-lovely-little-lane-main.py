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
    x = randrange(2, q)
    y = pow(g, x, p)
    return p, q, g, x, y

def H(msg):
    return int.from_bytes(sha256(msg).digest(), 'big')

def sign(m):
    k = randrange(2, q >> 100)
    r = pow(g, k, p) % q
    s = (H(m) + x*r) * pow(k, -1, q) % q
    return r, s

def verify(m, r, s):
    assert 0 < r < q and 0 < s < q
    u = pow(s, -1, q)
    v = pow(g, H(m) * u, p) * pow(y, r * u, p) % p % q
    return v == r

flag = b"ictf{REDACTED}"
p, q, g, x, y = gen_key()

ms = b"jctf{Puzzler_is_the_best_chall_author}", b"jctf{Wanna_see_you_trying_to_submit_that_flag}", b"jctf{D54_15_345y_4f73r_411}", b"jctf{n0_1d34}", b"jctf{s0_m4ny_fr33_s1g5}"
sigs = [sign(m) for m in ms]
assert all(verify(m, *sig) for m, sig in zip(ms, sigs))

aes = AES.new(long_to_bytes(x)[:16], AES.MODE_CBC, b'\0'*16)
c = aes.encrypt(pad(flag, 16)).hex()

print(f'{p = }\n{g = }\n{y = }\n{ms = }\n{sigs = }\n{c = }')
