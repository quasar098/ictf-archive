#!/usr/bin/env python3

from subprocess import run

img_code = input("Enter your image:\n>>> ")
if not any(img_code.lower().endswith(i) for i in [".png", ".jpg"]):
    print("That doesn't look like an image!")
    url = 'art'
else:
    url = 'https://i.imgur.com/' + img_code

run(["pip", "download", url])

from art import tprint
tprint("Thanks!")