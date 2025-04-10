import random
from animation_base_tk import TkAnimationBase

class Block:                                                                    # VER: single_block
    x: float = 0                                                                # VER: single_block
    y: float = 0                                                                # VER: single_block
    size: int = 20                                                              # VER: single_block
    x_vel: float = 0                                                            # VER: move_to_mouse
    y_vel: float = 0                                                            # VER: move_to_mouse
    def contains(self, mx, my):                                                 # VER: collision
        s, x, y = self.size, self.x, self.y                                     # VER: collision
        return mx>=x and mx<=x+s and my>=y and my<=y+s                          # VER: collision

class Gravity(TkAnimationBase):
    def __init__(self):
        super().__init__(width=640, height=480)
                                                                                # VER: single_block
    def before_start(self):                                                     # VER: single_block
        self.MIN_BLOCK_SIZE = 5                                                 # VER: random_start
        self.MAX_BLOCK_SIZE = 35                                                # VER: random_start
        self.NUM_BLOCKS = 50                                                    # VER: multiple_blocks
        self.reset()                                                            # VER: single_block

    def reset(self):                                                            # VER: single_block
        #self.blocks = [Block()]                                                # VER: single_block NOT multiple_blocks
        self.blocks = [Block() for i in range(self.NUM_BLOCKS)]                 # VER: multiple_blocks
        for b in self.blocks:                                                   # VER: random_start
            b.size = random.randint(self.MIN_BLOCK_SIZE, self.MAX_BLOCK_SIZE)   # VER: random_start
            b.x = random.random() * (self.width - b.size)                       # VER: random_start
            b.y = random.random() * (self.height - b.size)                      # VER: random_start
        self.time_elapsed = 0                                                   # VER: score

    def loop(self, canvas, frame):
        mx, my = self.mouse_x, self.mouse_y
                                                                                # VER: single_block
        for b in self.blocks:                                                   # VER: single_block
            if b.x < 0 or b.x > self.width-b.size:                              # VER: bounce
                b.x_vel = -(b.x_vel / 3)                                        # VER: bounce
            if b.y < 0 or b.y > self.height-b.size:                             # VER: bounce
                b.y_vel = -(b.y_vel / 3)                                        # VER: bounce
            b.x_vel += -(b.x - mx) / b.size / 500                               # VER: physics
            b.y_vel += -(b.y - my) / b.size / 500                               # VER: physics
            #b.x_vel = 1 if b.x<mx else -1                                      # VER: move_to_mouse NOT physics
            #b.y_vel = 1 if b.y<my else -1                                      # VER: move_to_mouse NOT physics
            b.x += b.x_vel                                                      # VER: move_to_mouse
            b.y += b.y_vel                                                      # VER: move_to_mouse
            canvas.create_rectangle(b.x, b.y, b.x+b.size, b.y+b.size, fill="#ff0")  # VER: single_block

        if any(b.contains(mx, my) for b in self.blocks):                        # VER: collision
            print(f"Score: {self.time_elapsed}")                                # VER: score
            self.reset()                                                        # VER: collision
                                                                                # VER: collision
        canvas.create_rectangle(mx-2, my-2, mx+2, my+2, fill="#fff")
        self.time_elapsed += 1                                                  # VER: score

if __name__ == '__main__':
    Gravity()
