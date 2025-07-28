import pygame
from animation_base_pygame import PygameBase

from pathlib import Path                                                        # ver: download_font
from urllib.request import urlopen, Request                                     # ver: download_font
import math                                                                     # ver: draw_wave
import random                                                                   # ver: bounce_text

## https://damieng.com/typography/zx-origins/                                   # ver: load_font_advance
SEQUENCE_DAMIENG = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_£abcdefghijklmnopqrstuvwxyz{|}~©"""  # ver: load_font_advance
                                                                                # ver: load_font_advance
from dataclasses import dataclass                                               # ver: bounce_text
@dataclass                                                                      # ver: bounce_text
class BounceText():                                                             # ver: bounce_text
    text: str                                                                   # ver: bounce_text
    x: int                                                                      # ver: bounce_text
    y: int                                                                      # ver: bounce_text
    inc_x: int                                                                  # ver: bounce_text
    inc_y: int                                                                  # ver: bounce_text
                                                                                # ver: bounce_text
                                                                                # ver: bounce_text
class PygameFont(PygameBase):
    def __init__(self):
        #self.font = self.load_font()                                           # ver: load_font_advance NOT_
        self.font = self.load_font_advanced()                                   # ver: load_font_advance
        #super().__init__(resolution=(320,180))                                 # ver: load_font_advance NOT_
        super().__init__(resolution=(320,180), color_background='white')        # ver: load_font_advance

        #self.bounce_text = BounceText(                                         # ver: bounce_text NOT bounce_text_multi
        self.bounce_texts = tuple(                                              # ver: bounce_text_multi
            BounceText(                                                         # ver: bounce_text_multi
                text=text,                                                      # ver: bounce_text_multi
                #text='Bounce',                                                 # ver: bounce_text NOT bounce_text_multi
                x=random.randint(0, self.width - (len(text)*8)),                # ver: bounce_text
                y=random.randint(0, self.height - 8),                           # ver: bounce_text
                inc_x=random.choice((1,-1)),                                    # ver: bounce_text
                inc_y=random.choice((1,-1)),                                    # ver: bounce_text
            )                                                                   # ver: bounce_text_multi
            for text in ('Allan', 'Dale', 'Monika')                             # ver: bounce_text_multi
        )                                                                       # ver: bounce_text
                                                                                # ver: bounce_text
        self.random_ys = tuple(random.randint(0, self.height) for i in range(10)) # ver: list_scroll_x
    def download_if_not_exist(self, url):                                       # ver: download_font
        path = Path(Path(url).name)                                             # ver: download_font
        if not path.exists():                                                   # ver: download_font
            url = Request(url, headers={'User-Agent': 'curl'})                  # ver: download_font
            with urlopen(url) as r, path.open(mode='wb') as f:                  # ver: download_font
                f.write(r.read())                                               # ver: download_font
        return path                                                             # ver: download_font
                                                                                # ver: download_font
    def load_font(self):
        #path = 'font.gif'                                                      # ver: download_font NOT_
        path = self.download_if_not_exist('http://localhost:8000/static/font.gif') # ver: download_font
        img = pygame.image.load(path)
        return {chr(i): img.subsurface((i*8, 0, 8, 8)) for i in range(img.get_width()//8)}

    def load_font_advanced(self):                                               # ver: load_font_advance
        path = self.download_if_not_exist('https://img.damieng.com/fonts/ch8-previews/Babyteeth.webp') # ver: load_font_advance
        img = pygame.image.load(path)                                           # ver: load_font_advance
        w, h, seq = 8, 8, SEQUENCE_DAMIENG                                      # ver: load_font_advance
        ww, hh = img.get_size()                                                 # ver: load_font_advance
        return {                                                                # ver: load_font_advance
            seq[i]: img.subsurface(((i*w)%ww, ((i*w)//ww)*h, w, h))             # ver: load_font_advance
            for i in range(min((ww//w)*(hh//h), len(seq)))                      # ver: load_font_advance
        }                                                                       # ver: load_font_advance
                                                                                # ver: load_font_advance
    #def draw_font(self, text, x, y):                                           # ver: draw_string NOT draw_scale
    def draw_font(self, text, x, y, factor=1):                                  # ver: draw_scale
        for i, char in enumerate(text):                                         # ver: draw_string
            #self.screen.blit(self.font[char], (x+i*8, y))                      # ver: draw_string NOT draw_scale
            char_img = pygame.transform.scale_by(self.font[char], factor)       # ver: draw_scale
            self.screen.blit(char_img, (x+i*8*factor, y))                       # ver: draw_scale
                                                                                # ver: draw_string
    def draw_font_wave(self, text, x, y):                                       # ver: draw_wave
        for i, char in enumerate(text):                                         # ver: draw_wave
            _x = x+i*8                                                          # ver: draw_wave
            _y = y + math.sin(_x/50)*50                                         # ver: draw_wave
            self.screen.blit(self.font[char], (_x, _y))                         # ver: draw_wave
                                                                                # ver: draw_wave
    def loop(self, screen, frame):
        self.screen.blit(self.font["A"], (100, 100))
        self.draw_font("abcde", frame % self.width, 50)                         # ver: draw_string
        self.draw_font("Big Text!", 40, 30, factor=2)                           # ver: draw_scale
        self.draw_font_wave("abcde", frame % self.width, 110)                   # ver: draw_wave
        self.move_bounce_text()                                                 # ver: bounce_text
        self.horizontal_scroll_stateless_branchless(frame)                      # ver: list_scroll_x
                                                                                # ver: bounce_text
    def move_bounce_text(self):                                                 # ver: bounce_text
            #b = self.bounce_text                                               # ver: bounce_text NOT bounce_text_multi
        for b in self.bounce_texts:                                             # ver: bounce_text_multi
            b.x += b.inc_x                                                      # ver: bounce_text_move_x
            b.y += b.inc_y                                                      # ver: bounce_text
            b_width = len(b.text)*8                                             # ver: bounce_text
            if b.x < 0 or b.x > self.width - b_width:                           # ver: bounce_text_x
                b.inc_x = -b.inc_x                                              # ver: bounce_text_x
            if b.y < 0 or b.y > self.height-8:                                  # ver: bounce_text_y
                b.inc_y = -b.inc_y                                              # ver: bounce_text_y
            self.draw_font(b.text, b.x, b.y)                                    # ver: bounce_text
                                                                                # ver: bounce_text
    def horizontal_scroll_stateless_branchless(self, frame):                    # ver: list_scroll_x
        names = ['', 'me2', 'me3']                                              # ver: list_scroll_x
        index = (frame // self.width) % len(names)                              # ver: list_scroll_x
        x = frame % self.width                                                  # ver: list_scroll_x
        y = self.random_ys[index]                                               # ver: list_scroll_x
        name = names[index]                                                     # ver: list_scroll_x
        self.draw_font(name, x, y)                                              # ver: list_scroll_x

if __name__ == '__main__':
    PygameFont().run()
