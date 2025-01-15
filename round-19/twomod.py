from Crypto.Util.number import getPrime, bytes_to_long
from math import lcm
import sys

def keygen():
    p = getPrime(1024)
    q = getPrime(1024)
    return p*p*q, p*q, pow(p*p*q,-1,lcm((p-1),(q-1)))

def encrypt(m):
    return pow(m,n1,n1)

def decrypt(m):
    return pow(m,d,n2)

def exit(_):
    with open("flag.txt", "rb") as f:
        flag = bytes_to_long(f.read().strip())
    print(f"{encrypt(flag) = }")
    sys.exit(0)

if __name__ == "__main__":
    n1, n2, d = keygen()
    print(f"{n1 = }")

    while True:
        method = input("? ")
        print({"enc": encrypt, "dec": decrypt}.get(method, exit)(int(input("> "))))
