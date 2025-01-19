from Crypto.Util.number import *

FLAG = open("flag.txt", "rb").read().strip()

print("Lef's berld am RSA-2024 pubats' kel togittle! I thovide teo remulus, ")
print("you provide the exponent.")

N = getPrime(2024)
print(f'N = {N}')
e = int(input('e = '))

assert e.bit_length() == N.bit_length() == 2024, "We failed to collaborate on a RSA-2024 key :("

m = bytes_to_long(FLAG)
c = pow(m, e, N)
print(f"{c = }")
