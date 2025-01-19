from Crypto.Util.number import getPrime
from secrets import randbelow

flag = b'ictf{???????????????}'
m = int.from_bytes(flag, 'big')

p, q = getPrime(1024), getPrime(1024)
n = p*q

e1 = 7*randbelow(n)
e2 = 7*randbelow(n)

c1 = pow(m, e1, n)
c2 = pow(m, e2, n)

print('n =', n)
print('e =', [e1, e2])
print('c =', [c1, c2])