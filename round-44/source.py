from Crypto.Util.number import bytes_to_long, getPrime
from os import urandom
from secret import FLAG

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 3
d = pow(e, -1, (p - 1) * (q - 1))
x = len(FLAG) // 3

print(f'[A] Please send me the encrypted message. My public key is ({n:x}, {e:x})')

m1 = bytes_to_long(b'How can you tell a difference between a good cryptography joke and a random string of words? ' + FLAG[:x])
print(f'[B] {pow(m1, e, n):x}')

m2 = bytes_to_long(b'You can\'t. They\'re indistinguishable! Hahahahahahahahahahahahahahahahahahahahahahahahahaha! ' + FLAG[x:2*x])
print(f'[B] {pow(m2, e, n):x}')

print('[A] Stop with those stupid jokes and just send me the third part of the message! But this time, please pad it.')

padding = urandom(128)
m3 = bytes_to_long(padding + FLAG[2*x:] + urandom(16))
print(f'[B] {pow(m3, e, n):x}')

print('[A] I think the message got corrupted, could you send it again?')

m4 = bytes_to_long(padding + FLAG[2*x:] + urandom(16))
print(f'[B] {pow(m4, e, n):x}')

print('[A] Thanks!')
