import math
import io

import pygame

from pygame_test import GameBase


class Game(GameBase):
    def __init__(self):
        self.s = None
        self.c = None
        pygame.mixer.pre_init(frequency=44100, size=8, channels=1, buffer=512)
        super().__init__()
    def loop(self, screen, frame):
        if frame == 0:
            #sd = io.BytesIO()
            #print(tt)
            #sd = bytes(tt)  #(128,)*512
            #s = pygame.sndarray.make_sound()
            self.c = pygame.mixer.Channel(0)
        if frame > 10:
            ff = ((frame//60) % 7) + 1
            tt = tuple(int((math.sin(i/ff)*128)+127) for i in range(735))
            self.s = pygame.mixer.Sound(buffer=bytes(tt))
            self.c.queue(self.s)

if __name__ == '__main__':
    Game()
