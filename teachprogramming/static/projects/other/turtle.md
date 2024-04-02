turtle
======

Base
----

```python  {.line-numbers}
import turtle
t = turtle.Pen()

t.fd(100)
```


Fill
----

```python  {.line-numbers}
def fill(color_outline, color_fill, f):
    t.color(color_outline)
    t.fillcolor(color_fill)
    t.begin_fill()
    start_pos = t.pos()
    f()
    t.setpos(start_pos)
    t.end_fill()
```


Animation loop
--------------

```python  {.line-numbers}
turtle.tracer(n=0, delay=0)
frame = 0
def loop():
    turtle.ontimer(loop, int(1000/30))
    global frame;  frame += 1
    turtle.resetscreen()

    # Do drawing and variable updates here

    turtle.update()
loop()
breakpoint()
```

Commands
--------

https://docs.python.org/3/library/turtle.html

```python  {.line-numbers}
def thing():
    t.fd(100)
    t.rt(90)
    t.lt(90)
    t.bk(100)

t.up()
t.down()

p = t.pos()
t.setpos(p)
t.setpos((100,200))

t.teleport(p)
t.teleport((100,200))

turtle.colormode(255)
t.color((255,0,0))
t.fillcolor((0,255,0))
```
