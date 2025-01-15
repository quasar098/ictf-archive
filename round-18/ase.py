from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

flag = open("flag.txt", "rb").read()

key = pad(os.urandom(1), 16)

c = AES.new(key, AES.MODE_ECB)
print(c.encrypt(pad(flag,16)))

# b'\xd9d(n\x94\x07P\x05\xb7\x85U\xb2\xf6s\x8eH\xa3\xcf\xa0\x9eR\xc2U*P\xe4\x83\x84w|\x9c\x81\x1b\xec\xb7M\xdf\x17\x8an\x91\xa7\x80\x13\\\xf7\xdf\xed'
