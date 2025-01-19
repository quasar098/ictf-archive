from zlib import compress, decompress
from Crypto.Cipher import AES
from os import urandom

def encrypt(raw):
    msg = raw
    return aes.encrypt(compress(msg + flag))

with open('flag.txt', 'rb') as file:
    flag = file.read().strip()

aes = AES.new(urandom(32), AES.MODE_CTR)

while 1:
    pt = decompress(bytes.fromhex(input('salt > ')))
    ct = encrypt(pt)
    print(ct.hex())