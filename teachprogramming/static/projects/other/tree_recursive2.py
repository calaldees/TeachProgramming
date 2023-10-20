import math
import turtle
t = turtle.Pen()

turtle.tracer(n=0, delay=0)

from typing import NamedTuple

class TreeState(NamedTuple):
    size: float =100
    branches: int =5
    total_angle: float =120
    depth: int =4
    def copy(self, **kwargs):
        return TreeState(**{**self._asdict(), **kwargs})


def draw_tree_recursive(t, s: TreeState):
    if not s.depth:
        return
    start_pos = t.pos()
    start_heading = t.heading()
    for branch_number in range(s.branches):
        t.setheading(
            start_heading - (s.total_angle / 2)
            +
            (branch_number * s.total_angle / (s.branches-1))
        )
        t.forward(s.size)
        draw_tree_recursive(t, s.copy(size=s.size*0.8, total_angle=s.total_angle*0.8, depth=s.depth-1))
        t.setpos(start_pos)
        t.setheading(start_heading)


frame = 0
def loop():
    global frame
    frame += 1
    turtle.ontimer(loop, int(1000/30))

    ossilator1 = math.sin((frame/60)*math.pi*2)
    ossilator2 = math.sin((frame/37)*math.pi*2)
    turtle.resetscreen()
    t.penup()
    t.setheading(90)
    t.sety(-200)
    t.pendown()
    #t.backward(200)
    t.hideturtle()
    draw_tree_recursive(t,
                        TreeState(
                            size=100+ossilator2*50,
                            total_angle=90+ossilator1*30
                        )
    )
    turtle.update()
loop()
breakpoint()
#draw_tree_recursive(t, TreeState(size=100+frame))
