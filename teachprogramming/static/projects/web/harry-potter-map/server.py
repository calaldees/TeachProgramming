from aiohttp import web


# https://docs.aiohttp.org/en/stable/#server-example
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

# https://docs.aiohttp.org/en/stable/web_quickstart.html#websockets
async def websocket_handler(request):
    print('websocket connection open')
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())
    print('websocket connection closed')
    return ws

# https://stackoverflow.com/a/43009754/3356840
async def index(request):
    return web.FileResponse('./index.html')

app = web.Application()
app.add_routes([
        web.get('/', index),
        web.get('/ws', websocket_handler),
        web.get('/{name}', handle),
])

if __name__ == '__main__':
    web.run_app(app, port=8000)
