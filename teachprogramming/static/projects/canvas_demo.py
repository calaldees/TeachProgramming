from tkinter import Tk, Canvas, ALL
import time


class TkAnimationFrame():
    def __init__(self, width=640, height=480, frames_per_second=30):
        self.frames_per_second = frames_per_second
        self.root = Tk()
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.startup()
        self.animation_thread()
        self.root.mainloop()

    def animation_thread(self):
        frame = 0
        while True:
            self.animation_frame(frame)
            frame += 1
            self.canvas.update()
            time.sleep(1/self.frames_per_second)
            self.canvas.delete(ALL)

    def startup(self):
        """
        https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        """
        pass

    def animation_frame(self, frame):
        """
        http://zetcode.com/gui/tkinter/drawing/
        """
        raise Exception('Please override animation_frame')


class AnimationDemo(TkAnimationFrame):
    def startup(self):
        """
        """
        super().startup()
        self.root.bind("<Key>", lambda event: print(event.char))
        def click(event):
            print(event.x)
        def motion(event):
            print(event.y)
        self.canvas.bind("<Button-1>", click)
        self.canvas.bind('<Motion>', motion)

    def animation_frame(self, frame):
        c = self.canvas
        t = frame % c.winfo_height()
        c.create_line(t, t, t+10, t+10)

        t = frame % c.winfo_width()
        c.create_rectangle(t, 10, t+120, 80, outline="#fb0", fill="#fb0")

        x = self.root.winfo_pointerx() - self.root.winfo_rootx()
        y = self.root.winfo_pointery() - self.root.winfo_rooty()
        c.create_rectangle(x, y, x+20, y+20, outline="#ff0", fill="#ff0")


AnimationDemo()
