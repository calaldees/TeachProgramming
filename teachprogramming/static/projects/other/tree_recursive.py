import turtle
t = turtle.Pen()

def draw_tree_recursive(t, size=100, branches=3, total_angle=120, depth=2):
    if not depth:
        return
    start_pos = t.pos()
    start_heading = t.heading()
    for branch_number in range(branches):
        t.setheading(
            start_heading - (total_angle / 2)
            +
            (branch_number * total_angle / (branches-1))
        )
        t.forward(size)
        draw_tree_recursive(t, size=size * 0.6, branches=branches, total_angle=total_angle * 0.8, depth=depth-1)
        t.setpos(start_pos)
        t.setheading(start_heading)

draw_tree_recursive(t)

import pdb ; pdb.set_trace()


# TODO: consider stack implementation
