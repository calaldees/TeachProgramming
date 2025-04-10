import abc
import typing as t
import tkinter
import time

# TODO:
# we need get sub images from an image - pygame has `subsurface`
# https://stackoverflow.com/questions/52375035/cropping-an-image-in-tkinter

class TkAnimationBase():
    def __init__(self, width:int=320, height:int=180, frames_per_second:int=60):
        self.width = width
        self.height = height
        self.frames_per_second = frames_per_second

        self.root = tkinter.Tk()
        self.root.resizable(False, False)
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        self.input = set()
        self.root.bind("<Key>", lambda event: self.input.add(event.keysym))
        self.root.bind("<KeyRelease>", lambda event: self.input.remove(event.keysym))
        self.mouse_x, self.mouse_y = (0, 0)
        def mouse_motion(event):
            self.mouse_x, self.mouse_y = (event.x, event.y)
        self.root.bind('<Motion>', mouse_motion)

        self.before_start()
        self.animation_thread()
        self.root.mainloop()

    def animation_thread(self):
        frame = 0
        time_start = time.time()
        while 'Escape' not in self.input:
            self.canvas.create_rectangle(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height(), outline="#000", fill="#000")
            self.loop(self.canvas, frame)
            self.canvas.update()
            frame += 1
            time_next_frame = frame / self.frames_per_second
            time_elapsed = time.time() - time_start
            time_sleep = time_next_frame - time_elapsed
            time.sleep(max(0, time_sleep))
            try:
                self.canvas.delete(tkinter.ALL)
            except tkinter.TclError:
                pass
        self.root.destroy()

    @abc.abstractmethod
    def before_start(self):
        """
        https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        """
        pass

    @abc.abstractmethod
    def loop(self, canvas: tkinter.Canvas, frame:int):
        """
        https://tkdocs.com/tutorial/canvas.html
        https://web.archive.org/web/20190302183420/http://zetcode.com/gui/tkinter/drawing/
        """
        raise NotImplementedError('override loop method')


class TkDemo(TkAnimationBase):
    def before_start(self):
        super().before_start()
        def click(event):
            print(event)
        self.canvas.bind("<Button>", click)

        self.x = 100
        self.y = 100
        self.image = tkinter.PhotoImage(file='images/block.gif')

        self.img = tkinter.PhotoImage(file="images/block.gif")

    def loop(self, canvas, frame):
        c = canvas
        width, height = c.winfo_width(), c.winfo_height()

        t = frame % width
        c.create_rectangle(t, 10, t+120, 80, outline="#fb0", fill="#fb0")

        t = frame % height
        c.create_line(t, t, t+10, t+10, fill="red", width=5)

        c.create_image(self.mouse_x, self.mouse_y, image=self.img, anchor=tkinter.NW)

        if 'Up' in self.input:
            self.y += -1
        if 'Down' in self.input:
            self.y += 1
        if 'Right' in self.input:
            self.x += 1
        if 'Left' in self.input:
            self.x += -1
        c.create_image(self.x, self.y, image=self.image, anchor=tkinter.NW)

        # TODO: write frame as text at 0,0 (do this for all animation_bases)
        #print(self.input)

if __name__ == '__main__':
    TkDemo()
