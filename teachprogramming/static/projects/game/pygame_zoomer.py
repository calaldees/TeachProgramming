import math
import random
import itertools
from types import MappingProxyType

import pygame as pg

from pygame_test import GameBase


class Zoomer():
    def __init__(self):
        self.size_min = 3
        self.size_max = 30
        self.colors = (
            (0,0,0),
            (255,255,255),
        )
    def render(self, sf, frame, pos=None):
        sf_w = sf.get_width()
        sf_h = sf.get_height()
        x, y = pos or (sf_w/2, sf_h/2)  # todo use sin/cos for auto x/y from frame?

        p = (math.sin(((frame % 360)/360)*math.pi*2) + 1) / 2  # progress 0 to 1 from frame
        s = self.size_min + (p * self.size_max)  # size of square

        c_width = int(((sf_w / s) + 4) / 2)  # squares in x for surface
        c_height = int(((sf_h / s) + 4) / 2)  # squares in y for surface
        width_shift = int((x - (sf_w / 2)) / s) # shift for x pos
        height_shift = int((y - (sf_h / 2))/ s)
        for cx in range(-c_width - width_shift, c_width - width_shift):
            for cy in range(-c_height - height_shift, c_height - height_shift):
                pg.draw.rect(
                    sf,
                    self.colors[(cx+cy) % len(self.colors)],
                    (
                        x + (s * cx),
                        y + (s * cy),
                        s, s,
                    )
                )

class Stars():
    class Star():
        def __init__(self, x, y, s):
            self.x = x
            self.y = y
            self.s = s
    def __init__(self, width, height, density=0.001, layers=4):
        self.stars = tuple(
            self.Star(
                random.randint(0, width),
                random.randint(0, height),
                random.randint(1, layers),
            ) 
            for r in range(int(width * height * density))
        )
    def render(self, sf, frame):
        sf_w = sf.get_width()
        for s in self.stars:
            pg.draw.rect(sf, 'white', ((s.x + (-frame * s.s)) % sf_w , s.y, s.s, 1))


def font_loader(filename, sequence='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', size=8):
    """
    https://nfggames.com/games/fontmaker/index.php
    """
    image = pg.image.load(filename)
    return MappingProxyType({
        character: image.subsurface((i*size, 0, size, size))
        for i, character in enumerate(sequence)
    })


class Font():
    def __init__(self, filename, size=8, spacing=1):
        self.font = font_loader(filename, size=size)
        self.size = size
        self.spacing = spacing
    def render(self, sf, text, x, y):
        for i, character in enumerate(text):
            sf.blit(self.font[character], (x+(i*(self.size+self.spacing)), y))
    def scroll(self, sf, frame, text, x, y, width=128, speed=1, func_y=lambda x: 0):
        start_char = (frame // self.size) % len(text)
        num_visible_chars = width // self.size
        visible_text = text[start_char : start_char + num_visible_chars]
        for i, character in enumerate(visible_text):
            if character == ' ':
                continue
            _x = x + (i*(self.size+self.spacing)) - (frame % self.size)
            sf.blit(self.font[character], (
                _x,
                y + func_y(_x),
            ))

class Game(GameBase):
    def __init__(self):
        self.x = int(320/2)
        self.y = int(180/2)
        self.zoomer = Zoomer()
        self.stars = Stars(320, 180)
        self.font = Font('images/font.png')
        super().__init__()
    def loop(self, screen, frame):
        if self.keys[pg.K_UP]:
            self.y += -1
        if self.keys[pg.K_DOWN]:
            self.y += 1
        if self.keys[pg.K_RIGHT]:
            self.x += 1
        if self.keys[pg.K_LEFT]:
            self.x += -1

        self.zoomer.render(screen, frame, pos=(self.x, self.y))
        self.stars.render(screen, frame)
        def func_y(x):
            return math.sin(x/32) * 16
        self.font.scroll(screen, frame, '                                  MY FIRST EVER DEMO MOCK UP       CHECK OUT THIS SCROLLING TEXT          TIME TO TRY SOME MORE COOL OLD SKOOL IDEAS         ', 0, screen.get_height()/2, width=screen.get_width(), func_y=func_y)
        self.font.render(screen, 'HELLO', 100, 100)



if __name__ == '__main__':
    Game()
