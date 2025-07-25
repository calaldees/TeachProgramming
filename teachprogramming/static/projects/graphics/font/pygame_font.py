import pygame

# copy and pasted
#from animation_base_pygame import PygameBase
class PygameBase():
    def __init__(self, title="pg", resolution=(320,180), fps=60, color_background='black'):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(resolution, pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.color_background = color_background
    def run(self):
        frame = 0
        self.running = True
        while self.running:
            pygame.display.flip()
            self.keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                    self.running = False
                if event.type == pygame.VIDEORESIZE:
                    pygame.display._resize_event(event)
                if (self.keys[pygame.K_RALT] or self.keys[pygame.K_LALT]) and self.keys[pygame.K_RETURN]:
                    pygame.display.toggle_fullscreen()
            self.screen.fill(self.color_background)
            try:
                self.loop(self.screen, frame)
            except Exception:
                import traceback; traceback.print_exc()
                self.running = False
            frame += 1
            self.clock.tick(self.fps)
        self.quit()
        pygame.quit()
    def loop(self, screen, frame):
        raise NotImplementedError('override loop method')
    def quit(self):
        pass  # override to shutdown


#-------------------------------------------------------------------------------

from pathlib import Path
from urllib.request import urlopen
import math
import random
random.seed(0)

# https://damieng.com/typography/zx-origins/pristine
SEQUENCE_ZX_ORIGINS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_£abcdefghijklmnopqrstuvwxyz{|}~©""" # https://damieng.com/typography/zx-origins/

class PygameFont(PygameBase):
    def __init__(self):
        #self.font = self.load_font()
        self.font = self.load_font_advanced()
        #super().__init__(resolution=(320,180))
        self.random_ys = tuple(random.randint(0, 180) for i in range(10))
        super().__init__(resolution=(320,180), color_background='white')
    def load_font(self, path_font=Path('font.gif'), url_font='http://localhost:8000/static/font.gif'):
        if not path_font.exists():
            with urlopen(url_font) as r, path_font.open(mode='wb') as f:
                f.write(r.read())
        img = pygame.image.load(path_font)
        return {chr(i): img.subsurface((i*8, 0, 8, 8)) for i in range(img.get_width()//8)}
    def load_font_advanced(self, path_font=Path('font.webp'), seq=SEQUENCE_ZX_ORIGINS, w=8, h=8):
        img = pygame.image.load(path_font)
        ww, hh = img.get_size()
        return {
            seq[i]: img.subsurface(((i*w)%ww, ((i*w)//ww)*h, w, h))
            for i in range(min((ww//w)*(hh//h), len(seq)))
        }
    def draw_font(self, text, x, y):
        for i, char in enumerate(text):
            self.screen.blit(self.font[char], (x+i*8, y))
    def loop(self, screen, frame):
        width, height = screen.get_size()
        self.screen.blit(self.font["A"], (100, 100))
        self.draw_font("abcde", frame%width, 50)
        self.draw_font_wave("abcde", frame%width, 110)
        #self.horizontal_scroll_stateless_branchless(frame, width)

    def draw_font_wave(self, text, x, y):
        for i, char in enumerate(text):
            _x = x+i*8
            _y = y + math.sin(_x/50)*50
            self.screen.blit(self.font[char], (_x, _y))

    def horizontal_scroll_stateless_branchless(self, frame, width):
        names = ['me', 'me2', 'me3']
        index = (frame // width) % len(names)
        x = frame % width
        y = self.random_ys[index]
        name = names[index]
        self.draw_font(name, x, y)

if __name__ == '__main__':
    PygameFont().run()
