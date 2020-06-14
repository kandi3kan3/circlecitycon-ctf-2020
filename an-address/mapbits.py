#!/usr/bin/env python3
from PIL import Image


def glyph_value(glyph):
    # ......
    # .@6@..
    # .5.7..
    # .@4@2@
    # ...1.3
    # ...@0@
    bits = [
        (3, 2),
        (2, 1),
        (1, 2),
        (2, 3),
        (5, 4),
        (4, 3),
        (3, 4),
        (4, 5),
    ]

    value = 0
    for pos in bits:
        value <<= 1
        if not glyph.getpixel(pos):
            value |= 1

    return value


def read_line(image, x, y):
    curr_x, curr_y = x, y

    while True:
        # Get the next glyph on the line
        glyph = image.crop((curr_x, curr_y, curr_x + 6, curr_y + 6))
        value = glyph_value(glyph)
        if not value:
            break

        print('{:08b} {:s}'.format(value, chr(value)))
        curr_x += 6


im = Image.open('Address.png').convert('1')
read_line(im, 0, 281)
