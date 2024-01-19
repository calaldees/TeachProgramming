import asyncio
import json

from aiohttp import web, WSCloseCode, WSMsgType

websockets = set()
data = {
    'harry': {'lat':0, 'lon':0},
}

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    websockets.add(ws)
    print('websocket connection open')
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            msg_data = json.loads(msg.data)
            data[msg_data.get('name', 'Unknown')] = msg_data
        elif msg.type == WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())
    print('websocket connection closed')
    websockets.remove(ws)
    return ws


async def send_websocket_timed_state():
    print("send_websocket_timed_state")
    while True:
        #print(f'WebSockets: {len(websockets)}')
        for ws in tuple(websockets):
            await ws.send_str(json.dumps(data))
        await asyncio.sleep(1)

async def on_startup(app):
    print('on_startup')
    asyncio.create_task(send_websocket_timed_state())
async def on_shutdown(app):
    print('on_shutdown')
    for ws in tuple(websockets):
        await ws.close(code=WSCloseCode.GOING_AWAY, message='shutdown')

async def index(request):
    return web.FileResponse('./index.html')

app = web.Application()
app.add_routes([
        web.get('/', index),
        web.get('/ws', websocket_handler),
])
app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

if __name__ == '__main__':
    web.run_app(app, port=8000)
