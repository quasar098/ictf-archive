from Crypto.Util.number import bytes_to_long, getPrime
from Crypto.Random.random import getrandbits

flag = b"ictf{xxxxxxxxxxxxxxxxxxxxxxx}"
flag = bytes_to_long(flag)

p = getPrime(512)
k = [getrandbits(n*2+3) for n in range(flag.bit_length())]
assert all(n < p for n in k)

e = getrandbits(1024)
pub = [(m * e) % p for m in k]

c = []
for n in range(flag.bit_length()):
  c.append((flag % 2) * pub[n])
  flag //= 2

print(f"{pub}")
print(f"{sum(c)}")
