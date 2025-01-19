#!/usr/bin/env python3

import shelve

name = ""

end = 10
enemies = [3, 5, 7, 9]

def handle_move(new_loc, db):
    if new_loc < 0 or new_loc > end:
        print("You can't move there!")
        return
    db[f"{name}_location"] = new_loc
    if new_loc == end:
        print("You reached the end and grabbed the flag!")
        db[f"{name}_hasFlag"] = 1
        return
    if new_loc in enemies:
        if db[f"{name}_hasFlag"]:
            print("Oh no! You've been caught with the flag, and sent back to the beginning!")
            db[f"{name}_location"] = 0
            db[f"{name}_hasFlag"] = 0
        else:
            print("You've been spotted!")
            print("Fortunately, you don't have the flag, so nothing happens.")
        return
    if new_loc == 0 and db[f"{name}_hasFlag"]:
        print("You recovered the flag! Nice work!")
        print(*open("flag.txt"))
        db[f"{name}_location"] = 0
        db[f"{name}_hasFlag"] = 0
        exit()

def menu():
    with shelve.open("db") as db:
        print()
        print(f"You are at location {db[f'{name}_location']}.")
        if db[f"{name}_hasFlag"]:
            print("You have the flag!")
        else:
            print("You do not have the flag.")
        print("What would you like to do?")
        print("1) Move forward")
        print("2) Move backwards")
        print("3) Save progress and quit")
        print("4) Reset")
        choice = input("\n>>> ")
        if '1' in choice:
            handle_move(db[f"{name}_location"] + 1, db)
        elif '2' in choice:
            handle_move(db[f"{name}_location"] - 1, db)
        elif '3' in choice:
            print(f"Thanks for playing, {name}!")
            exit()
        elif '4' in choice:
            db[f"{name}_hasFlag"] = 0
            handle_move(0, db)
        else:
            print("Invalid input!")

def main():
    global name
    name = input("What is your name? ")
    with shelve.open("db") as db:
        if f"{name}_location" not in db or f"{name}_hasFlag" not in db:
            db[f"{name}_location"] = 0
            db[f"{name}_hasFlag"] = 0
            print(f"Creating profile for {name}...")
        else:
            print(f"Loading data for {name}...")
    print(f"Welcome to Capture the Flag, {name}!")
    print(f"Grab the flag at the end of the field and bring it back home.")
    print(f"But don't get caught!")
    while(1):
        menu()

if __name__ == '__main__':
    main()
