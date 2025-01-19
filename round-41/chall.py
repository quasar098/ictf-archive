from hashlib import md5
from secret import flag

assert all(i in b'abcdefghijklmnopqrstuvwxyz0123456789{}_' for i in flag)

hash = md5(flag).digest()
p = 2**17 - 1
arr = []
for i,j in zip(flag[::2], flag[1::2]):
    arr.append(i * pow(j,-1,p) % p)
print(f'arr = {arr}')
print(f'hash = {hash}')

# arr = [27804, 113082, 71154, 1, 108473, 46422, 70266, 9659, 5142, 116383, 49154, 127179, 16778]
# hash = b'L3>\xb0C\xc0/(\xd9\xfa\xd3\xf2\xc4\x1a|\x18'
