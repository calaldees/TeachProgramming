"""
Inspired by https://web.stanford.edu/class/cs101/image-5-puzzles.html

curl -O "https://web.stanford.edu/class/cs101/puzzle-gold.png"
"""

from PIL import Image  # `pip3 install pillow`  # https://pillow.readthedocs.io/

image_src = Image.open('puzzle-gold.png')
image_des = Image.new('RGB', (image_src.width, image_src.height), 0x000000)

for y in range(image_src.height):
    for x in range(image_src.width):
        r,g,b,a = image_src.getpixel((x, y))
        r = r * 10
        image_des.putpixel((x, y), (r,r,r))

image_des.save('puzzle-gold.out.png')

# TODO: Now make an enoder?
