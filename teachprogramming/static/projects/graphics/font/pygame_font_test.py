import pygame
from animation_base_pygame import PygameBase


class PygameFont(PygameBase):
    def __init__(self):
        self.x = 0
        self.xc = 1
        self.y = 0
        self.yc = 1
        self.font = self.load_font()
        super().__init__(resolution=(320,180))

    def load_font(self):
        path = 'font.gif'
        img = pygame.image.load(path)
        return {
            chr(i): img.subsurface((i*8, 0, 8, 8))
            for i in range(img.get_width()//8)
        }

    def draw_font(self, text, x, y):
        for i, char in enumerate(text):
            self.screen.blit(self.font[char], (x+i*8, y))

    def loop(self, screen, frame):
        self.draw_font("TAeZ", self.x, self.y)
        self.x = self.x + self.xc
        if self.x + (4*8) > self.width:
            self.xc = -1
        if self.x < 0:
            ???
        if self.y > self.height:
            ???
        

if __name__ == '__main__':
    PygameFont().run()
