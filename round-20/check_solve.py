#!/usr/bin/env -S python3 -u
from config import web3, CONTRACT, BASE_PATH
import eth_account.messages
import secrets, os.path

def gib_flag():
    with open(os.path.join(BASE_PATH, "..", "flag.txt")) as f:
        print(f.read().strip())

if __name__ == "__main__":
    challenge = secrets.token_urlsafe(32)
    print("So you think you solved the challenge?")
    print(f"Send me a hex-encoded signature (EIP-191, version 'E') for the following (ascii) message: {challenge}")
    response = bytes.fromhex(input("> "))
    addr = web3.eth.account.recover_message(eth_account.messages.encode_defunct(text=challenge), signature=response)
    if CONTRACT.caller.owners(addr):
        gib_flag()
    else:
        print(f"Nope, I don't believe you (recovered address = {addr}).")
