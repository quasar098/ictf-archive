from random import randint
flag = b"ictf{some_redacted_lowercase_letters_and_underscores}"

for f in flag:
    a = randint(0, 1 << 255)
    b = randint(a, 1 << 255)
    r = randint(a, b).bit_length()
    print(f'{f^r:02x}', end=' ')

# 96 9c 8a 99 84 8f 9f 91 9b 90 92 a3 90 99 a0 8d 9e 90 9b 91 93 a0 96 8d a2 91 90 8a a0 8c 90 a0 8d 9f 91 9b 90 93 82