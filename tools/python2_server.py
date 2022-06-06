import SimpleHTTPServer
#SimpleHTTPServer.test()

import SocketServer
PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()

# Serve CCCU desktop via http on port 8000
# http://localhost:8000