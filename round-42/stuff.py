import random
import os

file = open("flag.txt", "r")
flag = file.readline()
string = ""

random.seed(os.stat("stuff.py").st_mtime)

a = str(random.randint(1,10000000000))
b = (os.stat("stuff.py").st_size)*1543424324398769579759769757361544769714143242343241434324324143243424234141432432

for n in flag:
  string += str(ord(n))

string = str((int(string)^b)+int(a[3])-int(a[4])+int(a[3:]))

print(string)