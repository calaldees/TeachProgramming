import turtle
import math


t = turtle.Pen()
turtle.colormode(255)



def f():
    #t.fd(50)
    #t.lt(60)
    global frame; frame+=1

s = turtle.Screen() 
s.onkey(f, "Up")
turtle.listen()



turtle.tracer(n=0, delay=0)
frame = 0
def loop():
    turtle.ontimer(loop, int(1000/30))
    global frame;  frame += 1
    turtle.resetscreen()

    oss1 = math.sin(frame/30)

    # Draw
    t.color("black", "red")
    t.begin_fill()
    t.circle(oss1 * 80)
    t.end_fill()

    turtle.update()
loop()
breakpoint()



#    
#    oss2 = math.sin(frame/17)

# https://docs.python.org/3/library/turtle.html#making-algorithmic-patterns
#for steps in range(100):
#    for c in ('blue', 'red', 'green'):
#        t.color(c)
#        t.forward(steps)
#        t.right(30)



t.color('red')
t.fillcolor('yellow')
t.begin_fill()
while False:
#for i in range(10):
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()


#t.circle(50, extent=180, steps=2)
