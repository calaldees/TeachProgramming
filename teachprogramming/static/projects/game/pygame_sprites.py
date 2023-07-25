import random

import pygame

from animation_base_pygame import PygameBase

def download(url):
    """
    Equivalent of curl if need
    # curl -O https://www.nicepng.com/png/full/222-2222069_megaman-sprite-png.png
    https://www.nicepng.com/ourpic/u2w7e6i1u2w7w7q8_megaman-sprite-png-megaman-sprite-sheet-png/
    """
    from pathlib import Path
    import urllib.request
    from urllib.parse import urlparse
    filename = Path(Path(urlparse(url).path).name)
    if not filename.is_file():
        #filename.parent.mkdir(parents=True, exist_ok=True)
        print(f'Downloading {url} to {filename}')
        with urllib.request.urlopen(url) as url_request, filename.open(mode='wb') as filehandle :
            filehandle.write(url_request.read())
    assert filename.is_file()
    return filename.resolve()

def load_sprites(filename, sprite_width=32, sprite_height=None):
    import math
    sprite_height = sprite_height or sprite_width
    image = pygame.image.load(filename)
    width, height = image.get_size()
    return [
        image.subsurface(pygame.Rect.clip(image.get_rect(), (x*sprite_width, y*sprite_height, sprite_width, sprite_height)))
        for y in range(math.ceil(height/sprite_height))
        for x in range(math.ceil(width/sprite_width))
    ]

class AnimationSprite():
    def __init__(self, sprites, speed=None, x=None, y=None):
        self.sprites = sprites
        self.speed = speed if speed != None else random.randint(1,6)
        self.x = x or random.randint(1,180)
        self.y = y or random.randint(1,140)
#    def move(self):
#        self.x += self.speed
#        if self.y > 320:  # bit of a hack - we can talk about this
#            self.y = -30


class GameDemo(PygameBase):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.sprites = load_sprites(
            download("https://www.nicepng.com/png/full/222-2222069_megaman-sprite-png.png"),
            sprite_width=50, sprite_height=49
        )
        self.animation_sprites = [
            AnimationSprite(self.sprites[32:32+11]),
            AnimationSprite(self.sprites[32:32+11]),
            AnimationSprite(self.sprites[45:45+11]),
            AnimationSprite(self.sprites[6:15], speed=0, x=100, y=100),
        ]
        super().__init__()
    def loop(self, screen, frame):
        width, height = screen.get_size()

        #screen.blit(self.sprites[0 + (frame//64 % 8)], (self.x, self.y))
        #screen.blit(self.sprites[32 + (frame//4 % 11)], (self.x, self.y))

        for s in self.animation_sprites:
            sprite_frame = (frame * (s.speed+1))//12
            screen.blit(s.sprites[sprite_frame%len(s.sprites)], (s.x, s.y))
            s.x += s.speed
            if s.x > width:
                s.x = -50
                s.y = random.randint(0,140)
                s.speed = random.randint(1,6)

if __name__ == '__main__':
    GameDemo().run()
