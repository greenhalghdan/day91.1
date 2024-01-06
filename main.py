import numpy
from PIL import Image
from collections import Counter
import requests


def rgb_to_hex(r, g, b):
    ans = ('{:X}{:X}{:X}').format(r, g, b)
    while len(ans) < 6:
        ans = "0" + ans
    return ans


def top_10(hexcodes):
    hexcodesdict = {}
    for code in hexcodes:
        if code in hexcodesdict:
            count = hexcodesdict[code]
            hexcodesdict[code] = count + 1
        else:
            hexcodesdict[code] = 1
    counter = Counter(hexcodesdict)
    dict_to_list = list(dict(counter.most_common(100)).keys())
    top_10_colors = []

    for colour in dict_to_list:
        response = requests.get(url=f'https://www.thecolorapi.com/id?hex={colour}')
        if dict(response.json())['name']['value'] not in top_10_colors:
            top_10_colors.append(dict(response.json())['name']['value'])
        if len(top_10_colors) == 10:
            return top_10_colors
    return top_10_colors


image = Image.open('index.jpeg')
array = numpy.array(image)
shape = array.shape

x = shape[0]
y = shape[1]
hex_list = []


for x in range(x):
    for y in range(y):
        rgb = array[x, y, :]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        hex_list.append(rgb_to_hex(r, g, b))

print(f'The top 10 colours are: {top_10(hex_list)}')