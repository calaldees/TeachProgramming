from urllib.parse import parse_qs
from pathlib import Path

from aiohttp import web
from PIL import Image

import logging
log = logging.getLogger(__name__)

PATH_FONT = Path('static/font.gif')


def hex_to_image_data(hex_str):
    """
    >>> dd = hex_to_image_data('0000000000000000')
    >>> dd == (False,)*64
    True
    >>> dd = hex_to_image_data('ffffffffffffffff')
    >>> dd == (True,)*64
    True
    >>> hex_to_image_data('ffffffffffffffa5')[:8]
    (True, False, True, False, False, True, False, True)
    """
    assert len(hex_str) == 16, f'hex string must be 16 chars to complete a 8x8 mono image - got {len(hex_str)}:{hex_str}'
    n = int(hex_str, 16)
    return tuple(bool((n >> i) & 1) for i in range(64))

def put_image_data(img, data, offset_x):
    for i, d in enumerate(data):
        x, y = (7-(i%8))+offset_x, 7-(i//8)  # `7-` flips y and x
        img.putpixel((x, y), (255,255,255,255 if d else 0))  # white pixel that is either solid or fully transparent

async def add_font(request):
    qs = {k:''.join(v) for k,v in parse_qs(request.query_string).items()}
    img = Image.open(PATH_FONT).convert(mode='RGBA') if PATH_FONT.exists() else Image.new('RGBA', (2048,8), (255,255,255,0))
    put_image_data(img=img, data=hex_to_image_data(qs['data']), offset_x=ord(qs['letter'])*8)
    img.save(PATH_FONT)
    return web.Response(text="add_font")

async def index(request):
    return web.FileResponse('./index.html')

app = web.Application()
app.add_routes([
        web.get('/', index),
        web.get('/add_font', add_font),
        web.static('/static', './static'),
])



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, port=8000)



# TODO: Future error handling?
# https://docs.aiohttp.org/en/stable/web_advanced.html#example
# @web.middleware
# async def error_middleware(request, handler):
#     try:
#         response = await handler(request)
#         if response.status != 404:
#             return response
#         message = response.message
#     except web.HTTPException as ex:
#         if ex.status != 404:
#             raise
#         message = ex.reason
#     return web.json_response({'error': message})
# app.middlewares.append(error_middleware)

