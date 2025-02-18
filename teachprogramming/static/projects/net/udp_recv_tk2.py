GRID_SIZE=100
WIDTH=5
HEIGHT=4

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5005))

import tkinter
root = tkinter.Tk()
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=GRID_SIZE*WIDTH, height=GRID_SIZE*HEIGHT)
canvas.pack()

#for x in range(WIDTH):
#    canvas.create_line(x*GRID_SIZE, 0, x*GRID_SIZE, HEIGHT*GRID_SIZE, fill="black", width=4)
#for y in range(HEIGHT):
#    canvas.create_line(0, y*GRID_SIZE, WIDTH*GRID_SIZE, y*GRID_SIZE, fill="black", width=4)

for y in range(HEIGHT):
    for x in range(WIDTH):
        canvas.create_rectangle(x*GRID_SIZE, y*GRID_SIZE, (x+1)*GRID_SIZE, (y+1)*GRID_SIZE, outline='black', width=4)
        canvas.create_text(x*GRID_SIZE+GRID_SIZE/2, y*GRID_SIZE+GRID_SIZE/2, text=f'{x},{y}', fill='black')

def recv_msg(x,y,fill):
    #canvas.delete(tkinter.ALL)
    #print(f'{x=},{y=},{fill=}')
    x, y = int(x)*GRID_SIZE, int(y)*GRID_SIZE
    if fill == 'X':
        canvas.create_line(x,y,x+GRID_SIZE,y+GRID_SIZE, fill="red", width=4)
        canvas.create_line(x,y+GRID_SIZE,x+GRID_SIZE,y, fill="red", width=4)
    elif fill == 'O':
        canvas.create_oval(x, y, x+GRID_SIZE, y+GRID_SIZE, outline='blue', width=4)
    else:
        canvas.create_rectangle(x, y, x+GRID_SIZE, y+GRID_SIZE, fill=fill)
    canvas.update()

def recv():
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"received bytes: {data} from {addr}")
        recv_msg(*data.decode('utf8').strip().split(','))

import threading
thread = threading.Thread(target=recv)
thread.daemon=True
thread.start()

root.mainloop()
