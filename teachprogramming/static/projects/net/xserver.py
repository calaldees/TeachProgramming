from gevent import monkey; monkey.patch_all()
import gevent

from ws4py.server.geventserver import WebSocketServer
from ws4py.websocket import EchoWebSocket

server = WebSocketServer(('localhost', 9999), websocket_class=EchoWebSocket)
server.serve_forever()