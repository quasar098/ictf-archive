#!/usr/bin/env python3
import random
from Crypto.Util.number import long_to_bytes as ltb
from Crypto.Util.strxor import strxor

unintended_solution_yeeter = 1

# getPrime(512) from Crypto.Util.number
prime = 9748729228494339631846388699994098788507701354484040512690379598196693697693937149457269291065421274894121574705508351692344913516332264306279955933193803

random.seed(0)
for i in range(10**100):
	r = random.getrandbits(24)
	unintended_solution_yeeter *= r
	unintended_solution_yeeter %= prime # modulus needs to be prime, cuz otherwise unintended_solution_yeeter (may) be 0
	random.seed(r)

assert unintended_solution_yeeter.bit_length() > 200  # sufficient
random.seed(random.getrandbits(24)*unintended_solution_yeeter)

with open("flag.txt", "rb") as f:
	flag = f.read()

with open("flag.enc", "wb") as f:
	f.write(strxor(flag, ltb(random.getrandbits(len(flag)*8))))