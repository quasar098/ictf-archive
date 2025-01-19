#!/usr/local/bin/python
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
from Crypto.Util.Padding import pad, unpad
from os import urandom
from json import loads

KEY = urandom(16)
TOKEN_ID = urandom(8).hex()

def encrypt(data):
    cipher = AES.new(key=KEY,mode=AES.MODE_CBC)
    return cipher.iv.hex() + cipher.encrypt(pad(data,AES.block_size)).hex()

def decrypt(data):
    iv, ctext = data[:16], data[16:]
    cipher = AES.new(key=KEY,iv=iv,mode=AES.MODE_CBC)
    return unpad(cipher.decrypt(ctext), 16)

def generate_token():

    print("With our super advanced AI, we have determined you to be of the user: Tarnished")
    _ = {}
    _["user"] = "Tarnished"
    _["privileges"] = "None"
    _["id"] = TOKEN_ID
    _["rooRunes"] = 0
    token = encrypt(str(_).replace("'","\"").encode())
    print(f"Here is your token: {token}")
    return token

def validate(token):
    try:
        data = decrypt(bytes.fromhex(token))
        try:
            _ = loads(data.decode())
            print(f"Token valid!")
            return True
        except:
            print(f"Token Invalid. Error Code {bytes_to_long(data)}")
            return False
    except:
        print("Token Invalid. Error Code 0")
        return False

def buy_flag(token):
    try:
        data = decrypt(bytes.fromhex(token))
        _ = loads(data.decode())
        price = int(urandom(9).hex(),16)
        if _["user"] not in ["Morgott", "Godfrey", "Marika", "Radagon", "Malenia", "Godwyn", "Miquella"] or _["privileges"] != "All" or _["id"] != TOKEN_ID:
            print("You don't have the right, O you don't have the right. therefore you don't have the right, O you don't have the right")
            print("jctf{Also_play_elden_ring!}")
        else:
            if int(_["rooRunes"]) > price:
                print(f"The flag currently costs {price} rooRunes.")
                print("You bought the flag. The flag is,")
                print(open('flag.txt').read())
            else:
                print(f"The flag currently costs {price} rooRunes.")
                print("You need more rooRunes.")
                print("jctf{Also_play_elden_ring!}")
    except:
        print("Error, token invalid.")

def main():
    print("Welcome to The Elden Token! While a Tarnished like you will never be Elden Lord (per the words of Morgott The Grace Given), This application uses cutting edge technology to ensure your login details, credentials and other information is safe!")
    print("With our state of the art system, we'll help you validate tokens and issue new tokens!\n")
    token = ""
    while True:
        choice = input("Tokenator Menu\n1.Get Token\n2.Validate and Register New Token\n3.Buy Flag\n>>")
        if choice == "1":
            token = generate_token()
        elif choice == "2":
            _ = str(input("Enter token to validate: "))
            if (validate(_)):
                token = _
        elif choice == "3":
            if not token:
                print("Hey, you dont have a token!")
            else:
                buy_flag(token)
        else:
            print("Invalid input!")
        print("\n")

if __name__ == "__main__":
    main()
