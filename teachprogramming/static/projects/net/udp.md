UDP/IP
===

* UDP/IP is subset (sort of misconception) TCP/IP. TCP is built on top of IP (not UDP)


Mental Model
------------

* When sending UDP you send from a port (like a server), but a random port one is picked for you. Often in 5 digit range. This allows response


`udp_send.py`
```python
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = sys.argv[1].encode('utf8')
addr = ("127.0.0.1", 5005)
sock.sendto(data, addr)
```

`udp_recv.py`
```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('0.0.0.0', 5005))
while True:
    data, addr = sock.recvfrom(1024)
    print(f"received bytes: {data} from {addr}")
```

`udp_recv_tk.py`
```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5005))

import tkinter
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=512, height=512)
canvas.pack()

def recv_msg(*args):
    #canvas.delete(tkinter.ALL)
    canvas.create_rectangle(*args, outline="#F00", fill="#0F0")
    canvas.update()

def recv():
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"received bytes: {data} from {addr}")
        recv_msg(*data.decode('utf8').split(','))

import threading
thread = threading.Thread(target=recv)
thread.daemon=True
thread.start()

root.mainloop()
```

```bash
python3 udp_recv_tk.py
python3 udp_send.py 100,100,200,200
```