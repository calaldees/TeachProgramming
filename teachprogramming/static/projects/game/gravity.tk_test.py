import random
from animation_base_tk import TkAnimationBase

class Block:
    x: float = 0
    y: float = 0
    size: int = 20
    x_vel: float = 0
    y_vel: float = 0

class Gravity(TkAnimationBase):
    def __init__(self):
        super().__init__(width=640, height=480)

    def before_start(self):
        self.reset()

    def reset(self):
        self.blocks = [Block()]

    def loop(self, canvas, frame):
        mx, my = self.mouse_x, self.mouse_y

        for b in self.blocks:
            b.x_vel += -(b.x - mx) / b.size / 500
            b.y_vel += -(b.y - my) / b.size / 500
            b.x += b.x_vel
            b.y += b.y_vel
            canvas.create_rectangle(b.x, b.y, b.x+b.size, b.y+b.size, fill="#ff0")

        canvas.create_rectangle(mx-2, my-2, mx+2, my+2, fill="#fff")

if __name__ == '__main__':
    Gravity()
