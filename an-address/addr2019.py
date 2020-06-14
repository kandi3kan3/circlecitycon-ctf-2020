#!/usr/bin/env python3
from PIL import Image

im = Image.open("Address.png")
im.convert('RGB')
im.load()



glyph_start = ord('!')

found_glyphs = []

def glyphstring(img):
    re = ''
    badtime = False
    for i in range(6):
        for j in range(6):
            re += ('#' if img.getpixel((j, i))[0] < 20 else '.')
            if i > 2 and re[-1] == '#' and '#' not in re[:-1]:
                badtime = True
        re += '\n'
    return (re if '#' in re else None, badtime)


def find_from(start_pt):
    my_start_pt = start_pt
    my_arr = [[]]
    while True:
        subimg = im.crop((my_start_pt[0], my_start_pt[1], my_start_pt[0] + 6, my_start_pt[1] + 6))
        st, badtime =glyphstring(subimg)
        if badtime:
            return my_arr
        if st is None and my_start_pt[0] < 50:
            return my_arr
        if st is not None:
            if not st.startswith('......'):
                for i, g in enumerate(found_glyphs):
                    print(i)
                    print(g)
                print(my_start_pt)
                __import__('pdb').set_trace()
            if st not in found_glyphs:
                found_glyphs.append(st)
            stindx = found_glyphs.index(st)
            my_arr[-1] += [chr(stindx + glyph_start)]
        my_start_pt = (my_start_pt[0] + 6, my_start_pt[1])
        if my_start_pt[0] + 6 >= im.size[0]:
            my_start_pt = (start_pt[0], my_start_pt[1] + 6)
            my_arr += [[]]
        if my_start_pt[1] + 6 > im.size[1]:
            return my_arr



result = find_from((0,0))
result += find_from((0, 40))
result += find_from((0, 80))
result += find_from((0, 120))
result += find_from((0, 160))
result += find_from((0, 200))
result += find_from((0, 240))
result += find_from((0, 281))
for i, g in enumerate(found_glyphs):
    print(i)
    print(g)

for block in result:
    print(''.join(block))
