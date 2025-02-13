import socket   # VER: network_udp_send,network_udp_recv

def udp_send_recv():
    """
    based on - https://wiki.python.org/moin/UdpCommunication
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # VER: network_udp_send,network_udp_recv

    addr = ("127.0.0.1", 5005)               # VER: network_udp_send
    sock.sendto(b"Hello, World!", addr)      # VER: network_udp_send
    print(f'Bound to {sock.getsockname()}')  # VER: network_udp_send

    class MockSocket():
        def recvfrom(*args, **kwargs):
            return (None, None)
        def bind(*args, **kwargs):
            pass
    sock = MockSocket()   # comment this out to run it for real

    #sock.bind(('0.0.0.0', 5005))                      # VER: network_udp_recv
    while True:                                        # VER: network_udp_recv
        data, addr = sock.recvfrom(1024)               # VER: network_udp_recv
        print(f"received bytes: {data} from {addr}")   # VER: network_udp_recv
        if not data:
            break
    # TODO - UDP receive in thread? queue? read?

if __name__ == '__main__':
    udp_send_recv()
