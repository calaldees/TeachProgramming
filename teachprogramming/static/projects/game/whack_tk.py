import random
import tkinter
from tkinter import messagebox                                                  # VER: reset
import time                                                                     # VER: time
import socket                                                                   # VER: network_score

class Whack():
    def __init__(self, width=300, height=300):
        self.width, self.height = width, height

        self.root = tkinter.Tk()
        self.root.resizable(False, False)
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)            # VER: network_score
        self.server_addr = ('45.152.210.188', 9802)                             # VER: network_score
                                                                                # VER: network_score
        self.root.bind('<ButtonPress>', self.click)                             # VER: click
        self.click_count = 10                                                   # VER: reset
        self.ball_size = 20                                                     # VER: reset
        self.reset()                                                            # VER: reset
        self.root.mainloop()
                                                                                # VER: reset
    def reset(self):                                                            # VER: reset
        messagebox.showinfo("Whack", "Ready to begin")                          # VER: reset
        self.start_time = time.time()                                           # VER: time
        self.clicks = 0                                                         # VER: click_count
        self.ball_hop()                                                         # VER: ball_hop
                                                                                # VER: ball_hop
    def ball_hop(self):                                                         # VER: ball_hop
        #self.ball_x = random.randint(0, self.width)                            # VER: ball_hop NOT ball_hop_fix
        self.ball_x = random.randint(0, self.width-self.ball_size)              # VER: ball_hop_fix
        #self.ball_y = random.randint(0, self.height)                           # VER: ball_hop NOT ball_hop_fix
        self.ball_y = random.randint(0, self.height-self.ball_size)             # VER: ball_hop_fix
                                                                                # VER: ball_hop
        c = self.canvas                                                         # VER: ball_hop
        c.delete(tkinter.ALL)                                                   # VER: ball_hop
        c.create_rectangle(                                                     # VER: ball_hop
            self.ball_x, self.ball_y,                                           # VER: ball_hop
            self.ball_x+self.ball_size, self.ball_y+self.ball_size,             # VER: ball_hop
            outline="#fb0", fill="#fb0"                                         # VER: ball_hop
        )                                                                       # VER: ball_hop
        c.update()                                                              # VER: ball_hop
                                                                                # VER: click
    def click(self, event):                                                     # VER: click
        inside_ball = (                                                         # VER: inside_ball
            event.x >= self.ball_x and                                          # VER: inside_ball
            event.x <= self.ball_x + self.ball_size and                         # VER: inside_ball
            event.y >= self.ball_y and                                          # VER: inside_ball
            event.y <= self.ball_y + self.ball_size                             # VER: inside_ball
        )                                                                       # VER: inside_ball
        if inside_ball:                                                         # VER: inside_ball
        #if True:                                                               # VER: click NOT inside_ball
            self.clicks += 1                                                    # VER: click_count
            print(f'Hit! {self.clicks}')                                        # VER: click_count
            self.ball_hop()                                                     # VER: ball_hop
            #self.canvas.create_rectangle(                                      # VER: click NOT ball_hop
            #    event.x, event.y,                                              # VER: click NOT ball_hop
            #    event.x+10, event.y+10,                                        # VER: click NOT ball_hop
            #    outline="#fb0", fill="#fb0"                                    # VER: click NOT ball_hop
            #)                                                                  # VER: click NOT ball_hop
        else:                                                                   # VER: inside_ball
            print('Missed')                                                     # VER: inside_ball
                                                                                # VER: click_end
        if self.clicks >= self.click_count:                                     # VER: click_end
            time_taken = time.time() - self.start_time                          # VER: time
            network_data = f'myname:{time_taken:.2f}'.encode('utf8')            # VER: network_score
            self.sock.sendto(network_data, self.server_addr)                    # VER: network_score
            #msg = f"You clicked {self.clicks} times")                          # VER: click_end NOT time
            msg = f"You clicked {self.clicks} times in {time_taken:.2f} seconds"  # VER: time
            messagebox.showinfo("Whack", msg)                                   # VER: click_end
            self.reset()                                                        # VER: click_end

Whack()