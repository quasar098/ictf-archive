import secrets

BLOCKLEN = 16
SBOX = [87, 163, 127, 114, 77, 128, 93, 126, 251, 105, 81, 216, 74, 158, 210, 122, 54, 90, 85, 254, 37, 72, 249, 234, 78, 174, 66, 14, 18, 203, 149, 60, 246, 9, 3, 80, 214, 141, 107, 245, 116, 150, 248, 183, 135, 227, 67, 71, 48, 153, 62, 42, 55, 83, 236, 146, 206, 244, 82, 56, 219, 182, 137, 23, 217, 111, 38, 5, 51, 223, 185, 221, 132, 103, 195, 200, 118, 226, 157, 124, 229, 238, 76, 253, 220, 155, 170, 145, 201, 21, 11, 177, 35, 154, 101, 86, 28, 180, 53, 70, 104, 215, 0, 181, 228, 68, 242, 52, 123, 161, 172, 186, 162, 59, 176, 152, 224, 125, 207, 178, 115, 7, 102, 45, 147, 222, 151, 139, 63, 237, 10, 160, 239, 20, 73, 69, 136, 188, 47, 58, 240, 1, 164, 166, 202, 100, 120, 199, 184, 196, 138, 95, 94, 88, 250, 193, 49, 247, 243, 198, 235, 129, 189, 24, 209, 117, 17, 205, 44, 191, 16, 142, 190, 31, 29, 113, 165, 204, 140, 241, 96, 26, 197, 169, 187, 159, 252, 110, 27, 79, 255, 99, 143, 230, 19, 108, 121, 192, 40, 12, 89, 175, 171, 144, 43, 92, 213, 65, 22, 91, 106, 119, 232, 64, 98, 148, 218, 173, 30, 225, 50, 75, 168, 211, 130, 179, 34, 6, 46, 208, 41, 61, 134, 194, 36, 13, 2, 133, 32, 57, 25, 33, 112, 233, 131, 8, 97, 15, 4, 167, 109, 156, 212, 231, 39, 84]

def S(b):
    hexes = list(b.hex())
    for i in range(2*BLOCKLEN - 1):
        n = int(hexes[i] + hexes[i + 1], 16)
        n = SBOX[n]
        hexes[i:i+2] = list(hex(n)[2:].zfill(2))
    return bytes.fromhex(''.join(hexes))

def blocks(m):
    return list(zip(*[iter(m)] * BLOCKLEN))

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def H(m):
    assert len(m) % BLOCKLEN == 0
    state = S(b"ictf{_initial0_}"[::-1])
    assert len(state) == BLOCKLEN
    for b in blocks(m):
        state = S(xor(state, b))
    return state

def main():
    challenge = secrets.token_bytes(20)
    print(f"This is your challenge, now get me a good hash... {challenge.hex()}")
    attempt = bytes.fromhex(input("> ").strip())
    if not attempt.startswith(challenge):
        print("Invalid")
        return
    if H(attempt).startswith(b"ictf{"):
        print("Oh, this looks close")
    if H(attempt) != b"ictf{_solution_}":
        print("Nahh")
        return
    with open("flag.txt", "r") as f:
        print(f.read())
        
if __name__ == "__main__":
    main()
