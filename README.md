# ictf challenge archive

this is a work in progress

## how?

short: scripting 100

long: i scraped the ictf archives for all challenges and challenge attachments that have imaginaryctf.org/whatever/whatever, and then i changed the /f/ in the link to /r/ so then when you try to access it, it redirects you to an actual discord link (but it is broken). then, i put all of the links onto discord using a webhook. these fix the discord links because discord implemented a policy where you cant just download discord links freely unless you are clicking it from discord (they added some verification stuff at the end of the url to make sure). a script is used to automatically download all of the files, but i still have to sort through them by hand to dump them into their rounds. all-files.txt. is also generated with a script

## notes on finding challenges

you will need the name of the challenge you are looking for, as well as the round number

all of the filenames for each challenge are listed in the all-files.txt file

you will need to go into that round-X folder in this directory, and find the filename. if you cannot find it, try looking for it prefixed with the title of the challenge (to avoid duplicate filenames if there are 99999 chall.py for one round)

keep in mind that some of the files discord has deleted from their cache, so i was not able to download them. you may be able to find this online; this is left as an OSINT exercise for the reader (sorry lol). these files are listed in unrecovered.txt.

if you truly cannot find it, do not contact me asking for help.

## todo

- rounds before round 9 do manually

- sort through the rest of the rounds

- save challenge descriptions and authors (?)