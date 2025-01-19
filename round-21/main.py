import random

number = random.randint(1, 1000)
flag = open("flag.txt", "r")
flag = flag.readline()
print("Think you can guess my number THIRTY times in a row?")
for n in range(1, 31):
   print(f"\nAttempt #{str(n)}")
   fail == True
   for x in range(1, 11):
      guess = int(input("What's your guess?: "))
      if guess == number:
         print("You guessed my number!")
         fail = False
         break
      elif guess > number:
         print("Your guess is too high.")
      elif guess < number:
         print("Your guess is too low.")
   if fail == True :
      print("\nYou wern't able to guess my number in 10 tries :(")
      exit()
print(f"You guessed my number thirty times in a row! Here's your flag!: {flag}")
