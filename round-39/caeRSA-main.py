from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long

p = getPrime(1024)
q = getPrime(1024)
e = 65537

n = p*q
leak = (p+42)*(q+69)
m = bytes_to_long(open("flag.txt", "rb").read().strip())
c = pow(m, e, n)

print(f"{n = }")
print(f"{e = }")
print(f"{c = }")
print(f"{leak = }")
