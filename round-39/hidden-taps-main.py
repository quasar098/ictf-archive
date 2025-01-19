from random import randint


def lfsr(data: int, size: int, taps: list[int], repetitions: int):
    state = []
    for _ in range(size):
        state.insert(0, data & 1)
        data = data >> 1
    for _ in range(repetitions):
        xored = 0
        for tap in taps:
            xored = xored ^ state[len(state)-tap]
        state = [xored] + state[:-1]
    new_data = 0
    while len(state):
        new_data = state.pop(0) | (new_data << 1)
    return new_data


def main():
    flag = b"ictf{<redacted>}"
    assert len(flag) == 50
    taps = [1]
    for _ in range(9):
        n = randint(2, 39)
        while n in taps:
            n = randint(2, 39)
        taps.append(n)
    assert len(taps) == 10
    flag_chunks = [int.from_bytes(flag[_:_+5], 'big') for _ in range(0, len(flag), 5)]
    print("LFSR'd Flag:")
    for chunk in flag_chunks:
        ct = lfsr(chunk, 40, taps, 40)
        assert ct != chunk
        print(f"{ct}")


if __name__ == '__main__':
    main()
