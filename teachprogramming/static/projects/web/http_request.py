import socket
address = ("calaldees.uk", 80)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
sock.connect(address)
sock.sendall(b'''GET / HTTP/1.1\r\nHost: calaldees.uk\r\nUser-Agent: curl/7.81.0\r\nAccept: */*\r\n\r\n''')
while True:
    response = sock.recv(65535)
    if not response:
        break
    print(response.decode())
sock.close()
