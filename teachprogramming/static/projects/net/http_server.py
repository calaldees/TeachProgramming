"""
Basic HTTP file server using raw sockets
"""

import socket
import re
import os


import logging
log = logging.getLogger(__name__)

PATH = '.'


def http_server(data_in):
    data_in = data_in.decode('utf8')
    response_headers = [
        b'HTTP/1.0 200 OK',
    ]
    data_out = b''
    if match := re.match('GET (.*) HTTP/1.1', data_in):
        path = PATH + match.group(1).replace('%20', ' ')
        log.info(f"{path=}")
        if os.path.isdir(path):
            html_body = ''.join(
                f"<li><a href='{path}{i}'>{path}{i}</a></li>" 
                for i in os.listdir(path)
            )
            data_out = f"<html><head><title>MiniServer</title></head><body><ul>{html_body}</ul></body></html>".encode('utf8')
            response_headers.append(b'Content-type: text/html; charset=utf-8')
        if os.path.isfile(path):
            with open(path, 'rb') as filehandle:
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