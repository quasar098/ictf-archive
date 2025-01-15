import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from pwn import *

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

io = remote('34.72.43.223','48123')
ciphertext = bytes.fromhex(io.readline()[24:].strip().decode())
for i in range(0,256):
	key = b''
	x = bytes([i])
	for j in range(16):
		key += x
		random.seed(int(x.hex(),16))
		x=random.randbytes(1)
	try:
		flag = decrypt(ciphertext,key)
		print(flag)
	except:
		continue