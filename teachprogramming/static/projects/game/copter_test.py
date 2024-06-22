import pygame
from animation_base_pygame import PygameBase
import pathlib

class CopterGame(PygameBase):
    def __init__(self):
        self.background_color = (0, 0, 0, 0)
        self.level_number = 1
        self.reset()
        super().__init__(resolution=(320,240))
        self.background_images = [
            pygame.image.load(file)
            for file in sorted(pathlib.Path('images').glob(f"*CopterLevel{self.level_number}*"))
        ]
    def reset(self):
        self.background_x_pos = 0
    def loop(self, screen, frame):
        self.background_x_pos += 1


        pygame.draw.rect(screen, self.background_color, (0,0)+screen.get_size())
        for parallax_number, background_image in sorted(enumerate(self.background_images), reverse=True):
            screen.blit(background_image, (-self.background_x_pos/2**parallax_number, 0))

if __name__ == '__main__':
    CopterGame().run()
