from PIL import Image
import numpy as np
from Crypto.Cipher import AES
from os import urandom

img = np.asarray(Image.open('penguin.png'))

cipher = AES.new(urandom(16), AES.MODE_ECB)
ct = cipher.encrypt(img.tobytes())

open("penguin.png.enc", "wb").write(ct)
