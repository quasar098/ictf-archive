#!/usr/bin/env python3

from socket import *
from random import randint
from secret import flag

assert b' ' not in flag
flag = bytes(i if randint(0,1) else 32 for i in flag)

server = input("Enter a hostname or ip: ")
port = int(input("Enter a port: "))

s = socket(AF_INET, SOCK_STREAM)
s.connect((server, port))
s.send(flag)
