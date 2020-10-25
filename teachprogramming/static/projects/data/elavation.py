"""
Elavation

http://www.shadedrelief.com/natural3/pages/extra.html
https://karczmarczuk.users.greyc.fr/TEACH/Imagerie.old/Images/elev_bump_8k.jpg
"""
from PIL import Image

IMAGE_FILENAME = './elev_bump_8k.jpg'

SEA_LEVEL_BASE = 24
CROP_UNITED_KINGDOM = (3850, 700, 4150, 950)

image_src = Image.open(IMAGE_FILENAME)
image_src = image_src.crop(CROP_UNITED_KINGDOM)
image_des = Image.new('RGB', (image_src.width, image_src.height), 0x000000)

sea_level = 10

# TODO - sea_level to meters function
for y in range(image_src.height):
    for x in range(image_src.width):
        land_height = image_src.getpixel((x, y))  # Greyscale image so we get 0->255 back from getpixel
        if land_height - sea_level > SEA_LEVEL_BASE:  # >= 24 for seeing jpeg artefacting
            c = (0, 255, 0)
        else:
            c = (0, 0, 255)
        image_des.putpixel((x, y), c)

image_des.show()
