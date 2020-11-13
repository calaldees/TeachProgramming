"""
Elavation

Earth land height data - a greyscale image
http://www.shadedrelief.com/natural3/pages/extra.html
https://karczmarczuk.users.greyc.fr/TEACH/Imagerie.old/Images/elev_bump_8k.jpg

The TIFFs and high ultra high res images will take too long to process in python.
Using the 8k(low res) and UK crop means the processing in python will take 3 seconds on a normal machine.
The jpg will have compression artifacts - this is good disscussion point with students.

Extension:
* Have 4 or 5 colours to signify different heights.
    * At first this can be done with `if` statements and then upgraded to a tuple of data.
        * talk about the problems of expressing data as logic (e.g 3+ if statements)
    * Maybe the tuple of data could be loaded from JSON and shared with other students?
* sea_level(0-255) to meters function?
"""
from PIL import Image  # `pip install pillow`  # https://pillow.readthedocs.io/

IMAGE_FILENAME = './elev_bump_8k.jpg'

SEA_LEVEL_BASE = 24  # 0/black is actually below sea level - `24` is the level of the sea for this dataset
CROP_UNITED_KINGDOM = (3850, 700, 4150, 950)

image_src = Image.open(IMAGE_FILENAME)
image_src = image_src.crop(CROP_UNITED_KINGDOM)
image_des = Image.new('RGB', (image_src.width, image_src.height), 0x000000)

sea_level = 10  # change this and see what happens

for y in range(image_src.height):
    for x in range(image_src.width):
        land_height = image_src.getpixel((x, y))  # Greyscale image so we get 0->255
        if land_height - sea_level > SEA_LEVEL_BASE:  # `>=` 24 for seeing jpeg artefacts
            c = (0, 255, 0)
        else:
            c = (0, 0, 255)
        image_des.putpixel((x, y), c)

image_des.show()
