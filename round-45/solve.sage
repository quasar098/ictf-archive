from Crypto.Cipher import ARC4
from datetime import datetime


def rotl(x, n, nbits=64):
    return ((x << n) % (2**nbits)) | (x >> (64 - n))


class LuaXoshiro:
    def __init__(self, seed=0):
        self.seed(seed)

    def seed(self, seed):
        self.state = [seed, 0xff, 0, 0]

    def raw_seed(self, state):
        self.state = [state >> 192, (state >> 128) % (2**64), (state >> 64) % (2**64), state % (2**64)]

    def next(self):
        [s0, s1, s2, s3] = self.state
        s2 ^^= s0
        s3 ^^= s1
        res = rotl((s1 * 5) % (2**64), 7) * 9 % (2**64)
        self.state[0] = s0 ^^ s3
        self.state[1] = s1 ^^ s2
        self.state[2] = s2 ^^ ((s1 << 17) % (2**64))
        self.state[3] = rotl(s3, 45)
        return res

    def raw_state(self):
        [s0, s1, s2, s3] = self.state
        return (s0 << 192) + (s1 << 128) + (s2 << 64) + s3

    def next_state(self):
        self.next()
        return self.raw_state()


def n_to_bit_list(n, nbits=256):
    F = GF(2)
    result = [None for _ in range(nbits)]
    for i in range(nbits):
        result[i] = F((n >> (nbits - i - 1)) % 2)
    return result

def bit_list_to_n(bl):
    result = 0
    for b in bl:
        result *= 2
        result += int(b)
    return result


def transition_matrix(engine, nbits=256):
    state = engine.state
    columns = []

    for i in range(nbits):
        seed = 1 << (nbits - i - 1)
        engine.raw_seed(seed)
        columns.append(n_to_bit_list(engine.next_state()))

    engine.state = state
    return matrix(GF(2), columns).transpose()


def jump(engine, num_steps, mat=None):
    if mat is None:
        mat = transition_matrix(engine)

    state = engine.raw_state()
    v = vector(n_to_bit_list(state))
    v2 = mat^num_steps * v
    newstate = bit_list_to_n(v2)
    engine.raw_seed(newstate)


def lua_nth_random(e, n, mat=None):
    # lua advances the state 16 times after settig the seed in math.randomseed
    jump(e, n + 16, mat)
    return e.next() & (2**32 - 1)


def solve():
    with open('chall.bmp', 'rb') as f:
        data = f.read()
    header = data[:0x8a]
    enc = data[0x8a:]
    dt = datetime.strptime('31 Jan 2020, 20:38 +0000', '%d %b %Y, %H:%M %z')
    e = LuaXoshiro()
    mat = transition_matrix(e)
    for i in range(60):
        seed = int(dt.timestamp() + i)
        e.seed(seed)
        key = str(lua_nth_random(e, 1_000_000_000_000_000)).encode()
        cipher = ARC4.new(key, drop=3072)
        dec = cipher.decrypt(enc)
        with open(f'decrypted/{i:02}.bmp', 'wb') as f:
            f.write(header + dec)


if __name__ == '__main__':
    solve()

# ictf{xoshiro_jumps_in_lua_like_a_pro}
