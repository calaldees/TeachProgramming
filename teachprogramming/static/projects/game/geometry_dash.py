from collections.abc import Mapping, Sequence
from pathlib import Path

import pygame

from animation_base_pygame import PygameBase


def load_geometry_dash_levels(path: Path, width=120) -> Sequence[str]:
    lines = []
    with path.open() as f:
        while line := f.readline():
            lines.append(line.removesuffix('\n').ljust(width, ' '))
    return lines


def load_tiles(path: Path, seq: str, w: int, h: int = 0) -> Mapping[str, pygame.image]:
    h = h or w
    img = pygame.image.load(path)
    ww, hh = img.get_size()
    return {
        seq[i]: img.subsurface(((i*w)%ww, ((i*w)//ww)*h, w, h))
        for i in range(min((ww//w)*(hh//h), len(seq)))
    }


class GeometryDash(PygameBase):
    def __init__(self):
        self.level_data = load_geometry_dash_levels(Path('geometry_dash.txt'))
        self.tile_size = 32
        self.tiles = load_tiles(Path('geometry_dash.png'), '@^#_', self.tile_size)

        self.level: int = 0
        self.speed: float = 1.21

        self.x: float = 0.0

        self.y = 100
        self.y_vel = 0
        self.jump_vel = -10
        super().__init__()

    def data_slice_screen(self, level:int, x:float, lines_per_level:int=8):
        x_start:int = int(x) // self.tile_size
        x_end  :int = x_start + (self.width // self.tile_size) + self.tile_size
        return [
            self.level_data[line_num][x_start:x_end]
            for line_num in range((level)*lines_per_level, (level+1)*lines_per_level)
        ]

    def loop(self, screen, frame):
        s = screen

        self.x += self.speed
        #if self.keys[pygame.K_RIGHT]:
        #    self.x += 1
        #if self.keys[pygame.K_LEFT]:
        #    self.x += -1

        x_draw_offset = (self.width / self.tile_size) * self.speed * 4
        screen_data = self.data_slice_screen(self.level, self.x-x_draw_offset)

        is_on_ground = self.y >= self.height - self.tile_size
        self.y = min(self.height - self.tile_size, self.y)
        if is_on_ground:
            self.y_vel = 0
            if self.keys[pygame.K_SPACE]:
                self.y_vel = self.jump_vel
        else:
            self.y_vel += 1
        self.y += self.y_vel

        tile_x_offset = int(self.x % self.tile_size)
        for tile_y, line in enumerate(screen_data):
            for tile_x, chr in enumerate(line):
                if chr == ' ': continue
                s.blit(self.tiles[chr], (tile_x * self.tile_size - tile_x_offset, tile_y * self.tile_size))
        s.blit(self.tiles['@'], (x_draw_offset, self.y))


if __name__ == '__main__':
    GeometryDash().run()
