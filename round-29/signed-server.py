#!/usr/bin/env python3

from hashlib import sha1
from os import urandom

SECRET = urandom(320)

def die(*args):
    print(*args)
    exit()

def hmac(key, msg):
    return sha1(msg+key).digest()

def sign_message(msg):
    return hmac(SECRET, msg) + msg

def verify_message(signed):
    signature = signed[:20]
    msg = signed[20:]
    if hmac(SECRET, msg) == signature:
        return msg
    else:
        die("Signature not valid!")

if __name__ == '__main__':
    hex_msg = bytes.fromhex(input("Enter a message to sign, in hex\n>>> "))
    if len(hex_msg) > 1024:
        die("Message too long!")
    print("Signed message:")
    print(sign_message(hex_msg).hex())
    print()
    signed_msg = input("Enter a different signed message, in hex\n>>> ")
    new_msg = verify_message(bytes.fromhex(signed_msg))
    if new_msg == hex_msg:
        die("These two messages are the same!")
    print(open("flag.txt").read())