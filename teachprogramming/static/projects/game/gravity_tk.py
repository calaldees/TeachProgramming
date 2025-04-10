import random
from animation_base_tk import TkAnimationBase

class Block:
    x: float = 0
    y: float = 0
    size: int = 0
    x_vel: float = 0
    y_vel: float = 0
    def contains(self, mx, my):
        s, x, y = self.size, self.x, self.y
        return mx>=x and mx<=x+s and my>=y and my<=y+s

class Gravity(TkAnimationBase):
    def __init__(self):
        super().__init__(width=640, height=480)

    def startup(self):
        super().startup()
        self.MAX_BLOCK_SIZE = 30
        self.NUM_BLOCKS = 50
        self.reset()

    def reset(self):
        self.blocks = [Block() for i in range(self.NUM_BLOCKS)]
        for b in self.blocks:
            b.x = random.random() * self.width
            b.y = random.random() * self.height
            b.size = random.randint(0, self.MAX_BLOCK_SIZE) + 5
        self.time_elapsed = 0

    def loop(self, canvas, frame):
        mouse_x, mouse_y = self.mouse_x, self.mouse_y

        for b in self.blocks:
            if b.x < 0 or b.x > self.width:
                b.x_vel = -(b.x_vel / 3)
            if b.y < 0 or b.y > self.height:
                b.y_vel = -(b.y_vel / 3)
            b.x_vel += -(b.x - mouse_x) / b.size / 500
            b.y_vel += -(b.y - mouse_y) / b.size / 500
            b.x += b.x_vel
            b.y += b.y_vel
            canvas.create_rectangle(b.x, b.y, b.x+b.size, b.y+b.size, fill="#ff0")

        if any(b.contains(mouse_x, mouse_y) for b in self.blocks):
            print(f"Score: {self.time_elapsed}")
            self.reset()

        canvas.create_rectangle(mouse_x-2, mouse_y-2, mouse_x+2, mouse_y+2, fill="#fff")
        self.time_elapsed += 1


if __name__ == '__main__':
    Gravity()
