#!/usr/local/bin/python
import random
flag = open('flag.txt').read()
print("Welcome! Let's play a game!")
def print_menu():
	print("""1) Get random bits
2) Guess number
3) Exit	""")

while True:
	print_menu()
	x = int(input("Choice: "))
	if x == 1:
		print("How many random numbers do you want?")
		r = int(input())
		arr = []
		for i in range(r):
			arr.append(random.getrandbits(32))
		print(f'Here you go: {arr}')
	if x == 2:
		to_guess = random.randint(0,65535*65537)
		guess = int(input("Enter guess: "))
		if guess == to_guess:
			print(f"Wow! Here's your flag: {flag}")
		else:
			print('Incorrect!')
			exit()
	if x == 3:
		exit()