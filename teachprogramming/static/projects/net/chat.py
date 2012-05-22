#!/usr/bin/python
import socket, threading, time

try:
    import tkinter
    import tkinter.scrolledtext
except ImportError as e:
    import Tkinter as tkinter
    

running = True

def connection(sock):
    while running:
        data_recv = sock.recv(4098)
        if not data_recv:
            break
        #print(data_recv)
        output_box.insert(tkinter.END, data_recv)
        #output_box.insert(tkinter.END, '\n')
        output_box.yview(tkinter.END)
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9872))
thread = threading.Thread(target=connection, args=(sock,))
thread.daemon=True
thread.start()

root = tkinter.Tk()
root.title("Chat Client")

output_box = tkinter.scrolledtext.ScrolledText(root, width=40, height=15)
output_box.pack(fill=tkinter.BOTH, expand=1)

input_box = tkinter.Entry(root)
input_box.pack(fill=tkinter.BOTH)
def handle_user_input(e):
    sock.sendall((input_box.get()+"\n").encode('utf-8'))
    input_box.delete(0, tkinter.END)
input_box.bind("<KeyRelease-Return>", handle_user_input)
input_box.focus_set()

root.mainloop()

#try:
#    while True:
#        sock.sendall(raw_input()+"\n")
#finally:
#    sock.close()
#    running = False
