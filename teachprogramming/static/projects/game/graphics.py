import tkinter

w = 480
h = 270
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=w, height=h)
canvas.pack()

def render(c):
    c.create_rectangle(0, 0, w, h, outline="#000", fill="#000")  # Reset the canvas to black

    # https://tkdocs.com/tutorial/canvas.html
    # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html

    c.create_rectangle(20, 20, 30, 30, outline="#fff", fill="#fff")

    c.create_line(100, 100, 200, 100, fill="cyan", width=2)

    c.create_arc(200, 200, 250, 250, fill='magenta', outline='black', start=-90, extent=90, width=1)

    c.update()

render(canvas)

root.mainloop()
