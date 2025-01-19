from FLAG import flag
from Crypto.Util.number import *
from secrets import randbits

caesar_lucky_number = 7
m = bytes_to_long(flag)
p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 17       # woah smol e attack?? :O

c0 = pow(m,e,n)
caesar_shift = randbits(caesar_lucky_number)
c1 = pow(m+caesar_shift,e,n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c0 = {c0}')
print(f'c1 = {c1}')
