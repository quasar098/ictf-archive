import random, time
from randcrack import RandCrack
from pwn import *

io = remote('34.72.43.223','49133')
io.sendline(b'1')
io.sendline(b'624')
io.readuntil(b'Here you go: ')
arr = (io.readline().strip())
x = b'arr = ' + arr
exec(x)

rc = RandCrack()

for i in range(624):
	rc.submit(arr[i])

answer = rc.predict_randint(0, 65535*65537)
io.sendline(b'2')
io.sendline(str(answer).encode())
io.readuntil(b"Wow! Here's your flag: ")
print(io.readline().strip())