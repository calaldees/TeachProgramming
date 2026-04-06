import random
import tkinter
from time import time
from tkinter import messagebox

class Whack():
    def __init__(self, width=300, height=300, ball_size=20, click_count=10):
        self.width, self.height = width, height

        self.root = tkinter.Tk()
        self.root.resizable(False, False)
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        self.root.bind('<ButtonPress>', self.click)

        self.ball_size = ball_size
        self.click_count = click_count

        self.reset()
        self.root.mainloop()

    def reset(self):
        messagebox.showinfo("Whack", "Ready to begin")
        self.clicks = 0
        self.start_time = time()
        self.hop()

    def hop(self):
        self.ball_x = random.randint(0, self.width)
        self.ball_y = random.randint(0, self.height)

        c = self.canvas
        c.delete(tkinter.ALL)
        c.create_rectangle(
            self.ball_x, self.ball_y,
            self.ball_x+self.ball_size, self.ball_y+self.ball_size,
            outline="#fb0", fill="#fb0"
        )
        c.update()

    def click(self, event):
        # c.create_rectangle(event.x, event.y, event.x+20, event.y+20, outline="#fb0", fill="#fb0")

        inside_ball = (
            event.x >= self.ball_x and
            event.x <= self.ball_x + self.ball_size and
            event.y >= self.ball_y and
            event.y <= self.ball_y + self.ball_size
        )
        if inside_ball:
            self.clicks += 1
            print(f'Hit! {self.clicks}')
            self.hop()
        else:
            print('Missed')

        if self.clicks >= self.click_count:
            time_taken = time() - self.start_time
            messagebox.showinfo(
                "Whack",
                f"You clicked {self.click_count} times in {time_taken:.2f} seconds"
            )
            self.reset()

Whack()