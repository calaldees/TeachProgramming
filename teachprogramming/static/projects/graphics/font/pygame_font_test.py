import pygame
from pathlib import Path

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
            self.clock.tick(self.fps)
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
            except:
                import traceback; traceback.print_exc()
                self.running = False
            pygame.display.flip()
            frame += 1
        self.quit()
        pygame.quit()
    def loop(self, screen, frame):
        raise NotImplementedError('override loop method')
    def quit(self):
        pass  # override to shutdown


import pygame
from pathlib import Path

class PygameFont(PygameBase):
    def __init__(self):
        self.font = self.load_font()
        super().__init__(resolution=(320,180))
    def load_font(self, path_font=Path('font.gif')):
        img = pygame.image.load(path_font)
        return {chr(i): img.subsurface((i*8, 0, 8, 8)) for i in range(img.get_width()//8)}
    def loop(self, screen, frame):
        self.screen.blit(self.font["a"], (100, 100))

if __name__ == '__main__':
    PygameFont().run()