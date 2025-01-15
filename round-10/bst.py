#!/usr/bin/env -S python3 -u

import time

class Tree:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def set(self, data):
        self.data = data

    def add(self, data):
        if self.data == None:
            self.data = data
            return
        if data < self.data:
            if self.left is not None:
                self.left.add(data)
            else:
                self.left = Tree(data)
        if data > self.data:
            if self.right is not None:
                self.right.add(data)
            else:
                self.right = Tree(data)
        # note that duplicates don't get added to the tree

    def find(self, data):
        time.sleep(0.01) # cpu throttling or something like that
        if self.data == data:
            return True
        if data > self.data:
            return self.right is not None and self.right.find(data)
        if data < self.data:
            return self.left is not None and self.left.find(data)
        return False

    def length(self):
        ret = 1 if self.data is not None else 0
        ret += self.right.length() if self.right is not None else 0
        ret += self.left.length() if self.left is not None else 0
        return ret


def get_flag():
    with open("/tmp/bst_flag", 'rt') as f:
        return f.read()

def calibrate():
    print("Press enter to begin a 1 second delay.")
    input()
    time.sleep(1)
    print("1 second has passed")

if __name__ == "__main__":
    print("Hello! This service will tell you if you have found the correct flag.")
    while True:
        print()
        print("Menu:")
        print("(1) Calibrate Timing")
        print("(2) Check Flag")
        x = input()
        if '1' in x:
            calibrate()
        if '2' in x:
            break
    bst = Tree(None)
    print("For speed, this service allows you to check the value of multiple flags at the same time.")
    print("Please enter any number of 16 character flags, in the regex form ictf{.+}")
    print("These should be separated by newlines.")
    print()
    print("To stop submitting flags and have them checked, enter an empty string.")
    while True:
        s = input("Flag: ")
        if len(s) == 0:
            break
        bst.add(s)
    #print("length", bst.length())
    if bst.find(get_flag()[:16]):
        print("One of the flags you submitted is the correct flag!")
    else:
        print("Sorry, none of the flags you submitted were correct...")
