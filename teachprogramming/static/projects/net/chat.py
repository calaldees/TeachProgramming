import socket, threading, time
                            # VER: gui
import tkinter              # VER: gui
import tkinter.scrolledtext # VER: gui_recv
                                                      # VER: recv
def connection(sock):                                 # VER: recv
    while True:                                       # VER: recv
        data_recv = sock.recv(4098)                   # VER: recv
        if not data_recv:                             # VER: recv
            break                                     # VER: recv
        #print(data_recv)                             # VER: recv not gui_recv
        output_box.insert(tkinter.END, data_recv)     # VER: gui_recv
        output_box.yview(tkinter.END)                 # VER: gui_scroll
    sock.close()                                      # VER: recv

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9872))
#connection(sock)                                          # VER: recv not send_recv
                                                           # VER: send_recv
thread = threading.Thread(target=connection, args=(sock,)) # VER: send_recv
thread.daemon=True                                         # VER: send_recv
thread.start()                                             # VER: send_recv
                                                                          # VER: gui
root = tkinter.Tk()                                                       # VER: gui
root.title("Chat Client")                                                 # VER: gui
output_box = tkinter.scrolledtext.ScrolledText(root, width=40, height=15) # VER: gui_recv
output_box.pack(fill=tkinter.BOTH, expand=1)                              # VER: gui_recv
input_box = tkinter.Entry(root)                                           # VER: gui
input_box.pack(fill=tkinter.BOTH)                                         # VER: gui
def handle_user_input(e):                                                 # VER: gui
    #sock.sendall((input_box.get()+'\n').encode('utf-8'))                 # VER: gui not gui_username
    sock.sendall(('Yourname: '+input_box.get()+'\n').encode('utf-8'))     # VER:         gui_username
    input_box.delete(0, tkinter.END)                                      # VER: gui
input_box.bind("<KeyRelease-Return>", handle_user_input)                  # VER: gui
input_box.focus_set()                                                     # VER: gui
                                                                          # VER: gui
root.mainloop()                                                           # VER: gui

#sock.sendall(bytes('Hello I am Bob'+"\n",'utf-8'))   # VER: send_one not gui
#while True:                                          # VER: send     not gui
#    sock.sendall(bytes(input()+"\n",'utf-8'))        # VER: send     not gui
#