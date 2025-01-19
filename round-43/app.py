#!/usr/bin/env python3

import discord

print("Hi! ImaginaryCTF is looking for challenges for the upcoming March round. Can you write a medium-level challenge for us? You will get the flag after we recieve your challenge.")
challenge = input("Enter challenge here, markdown formatted: ")
discord.send_dm("eth007", challenge) # yea it doesnt work this way ik
