import math
import random
import itertools
from types import MappingProxyType
from typing import NamedTuple
from functools import partial

import pygame as pg

from pygame_test import GameBase

random.seed(0)


class Zoomer():
    def __init__(self, size_min=8, size_max=30):
        self.size_min = size_min
        self.size_max = size_max
        self.colors = (
            pg.Color('#4c2e6b'),
            pg.Color('#894c6b'),
        )
    @staticmethod
    def frame_to_progress(frame, ratio=100):
        return math.sin((frame % ratio / ratio) * math.pi * 2)
    def render(self, sf, frame, pos=None):
        fp = partial(self.frame_to_progress, frame)
        sf_w = sf.get_width()
        sf_h = sf.get_height()
        x, y = pos or (
            fp(200) * (sf_w/2),
            fp(166) * (sf_h/2),
        )
        p = (fp(360) + 1) / 2  # progress 0 to 1 from frame
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
                        s+1, s+1,
                    )
                )

class Stars():
    class Star(NamedTuple):
        x: int
        y: int
        s: int
    def __init__(self, width, height, density=0.0015, layers=4):
        self.layers = layers
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
        #sf_h = sf.get_height()
        for s in self.stars:
            _x_true = (s.x + (-frame * s.s))
            _x = _x_true % sf_w
            #_y_overflow_multiplier = -((_x_true - _x) / sf_w) + 1
            _y = s.y #(s.y * _y_overflow_multiplier) % sf_h
            color = ( ((s.s/self.layers)*255) ,) * 3
            pg.draw.line(sf, color, (_x, _y,), (_x-s.s, _y))


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
    def scroll(self, sf, frame, text, x, y, width=128, func_y=lambda x: 0):
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

class Demo(GameBase):
    def __init__(self, resolution=(320,180)):
        self.zoomer = Zoomer()
        self.stars = Stars(resolution[0]/2, resolution[1])
        self.font = Font('images/font.png')
        super().__init__(resolution=resolution)
    def loop(self, screen, frame):
        width = screen.get_width()
        _width = screen.get_width()/2
        height = screen.get_height()

        self.zoomer.render(screen.subsurface(0, 0, _width, height), frame)
        self.stars.render(screen.subsurface(_width, 0, _width, height), frame)

        text = '                '.join((
            '                     ',
            'MY FIRST EVER DEMO MOCK UP',
            'CHECK OUT THIS SCROLLING TEXT',
            'ALL THE EFFECTS ARE FUNCTIONAL AND HAVE ZERO STATE BETWEEN FRAMES',
            'NOT BAD FOR 100ISH LINES OF PYTHON AND PYGAME',
            'TIME TO TRY SOME MORE COOL OLD SKOOL IDEAS',
        ))
        def func_y(x):
            return math.sin(x/32) * 16
        self.font.scroll(screen, frame, text, 0, height/2, width=width, func_y=func_y)


if __name__ == '__main__':
    Demo()
