import socket, threading, time

def connection(sock):
    while True:
        data_recv = sock.recv(4098)
        print(data_recv)
        #if 'exit' in data_recv:
        #    break
        time.sleep(0)
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9872))
threading.Thread(target=connection, args=(sock,)).start()

while True:
    sock.sendall(raw_input())
