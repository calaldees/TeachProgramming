from aiohttp import web, WSCloseCode

websockets = set()

# https://docs.aiohttp.org/en/stable/#server-example
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

# https://docs.aiohttp.org/en/stable/web_quickstart.html#websockets
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    websockets.add(ws)
    print('websocket connection open')
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())
    print('websocket connection closed')
    websockets.remove(ws)
    return ws


async def send_websocket_timed_state(app):
    print("send_websocket_timed_state")
    return

async def on_shutdown(app):
    print('shutdown')
    for ws in tuple(websockets):
        await ws.close(code=WSCloseCode.GOING_AWAY, message='shutdown')

# https://stackoverflow.com/a/43009754/3356840
async def index(request):
    return web.FileResponse('./index.html')

app = web.Application()
app.add_routes([
        web.get('/', index),
        web.get('/ws', websocket_handler),
        web.get('/{name}', handle),
])
app.on_startup.append(send_websocket_timed_state)
app.on_shutdown.append(on_shutdown)

if __name__ == '__main__':
    web.run_app(app, port=8000)
