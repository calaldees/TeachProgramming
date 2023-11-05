import math
import turtle
t = turtle.Pen()


def tree(t, size, angle, depth):
    if depth <= 0:
        return
    t.fd(size)
    t.rt(angle/2)
    tree(t, size, angle, depth-1)
    t.lt(angle)
    tree(t, size, angle, depth-1)
    t.rt(angle/2)
    t.bk(size)

#tree(t, 50, 90, 4)

def squiggle(t, size, angle, depth):
    if depth <= 0:
        return
    t.fd(size)
    t.rt(angle)
    squiggle(t, size, angle, depth-1)
    t.lt(angle)
    t.bk(size)


def reset():
    turtle.resetscreen()
    t.hideturtle()
    t.penup()
    t.setheading(90)
    t.sety(-200)
    t.pendown()


turtle.tracer(n=0, delay=0)
frame = 0
def loop():
    turtle.ontimer(loop, int(1000/30))
    global frame;  frame += 1

    oss1 = math.sin(frame/30)
    oss2 = math.sin(frame/17)

    reset()
    #tree(t, 100+oss1*50, 90+oss2*60, 5)
    #squiggle(t, 100+oss1*50, oss2*10, 10)
    turtle.update()
loop()

breakpoint()