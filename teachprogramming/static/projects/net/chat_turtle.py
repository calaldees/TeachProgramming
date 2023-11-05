import turtle
t = turtle.Pen()


def handle_message(data):                                      # NEW
    if not data.startswith("Yourname: "):                      # NEW
        return                                                 # NEW
    command, value = data.strip().replace("Yourname: ", "").split(",") # NEW
    value = float(value)                                       # NEW
    getattr(t, command)(value)                                 # NEW



# Boilerplate for receiving network messages

import socket, threading
address = ("45.152.210.188", 9801)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

def connection(sock):
    while True:
        data_recv = sock.recv(4098)
        if not data_recv:
            break
        try:                                          # NEW
            handle_message(data_recv.decode('utf8'))  # NEW
        except:                                       # NEW
            import traceback                          # NEW
            traceback.print_exc()                     # NEW
    sock.close()

thread = threading.Thread(target=connection, args=(sock,))
thread.daemon=True
thread.start()

turtle.TK.mainloop()      # NEW
