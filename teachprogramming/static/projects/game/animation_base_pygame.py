#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "pygame",
# ]
# ///

from abc import abstractmethod
from typing import override, Tuple
from functools import cached_property

try:
    import pygame
except ImportError:
    print('Failed to import `pygame` - attempting automatic install')
    # The instructions on Pygame site suck https://www.pygame.org/wiki/GettingStarted
    # Python on windows can be installed in many different places and does not set a default path for `pip`
    # https://stackoverflow.com/a/12333108/3356840
    import subprocess
    import sys
    def pip_install(name):
        return subprocess.call([sys.executable, '-m', 'pip', 'install', name])
    pip_install('pygame')
    import pygame


RESOLUTION_1080x3 = (640,360)
RESOLUTION_1080x4 = (480,270)

class PygameBase():
    def __init__(self, title: str="pg", resolution:Tuple[int,int]=RESOLUTION_1080x4, fps:int=60, color_background:str='black'):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(resolution, pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.color_background = color_background
    def run(self) -> None:
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
    @abstractmethod
    def loop(self, screen: pygame.Surface, frame: int) -> None:
        raise NotImplementedError('override loop method')
    def quit(self):
        pass  # override to shutdown
    @cached_property
    def width(self) -> int:
        return self.screen.get_width()
    @cached_property
    def height(self) -> int:
        return self.screen.get_height()


class GameDemo(PygameBase):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.image = pygame.image.load('images/block.gif')
        super().__init__()

    def loop(self, screen, frame):
        s = screen
        width, height = s.get_size()

        t = frame % width
        pygame.draw.rect(s, pygame.Color("#f0b000"), (t, 10, 120, 80))

        t = frame % height
        pygame.draw.line(s, pygame.Color("red"), (t, t), (t+10, t+10), 5)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        s.blit(self.image, (mouse_x, mouse_y))

        if self.keys[pygame.K_UP]:
            self.y += -1
        if self.keys[pygame.K_DOWN]:
            self.y += 1
        if self.keys[pygame.K_RIGHT]:
            self.x += 1
        if self.keys[pygame.K_LEFT]:
            self.x += -1
        s.blit(self.image, (self.x, self.y))


        # Task DVD menu
        # 1.) Square edged red rectangle - 50 50
        # 2.) It moves automatically (in the x direction only)
        # 3.) It bounces left and right from the edges of the screen
        # 4.) DVD screensaver - bounces of top bottom left right
        # 5.) Make the rectangle an image
        # 6.) Remove any hard coded values for width/height/imagesize/etc

if __name__ == '__main__':
    GameDemo().run()

# mac install
#  brew install virtualenv
#  python3 -m venv my-venv
#  my-venv/bin/pip install pygame
#  my-venv/bin/python3 python_file_to_run.py