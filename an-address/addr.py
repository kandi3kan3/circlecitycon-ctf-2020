#!/usr/bin/env python3
from PIL import Image


def glyph_value(glyph):
    # The glyphs have eight lines that can be connected to represent whether
    # a bit is set or unset.

    # ......
    # .@6@..
    # .5.7..
    # .@4@2@
    # ...1.3
    # ...@0@
    alignment = [
        (1, 1),
        (1, 3),
        (3, 1),
        (3, 3),
        (3, 5),
        (5, 3),
        (5, 5),
    ]
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

    # Ensure the glyph has the padding pixels
    for i in range(6):
        if not glyph.getpixel((0, i)) or not glyph.getpixel((i, 0)):
            return None

    # Ensure the glyph has the alignment pixels
    for pos in alignment:
        if glyph.getpixel(pos):
            return None

    value = 0
    for pos in bits:
        value <<= 1
        if not glyph.getpixel(pos):
            value |= 1

    return value


def read_block(image, x, y):
    curr_x, curr_y = x, y

    block = bytearray()
    while True:
        # Get the next glyph on the line
        glyph = image.crop((curr_x, curr_y, curr_x + 6, curr_y + 6))
        value = glyph_value(glyph)

        # Check for end of line or block
        if not value:
            # Failed to read at beginning of line - end of block or error
            if not block or block[-1] == ord('\n'):
                break

            block.append(ord('\n'))
            curr_x = x
            curr_y += 6
            continue

        block.append(value)
        curr_x += 6

    return block


im = Image.open('Address.png').convert('1')
print(read_block(im, 0, 0).decode('utf-8'))
print(read_block(im, 0, 40).decode('utf-8'))
print(read_block(im, 0, 80).decode('utf-8'))
print(read_block(im, 0, 120).decode('utf-8'))
print(read_block(im, 0, 160).decode('utf-8'))
print(read_block(im, 0, 200).decode('utf-8'))
print(read_block(im, 0, 240).decode('utf-8'))
print(read_block(im, 0, 281).decode('utf-8'))
