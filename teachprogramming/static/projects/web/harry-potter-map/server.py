import asyncio
import json
from collections import defaultdict
import random

from aiohttp import web, WSCloseCode, WSMsgType

import logging
log = logging.getLogger(__name__)

websockets = set()
data = defaultdict(list)

# Fake Harry - can be removed later
data['Harry'] += [{'lat':100, 'lon':100, 'count':0},{'lat':120, 'lon':120, 'count':1}, {'lat':130, 'lon':130, 'count':2}]
def move_fake_harry():
    data['Harry'][:] = data['Harry'][-2:]
    ii = dict(data['Harry'][-1])
    ii['lat'] += random.randint(0,10)
    ii['lon'] += random.randint(0,10)
    ii['count'] += 1
    data['Harry'].append(ii)


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    websockets.add(ws)
    log.info('websocket connection open')
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            msg = json.loads(msg.data)
            name_items = data[msg.get('name', 'Unknown')]
            name_items[:] = name_items[-2:]
            name_items.append(msg)
        elif msg.type == WSMsgType.ERROR:
            log.error('ws connection closed with exception %s' % ws.exception())
    log.info('websocket connection closed')
    websockets.remove(ws)
    return ws

async def send_websocket_timed_state():
    log.info("send_websocket_timed_state")
    while True:
        move_fake_harry()  # Temp - remove later
        data_str = json.dumps(data)
        for ws in tuple(websockets):
            await ws.send_str(data_str)
        await asyncio.sleep(2)

async def on_startup(app):
    log.info('on_startup')
    task = asyncio.create_task(send_websocket_timed_state())
    # TODO - if an exception is raised by the task, it never appears, it's gobbled up. Maybe set a default handler?
async def on_shutdown(app):
    log.info('on_shutdown')
    for ws in tuple(websockets):
        await ws.close(code=WSCloseCode.GOING_AWAY, message='shutdown')

async def index(request):
    return web.FileResponse('./index.html')

app = web.Application()
app.add_routes([
        web.get('/', index),
        web.get('/ws', websocket_handler),
        web.static('/static', './static'),
])
app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    web.run_app(app, port=8000)
