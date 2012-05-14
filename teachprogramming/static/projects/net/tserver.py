#!/usr/bin/env python

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.websocket import WebSocketHandler

class Handler(WebSocketHandler):
        def open(self):
            print "New connection opened."

        def on_message(self, message):
                print message


        def on_close(self):
                print "Connection closed."

print "Server started."
HTTPServer(Application([("/", Handler)])).listen(1024)
IOLoop.instance().start()
