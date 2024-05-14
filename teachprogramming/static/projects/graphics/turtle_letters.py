import turtle

t = turtle.Pen()
turtle.colormode(255)

t.fd(100)

def draw_A():
    start_pos = t.pos()

    t.lt(60)
    t.fd(200)
    t.rt(120)
    t.fd(200)
    
    t.rt(120)
    t.fd(20)
    t.rt(60)
    t.fd(20)
    t.lt(60)
    t.fd(100)
    t.lt(60)
    t.fd(20)

    t.setpos(start_pos)

t.color('red')
t.fillcolor('yellow')
t.begin_fill()
draw_A()
t.end_fill()

t.teleport(100,100)


def fill(color_outline, color_fill, f):
    t.color(color_outline)
    t.fillcolor(color_fill)
    t.begin_fill()
    f()
    t.end_fill()


class V():
    a = 10
    b = 20


turtle.tracer(n=0, delay=0)
frame = 0
def loop():
    turtle.ontimer(loop, int(1000/30))
    global frame;  frame += 1
    turtle.resetscreen()

    global V
    V.a += 1
    t.teleport(V.a, 0)
    fill('red','yellow', draw_A)

    turtle.update()
loop()
breakpoint()
