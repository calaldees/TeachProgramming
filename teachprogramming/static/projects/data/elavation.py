"""
Elavation
How much of the UK will be flooded when the sea level rises?

Earth land height data - a greyscale image
Download (place in script folder)
http://shadedrelief.com/natural3/ne3_data/8192/elev_bump_8k.jpg
Source Image Reference
http://www.shadedrelief.com/natural3/pages/extra.html

The TIFFs and high ultra high res images will take too long to process in python.
Using the 8k(low res) and UK crop means the processing in python will take 3 seconds on a normal machine.
The jpg will have compression artifacts - this is good disscussion point with students.

You will need to install `pillow` image library (see below)

Extension:
* Have 4 or 5 colours to signify different heights.
    * At first this can be done with `if` statements and then upgraded to a tuple of data.
        * talk about the problems of expressing data as logic (e.g 3+ if statements)
    * Maybe the tuple of data could be loaded from JSON and shared with other students?
* sea_level(0-255) to meters function?

Quick Setup: bash commands
    curl -O "https://raw.githubusercontent.com/calaldees/TeachProgramming/master/teachprogramming/static/projects/data/elavation.py"
    curl  -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" -O "https://shadedrelief.com/natural3/ne3_data/8192/elev_bump_8k.jpg"
    pip3 install pillow
    python3 elavation.py
"""
from PIL import Image  # `pip3 install pillow`  # https://pillow.readthedocs.io/

IMAGE_FILENAME = './elev_bump_8k.jpg'

SEA_LEVEL_BASE = 24  # 0/black is actually below sea level - `24` is the level of the sea for this dataset
CROP_UNITED_KINGDOM = (3850, 700, 4150, 950)

image_src = Image.open(IMAGE_FILENAME)
image_src = image_src.crop(CROP_UNITED_KINGDOM)
image_des = Image.new('RGB', (image_src.width, image_src.height), 0x000000)

sea_level = 2  # change this and see what happens

for y in range(image_src.height):
    for x in range(image_src.width):
        land_height = image_src.getpixel((x, y))  # Greyscale image so we get 0->255
        if land_height - sea_level > SEA_LEVEL_BASE:  # `>=` 24 for seeing jpeg artefacts
            c = (0, 255, 0)
        else:
            c = (0, 0, 255)
        image_des.putpixel((x, y), c)

image_des.show()
#image_des.save('elavation_uk.png')