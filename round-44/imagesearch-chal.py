import PIL.Image

from math import sqrt
from random import randint, choice
from hexthetextflag import flag, bee_movie_script


def get_colors_from_string(string: str):
    cols = []
    assert not len(string) % 3
    while len(string):
        three, string = string[:3], string[3:]
        cols.append(tuple([ord(_) for _ in three]))
    return cols


def hex_the_text():
    """work the magic"""
    bee_movie_colors = get_colors_from_string(bee_movie_script)
    assert not sqrt(len(bee_movie_colors)) % 1
    size = int(sqrt(len(bee_movie_colors)))
    img = PIL.Image.new(mode="RGB", size=tuple([size] * 2))
    for index, col in enumerate(bee_movie_colors):
        colm, row = divmod(index, size)
        img.putpixel((row, colm), col)
    pos = [randint(0, 123456789), randint(0, 987654321)]
    direction = choice([(-1, 0), (0, 1), (0, -1)])
    flag_colors = get_colors_from_string(flag)
    while len(flag_colors):
        nextcol = flag_colors.pop(0)
        img.putpixel((pos[0] % size, pos[1] % size), nextcol)
        pos[0] += direction[0]
        pos[1] += direction[1]
    img.save("./output.png")


if __name__ == '__main__':
    hex_the_text()
