import socket


# from - https://wiki.python.org/moin/UdpCommunication

addr = ("127.0.0.1", 5005)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ---

sock.sendto(b"Hello, World!", addr)


# ---

# TODO - UDP receive in thread? queue? read?

sock.bind(addr)
while True:
    data, addr = sock.recvfrom(1024)
    print(f"received bytes: {data}")
