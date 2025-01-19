#!/usr/local/bin/python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import time

def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext

flag = open('flag.txt','rb').read().strip()
random.seed(int(time.time()))
key = random.randbytes(16)

encrypted_flag = encrypt(flag, key)
print("Encrypted flag (in hex):", encrypted_flag.hex())