import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = ("127.0.0.1", 5005)
sock.sendto(sys.argv[1].encode('utf8'), addr)
