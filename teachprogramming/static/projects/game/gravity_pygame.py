import random
import pygame

from animation_base_pygame import PygameBase

BLACK = (0, 0, 0, 255)


class Block:
    x: float = 0
    y: float = 0
    size: int = 0
    x_vel: float = 0
    y_vel: float = 0


class Gravity(PygameBase):
    def __init__(self):
        super().__init__(resolution=(640, 480))
        self.MAX_BLOCK_SIZE = 30
        self.NUM_BLOCKS = 50
        self.reset()

    def reset(self):
        self.blocks = [Block() for i in range(self.NUM_BLOCKS)]
        for b in self.blocks:
            b.x = random.random() * self.screen.get_width()
            b.y = random.random() * self.screen.get_height()
            b.size = random.randint(0, self.MAX_BLOCK_SIZE) + 5
        self.time_elapsed = 0

    def loop(self, screen, frame):
        width, height = screen.get_size()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for b in self.blocks:
            if b.x < 0 or b.x > width:
                b.x_vel = -(b.x_vel / 3)
            if b.y < 0 or b.y > height:
                b.y_vel = -(b.y_vel / 3)
            b.x_vel += -(b.x - mouse_x) / b.size / 500
            b.y_vel += -(b.y - mouse_y) / b.size / 500
            b.x += b.x_vel
            b.y += b.y_vel
            pygame.draw.rect(screen, "yellow", pygame.Rect(b.x, b.y, b.size, b.size))

        if screen.get_at((mouse_x, mouse_y)) != BLACK:
            print(f"Score: {self.time_elapsed}")
            self.reset()

        pygame.draw.rect(screen, "white", pygame.Rect(mouse_x - 2, mouse_y - 2, 4, 4))
        self.time_elapsed += 1


if __name__ == "__main__":
    Gravity().run()
