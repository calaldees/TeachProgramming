import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5005))

import tkinter
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=512, height=512)
canvas.pack()

def recv_msg(x1,y1,x2,y2):
    #canvas.delete(tkinter.ALL)
    canvas.create_rectangle(x1,y1,x2,y2, outline="#F00", fill="#0F0")
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