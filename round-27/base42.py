#!/usr/bin/env python3

alphabet = "0123456789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpP"

flag = open('flag.txt', 'rb').read().strip()
out = ''

btl = lambda a:sum((v*256**i)for i,v in enumerate(a[::-1]))

while len(flag) > 0:
    val = btl(flag[:21])
    flag = flag[21:]
    chunk = ''
    while len(chunk)<32:
        chunk += alphabet[val%len(alphabet)]
        val //= len(alphabet)
    out += chunk[::-1]

print(out)

# Output:
# 0koA439lJklKBLkABeK3oikB1GL1lelO0lCp50Kii0LFEbcdm1Il17GNKCj6P5KB0mpAfe4pAJ0p5lHb0kIC7K0I03meMpIG
