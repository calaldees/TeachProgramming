GRID_SIZE=80
WIDTH=7
HEIGHT=7

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5005))

import tkinter
root = tkinter.Tk()
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=GRID_SIZE*WIDTH, height=GRID_SIZE*HEIGHT)
canvas.pack()

for x in range(WIDTH):
    canvas.create_line(x*GRID_SIZE, 0, x*GRID_SIZE, HEIGHT*GRID_SIZE, fill="black", width=4)
for y in range(HEIGHT):
    canvas.create_line(0, y*GRID_SIZE, WIDTH*GRID_SIZE, y*GRID_SIZE, fill="black", width=4)

def recv_msg(x,y,fill):
    x, y = int(x)*GRID_SIZE, int(y)*GRID_SIZE
    canvas.create_rectangle(x,y,x+GRID_SIZE,y+GRID_SIZE, fill=fill)
    canvas.update()

def recv():
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"received bytes: {data} from {addr}")
        try:
            recv_msg(*data.decode('utf8').strip().split(','))
        except Exception as ex:
            print(ex)

import threading
thread = threading.Thread(target=recv)
thread.daemon=True
thread.start()

root.mainloop()
