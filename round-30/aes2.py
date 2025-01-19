# based off of https://github.com/boppreh/aes/blob/master/aes.py

import os

KEY_SIZE = 16
ROUNDS = 13

s_box = [105, 104, 107, 106, 109, 108, 111, 110, 97, 96, 99, 98, 101, 100, 103, 102, 121, 120, 123, 122, 125, 124, 127, 126, 113, 112, 115, 114, 117, 116, 119, 118, 73, 72, 75, 74, 77, 76, 79, 78, 65, 64, 67, 66, 69, 68, 71, 70, 89, 88, 91, 90, 93, 92, 95, 94, 81, 80, 83, 82, 85, 84, 87, 86, 41, 40, 43, 42, 45, 44, 47, 46, 33, 32, 35, 34, 37, 36, 39, 38, 57, 56, 59, 58, 61, 60, 63, 62, 49, 48, 51, 50, 53, 52, 55, 54, 9, 8, 11, 10, 13, 12, 15, 14, 1, 0, 3, 2, 5, 4, 7, 6, 25, 24, 27, 26, 29, 28, 31, 30, 17, 16, 19, 18, 21, 20, 23, 22, 233, 232, 235, 234, 237, 236, 239, 238, 225, 224, 227, 226, 229, 228, 231, 230, 249, 248, 251, 250, 253, 252, 255, 254, 241, 240, 243, 242, 245, 244, 247, 246, 201, 200, 203, 202, 205, 204, 207, 206, 193, 192, 195, 194, 197, 196, 199, 198, 217, 216, 219, 218, 221, 220, 223, 222, 209, 208, 211, 210, 213, 212, 215, 214, 169, 168, 171, 170, 173, 172, 175, 174, 161, 160, 163, 162, 165, 164, 167, 166, 185, 184, 187, 186, 189, 188, 191, 190, 177, 176, 179, 178, 181, 180, 183, 182, 137, 136, 139, 138, 141, 140, 143, 142, 129, 128, 131, 130, 133, 132, 135, 134, 153, 152, 155, 154, 157, 156, 159, 158, 145, 144, 147, 146, 149, 148, 151, 150]
inv_s_box = [s_box.index(i) for i in range(256)]


def sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = s_box[s[i][j]]


def inv_sub_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = inv_s_box[s[i][j]]


def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


def inv_shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]

def mix_columns(s):
    ret = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            tmp = 0
            for k in range(4):
                offset = (j+k)%4
                tmp |= s[offset][i] & (0x11 << k)
            ret[j][i] = tmp
    for i in range(4):
        for j in range(4):
            s[i][j] = ret[i][j]

def inv_mix_columns(s):
    ret = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            tmp = 0
            for k in range(4):
                offset = (j-k)%4
                tmp |= s[offset][i] & (0x11 << k)
            ret[j][i] = tmp
    for i in range(4):
        for j in range(4):
            s[i][j] = ret[i][j]

def add_round_key(s, k):
    for i in range(4):
        for j in range(4):
            s[i][j] ^= k[i][j]

def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))
    
def pad(plaintext):
    """
    Pads the given plaintext with PKCS#7 padding to a multiple of 16 bytes.
    Note that if the plaintext size is a multiple of 16,
    a whole block will be added.
    """
    padding_len = 16 - (len(plaintext) % 16)
    padding = bytes([padding_len] * padding_len)
    return plaintext + padding

def unpad(plaintext):
    """
    Removes a PKCS#7 padding, returning the unpadded text and ensuring the
    padding was correct.
    """
    padding_len = plaintext[-1]
    assert padding_len > 0
    message, padding = plaintext[:-padding_len], plaintext[-padding_len:]
    assert all(p == padding_len for p in padding)
    return message

def split_blocks(message, block_size=16, require_padding=True):
        assert len(message) % block_size == 0 or not require_padding
        return [message[i:i+16] for i in range(0, len(message), block_size)]


class AES2:
    def __init__(self, key):
        """
        Initializes the object with a given key.
        """
        self.n_rounds = ROUNDS
        self._key_matrices = [bytes2matrix(k) for k in key]

    def encrypt_block(self, plaintext):
        """
        Encrypts a single block of 16 byte long plaintext.
        """
        assert len(plaintext) == 16

        plain_state = bytes2matrix(plaintext)

        add_round_key(plain_state, self._key_matrices[0])

        for i in range(1, self.n_rounds):
            sub_bytes(plain_state)
            shift_rows(plain_state)
            mix_columns(plain_state)
            add_round_key(plain_state, self._key_matrices[i])

        sub_bytes(plain_state)
        shift_rows(plain_state)
        add_round_key(plain_state, self._key_matrices[-1])

        return matrix2bytes(plain_state)

    def decrypt_block(self, ciphertext):
        """
        Decrypts a single block of 16 byte long ciphertext.
        """
        assert len(ciphertext) == 16

        cipher_state = bytes2matrix(ciphertext)

        add_round_key(cipher_state, self._key_matrices[-1])
        inv_shift_rows(cipher_state)
        inv_sub_bytes(cipher_state)

        for i in range(self.n_rounds - 1, 0, -1):
            add_round_key(cipher_state, self._key_matrices[i])
            inv_mix_columns(cipher_state)
            inv_shift_rows(cipher_state)
            inv_sub_bytes(cipher_state)

        add_round_key(cipher_state, self._key_matrices[0])

        return matrix2bytes(cipher_state)

    def encrypt(self, pt):
        pt = pad(pt)
        ct = b""
        for block in split_blocks(pt):
            ct += self.encrypt_block(block)
        return ct

    def decrypt(self, ct):
        pt = b""
        for block in split_blocks(ct):
            pt += self.decrypt_block(block)
        return unpad(pt)

menu = """Choose an option:
1 - Encrypt some data
2 - Encrypt flag
"""

if __name__ == "__main__":
    KEY = [os.urandom(KEY_SIZE) for _ in range(ROUNDS + 1)]
    cipher = AES2(KEY)
    flag = open("flag.txt", "rb").read()

    print("Welcome to the AES2 encryption service. Sorry, no decrypting here, youre on your own for that one.")

    while True:
        print(menu)
        option = input("> ")
        if option == "1":
            pt = bytes.fromhex(input("Enter your data in hex format\n> "))
            print(cipher.encrypt(pt).hex())
        elif option == "2":
            print(cipher.encrypt(flag).hex())
        else:
            print("Bye")
            break
