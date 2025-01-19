#!/usr/bin/env python3

from hashlib import sha256
from datetime import datetime
from time import sleep
from os import urandom

secret = urandom(16)
flag = open("flag.txt").read()


def sign(time):
    time_in_bytes = time.to_bytes((time.bit_length() + 7) // 8, "little")
    return sha256(secret + time_in_bytes).hexdigest()


def extend_time(extended_time):
    print("Current extended time: " + str(extended_time))
    print("How many seconds do you want to extend time with?")
    inp_time = input(">> ")

    if len(inp_time) > 10:
        print("Thats too long!")
        return extended_time

    time = int(float(inp_time))

    if time < 0:
        print("Invalid time!")
        return extended_time

    return extended_time + time


def get_time(extended_time):
    time = int(datetime.now().timestamp()) + extended_time
    time_signature = sign(time)

    print("Time of generation: " + str(time))
    print("Time signature: " + time_signature)


def get_flag(extended_time):
    time = int(datetime.now().timestamp()) + extended_time
    time_signature = sign(time)

    print("Time of generation: " + str(time))
    print("Guess the time signature to get the flag!")
    inp_signature = str(input(">> "))

    if inp_signature == time_signature:
        print("Wow you did it! Here is the flag: " + flag)
        exit()
    else:
        print("Wrong time signature!")


def main():
    print("----------------------------------------------")
    print("|                                            |")
    print("|        Welcome to the Time Signer!         |")
    print("|   Who wouldn't want their time signed?!?   |")
    print("|                                            |")
    print("----------------------------------------------")

    extended_time = 0

    while True:
        print("")
        print("Please select an option:")
        print("1. Extend time")
        print("2. Get time")
        print("3. Get flag")
        print("4. Exit")

        inp = int(input(">> "))
        print("")

        if inp == 1:
            extended_time = extend_time(extended_time)

        elif inp == 2:
            get_time(extended_time)

        elif inp == 3:
            get_flag(extended_time)

        elif inp == 4:
            exit()

        else:
            print("Invalid option!")

        sleep(1)


if __name__ == "__main__":
    main()
