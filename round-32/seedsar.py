#!/usr/bin/env python3

from random import randint, seed

LIMIT = 10**8
alphabet = bytes(range(32, 127))

def seedsar(s, key):
    out = []
    for c in s:
        out.append(alphabet[(c+key)%len(alphabet)])
        seed(key)
        key = randint(0, LIMIT)
    return bytes(out)

flag = open("flag.txt", "rb").read()

print(seedsar(flag, randint(0,LIMIT)))

# Output:
# b']lFKQGuMKHkt7\'WnRM^H~|<)QmO=7Yo*1}5/q](1hH&y RG$v|RI5&=>>SBg{=Ea5q,V,b_Q\'cM%cBs-G9^nn*i~;%pWBe?,bQKe]g%]9\\L_x!"V::MG2hR,/yr<K}wA}JKH&<O/^#igA@|{*`oB"a<~'