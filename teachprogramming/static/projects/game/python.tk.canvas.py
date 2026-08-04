import pygame

import random
import tkinter
from tkinter import messagebox

class Whack():
    def __init__(self, width=300, height=300):
        self.width, self.height = width, height

        self.root = tkinter.Tk()
        self.root.resizable(False, False)
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        self.num_clicks = 0

        self.root.bind('<ButtonPress>', self.click)
        self.root.mainloop()

    def click(self, event):
        self.num_clicks = self.num_clicks + 1
        x = event.x
        y = event.y
        c = self.num_clicks
        col = '#'+(''.join(hex(num).replace('0x','') for num in (c % 16, 0, 0)))
        col = random.choice(('red', 'green', 'blue', 'yellow'))
        # Face
        self.canvas.create_oval(x, y, x+100, y+100, fill=col, outline='blue')
        # Left eye
        self.canvas.create_oval(x+20, y+20, x+20+10, y+10,fill='#ff0', outline='blue')
        self.canvas.create_line(x+10, y+10, x+40, y+10+c)
        # Right eye
        self.canvas.create_oval(x+60, y+20, x+60+10, y+10,fill='#ff0', outline='blue')
        # Mouth
        self.canvas.create_oval(x+40-c, y+60-c, x+40+20+c, y+60+20+c, fill='#fff', outline='blue')

        #self.canvas.create_rectangle(x, y, x+c*10, y+c*10,outline="#fb0", fill="#fb0")

Whack()
