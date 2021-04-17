import tkinter
import time


class TkAnimationFrame():
    def __init__(self, width=640, height=480, frames_per_second=60):
        self.frames_per_second = frames_per_second

        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        self.input = set()
        self.root.bind("<Key>", lambda event: self.input.add(event.keysym))
        self.root.bind("<KeyRelease>", lambda event: self.input.remove(event.keysym))
        self.mouse_x, self.mouse_y = (0, 0)
        def mouse_motion(event):
            self.mouse_x, self.mouse_y = (event.x, event.y)
        self.root.bind('<Motion>', mouse_motion)

        self.startup()
        self.animation_thread()
        self.root.mainloop()

    def animation_thread(self):
        frame = 0
        time_start = time.time()
        while 'Escape' not in self.input:
            self.loop(self.canvas, frame)
            self.canvas.update()
            frame += 1
            time_next_frame = frame / self.frames_per_second
            time_elapsed = time.time() - time_start
            time_sleep = time_next_frame - time_elapsed
            time.sleep(max(0, time_sleep))
            self.canvas.delete(tkinter.ALL)
        self.root.destroy()

    def startup(self):
        """
        https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        """
        pass

    def loop(self, canvas, frame):
        """
        http://zetcode.com/gui/tkinter/drawing/
        """
        raise Exception('Please override loop')


class AnimationDemo(TkAnimationFrame):
    def startup(self):
        super().startup()
        def click(event):
            print(event)
        self.canvas.bind("<Button>", click)

        self.img = tkinter.PhotoImage(file="images/fish.gif")

    def loop(self, canvas, frame):
        c = canvas
        c.create_rectangle(0, 0, c.winfo_width(), c.winfo_height(), outline="#000", fill="#000")

        t = frame % c.winfo_width()
        c.create_rectangle(t, 10, t+120, 80, outline="#fb0", fill="#fb0")

        t = frame % c.winfo_height()
        c.create_line(t, t, t+10, t+10, fill="red")

        c.create_image(self.mouse_x, self.mouse_y, image=self.img, anchor=tkinter.NW)

        #print(self.input)


AnimationDemo()
