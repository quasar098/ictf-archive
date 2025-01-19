from Crypto.Util.number import getPrime
from secrets import randbelow
from hashlib import sha256

m = getPrime(20)
a = randbelow(m)
b = randbelow(m)
x = randbelow(m)

def rand():
    def rand():
        global a, b, m, x
        x = (a*x + b) % m
        return x

    while 1:
        for _ in range(rand() & 0xFF):
            rand()
        for _ in range(rand() & 0x8):
            yield rand()

def xor(x, y):
    return bytes(a ^ b for a, b in zip(x, y))

rand = rand()
rand = [next(rand) for _ in range(20)]
print('rand =', rand)

print('ct =', xor(b'ictf{REDACTED}', sha256((m + a + b).to_bytes(6, 'big')).digest()))
