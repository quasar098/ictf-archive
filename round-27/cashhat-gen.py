#!/usr/bin/env python3

from hashlib import sha512
from random import choice, randint

words = [i.strip() for i in open("google-10000-english-no-swears.txt") if len(i) >= 12]
flag = f"ictf{{{choice(words)}{choice(words).upper()}{'%02d'%randint(0,99)}}}"
print(sha512(flag.encode()).hexdigest())

# 79959ceac451e42088f978040729eb266b7d2818eafcc1b71072e8050f71cf4ead9d5dcbdbf539c2f45ec63f313e43166502899057d461cfe2ca4df15b59b27e