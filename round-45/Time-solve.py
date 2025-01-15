from pwn import *
import time
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext


io = remote('34.72.43.223','48000')
ciphertext = bytes.fromhex(io.readline()[24:].strip().decode())
x = int(time.time())
for i in range(x-20,x+20):
	random.seed(i)
	key = random.randbytes(16)
	try:
		flag = decrypt(ciphertext,key)
		print(flag)
	except:
		continue