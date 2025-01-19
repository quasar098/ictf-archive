from Crypto.Util.number import getPrime, bytes_to_long

with open('flag.txt','rb') as f:
    m = bytes_to_long(f.read())

e = 0x10001
k = getPrime(4)
l = getPrime(512)
p = getPrime(512)
q = getPrime(512)
n = p*q
c = pow(m, e, n)
d = pow(2, k, n)
f = pow(p, d, l)

print(f"c = {c}")
print(f"n = {n}")
print(f"f = {f}")
print(f"l = {l}")