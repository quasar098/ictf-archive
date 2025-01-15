#!/usr/local/bin/python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import time
import os

def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext

flag = open('flag.txt','rb').read().strip()
random.seed(int(os.urandom(64).hex(),16)) # super secure!
key = b''
x=random.randbytes(1)
for i in range(16):
	key += x
	random.seed(int(x.hex(),16))
	x = random.randbytes(1)
encrypted_flag = encrypt(flag, key)
print("Encrypted flag (in hex):", encrypted_flag.hex())