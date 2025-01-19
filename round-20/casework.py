import base64

with open("flag.txt", "rb") as f:
    print(base64.b64encode(f.read().strip()).lower().decode())
