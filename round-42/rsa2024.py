from Crypto.Util.number import *
FLAG = open("flag.txt", "rb").read().strip()

print("Let's build an RSA-2024 public key together! I provide the exponent, you provide the modulus.")
e = getRandomNBitInteger(2024)
N = int(input("N = "))
assert e.bit_length() == N.bit_length() == 2024, "We failed to collaborate on a RSA-2024 key :("

m = bytes_to_long(FLAG)
c = pow(m, e, N)
print(f"{c = }")
