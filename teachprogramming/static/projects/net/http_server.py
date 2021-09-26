"""
Basic HTTP file server using raw sockets
"""

import socket
import re
import os
import sys


import logging
log = logging.getLogger(__name__)


# Commandline root path - (This is Jankey global rubbish - do not architect code like this!)
if len(sys.argv) == 1:
    sys.argv.append('.')
assert len(sys.argv) == 2, f"Usage: python3 ${__file__} PATH_TO_SERVE"
PATH = sys.argv[1]
assert os.path.isdir(PATH), f"{PATH} should be a dir"



def http_server(data_in):
    data_in = data_in.decode('utf8')
    log.debug(data_in)
    response_headers = [
        b'HTTP/1.0 200 OK',
    ]
    data_out = b''
    if match := re.match(r'GET (.*) HTTP/\d', data_in):
        path = match.group(1).replace('%20', ' ').split('?')[0].strip('/')
        path_actual = os.path.join(PATH, path)
        log.info(f"{path=} - {path_actual=}")
        if os.path.isdir(path_actual):
            html_body = ''.join(
                f"<li><a href='{os.path.join(path,i)}'>{os.path.join(path,i)}</a></li>" 
                for i in os.listdir(path_actual)
            )
            data_out = f"<html><head><title>MiniServer</title></head><body><ul>{html_body}</ul></body></html>".encode('utf8')
            response_headers.append(b'Content-type: text/html; charset=utf-8')
        if os.path.isfile(path_actual):
            with open(path_actual, 'rb') as filehandle:
                data_out = filehandle.read()
    return b'\r\n'.join(response_headers + [b'', data_out])

def serve_app(func_app, port=8000, host=''):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        while True:
            s.listen()
            try:
                conn, addr = s.accept()
            except KeyboardInterrupt as ex:
                break
            with conn:
                log.info(f"request from {addr}")
                data_in = conn.recv(65535)
                data_out = func_app(data_in)
                conn.send(data_out)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve_app(http_server)