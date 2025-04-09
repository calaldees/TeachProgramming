import tkinter
from math import floor
import socket            # VER: recv
import threading         # VER: recv

class TicTacToe():
    def __init__(self, grid_size=100, width=5, height=4, addr_to='127.0.0.1'):
        self.grid_size = grid_size
        self.width = width
        self.height = height
        self.addr_to = (addr_to, 5005)

        self.root = tkinter.Tk()
        self.root.resizable(False, False)
        self.canvas = tkinter.Canvas(self.root, width=grid_size*width, height=grid_size*height)
        self.canvas.pack()
                                                                       # VER: recv
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # VER: recv
        #self.sock.bind(('0.0.0.0', 5005))                             # VER: recv NOT 2players
        try:                                                           # VER: 2players
            self.sock.bind(('0.0.0.0', 5005))                          # VER: 2players
        except OSError as ex:                                          # VER: 2players
            print('cant bind socket - is another client is already running on this port?')  # VER: 2players
            self.sock.sendto(b'', self.addr_to)              # VER: 2players
                                                                       # VER: recv
        thread = threading.Thread(target=self.recv)                    # VER: recv
        thread.daemon=True                                             # VER: recv
        thread.start()                                                 # VER: recv
                                                                       # VER: mouse
        self.root.bind('<ButtonPress>', self.mouse_click)              # VER: mouse
                                                                       # VER: mouse
        #self.fill = 'black'                                           # VER: mouse NOT 2players
        self.fill = 'O'                                                          # VER: 2players
                                                                       # VER: draw_grid
        self.grid = ['' for i in range(self.width*self.height)]        # VER: local_state
        self.draw_grid()                                               # VER: draw_grid

        self.root.mainloop()
                                                                                # VER: mouse
    def mouse_click(self, event):                                               # VER: mouse
        x, y = floor(event.x/self.grid_size), floor(event.y/self.grid_size)     # VER: mouse
        data = ','.join(map(str,(x,y,self.fill))).encode('utf8')                # VER: mouse NOT local_state
        if (not any(self.grid)):                                                # VER: 2players
            self.fill = 'X'                                                     # VER: 2players
        self.grid[x+y*self.width] = self.fill                                   # VER: local_state
        data = ','.join(self.grid).encode('utf8')                               # VER: local_state
        self.sock.sendto(data, self.addr_to)                                    # VER: mouse
        self.draw_grid()                                                        # VER: local_state
                                                    # VER: draw_grid
    def draw_grid(self):                            # VER: draw_grid
        self.canvas.delete(tkinter.ALL)             # VER: local_state
        s = self.grid_size                          # VER: draw_grid
        for y in range(self.height):                # VER: draw_grid
            for x in range(self.width):             # VER: draw_grid
                fill = self.grid[x+y*self.width]                                                 # VER: local_state
                if fill == 'X':                                                                  # VER: 2players
                    self.canvas.create_line(x*s, y*s, (x+1)*s, (y+1)*s, fill="red", width=4)     # VER: 2players
                    self.canvas.create_line(x*s, (y+1)*s, (x+1)*s, y*s, fill="red", width=4)     # VER: 2players
                elif fill == 'O':                                                                # VER: 2players
                    self.canvas.create_oval(x*s, y*s, (x+1)*s, (y+1)*s, outline='blue', width=4) # VER: 2players
                else:                                                                            # VER: 2players
                #if fill:                                                                # VER: local_state NOT 2players
                    self.canvas.create_rectangle(x*s, y*s, (x+1)*s, (y+1)*s, fill=fill)  # VER: local_state
                self.canvas.create_rectangle(x*s, y*s, (x+1)*s, (y+1)*s, outline='black', width=4)   # VER: draw_grid
                #self.canvas.create_text(x*s+s/2, y*s+s/2, text=f'{x},{y}', fill='black')            # VER: draw_grid NOT 2players
        self.canvas.update()                                                                         # VER: draw_grid
                                                                    # VER: recv
    def recv(self):                                                 # VER: recv
        while True:                                                 # VER: recv
            data, self.addr_to = self.sock.recvfrom(1024)           # VER: recv
            print(f"received bytes: {data} from {self.addr_to}")    # VER: recv
            data = data.decode('utf8').strip().split(',')           # VER: recv_draw
            if not any(data):                                       # VER: 2players
                continue                                            # VER: 2players
                                                                    # VER: recv_draw
            #x, y, fill = int(data[0]), int(data[1]), data[2]                    # VER: recv_draw NOT local_state
            #s = self.grid_size                                                  # VER: recv_draw NOT local_state
            #self.canvas.create_rectangle(x*s, y*s, (x+1)*s, (y+1)*s, fill=fill) # VER: recv_draw NOT local_state
            self.grid[:] = data   # VER: local_state
            self.draw_grid()      # VER: local_state

if __name__ == '__main__':
    import sys                         # VER: commandline
    if len(sys.argv) == 1:             # VER: commandline
        sys.argv.append('127.0.0.1')   # VER: commandline
    TicTacToe(addr_to=sys.argv[1])     # VER: commandline
    #TicTacToe()                        # VER: commandline NOT_
