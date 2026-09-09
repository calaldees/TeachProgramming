from collections.abc import Mapping, Sequence
from pathlib import Path

import pygame

from animation_base_pygame import PygameBase


type LevelData = Sequence[str]
type LevelDataSlice = Sequence[str]
type Tile = str


def load_geometry_dash_levels(path: Path, width=120) -> LevelData:
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

        self.speed: float = 1.0
        self.jump_vel: float = -3.5
        self.jump_vel_inc: float = 0.11
        self.reset()

        super().__init__(fps=120)

    def reset(self) -> None:
        self.x: float = 0.0
        self.y: float = 100
        self.y_vel:float = 0
        self.rotation:float = 0

    def data_slice_screen(self, level:int, x:float, lines_per_level:int=8) -> LevelDataSlice:
        level_width_tiles = len(self.level_data[0])
        screen_width_tiles = (self.width // self.tile_size)
        x_start:int = max(0, int(x) // self.tile_size)
        x_end  :int = min(level_width_tiles, x_start + screen_width_tiles)
        return [
            self.level_data[line_num][x_start:x_end]
            for line_num in range((level)*lines_per_level, (level+1)*lines_per_level)
        ]

    def draw_level(self, screen: pygame.screen, screen_data: LevelDataSlice, x_scroll_backshift: int) -> None:
        #tile_x_offset = int(self.x % self.tile_size)
        for tile_y, line in enumerate(screen_data):
            for tile_x, chr in enumerate(line):
                if chr == ' ': continue
                screen.blit(self.tiles[chr], (tile_x * self.tile_size + x_scroll_backshift, tile_y * self.tile_size))

    def loop(self, screen, frame):
        s = screen

        y_floor = self.height - self.tile_size
        x_screen_offset = (self.width / self.tile_size) * self.speed * 4

        self.x += self.speed
        self.y += self.y_vel
        #if self.keys[pygame.K_RIGHT]:
        #    self.x += 1
        #if self.keys[pygame.K_LEFT]:
        #    self.x += -1
        screen_data = self.data_slice_screen(self.level, self.x)

        x_tile = int(x_screen_offset)//self.tile_size
        y_tile = int(self.y)//self.tile_size
        if screen_data[y_tile+1][x_tile] != ' ':  # Title below
            pygame.draw.rect(s, pygame.Color("#f0b000"), (x_screen_offset, self.y, self.tile_size, self.tile_size))
            y_floor = y_tile * self.tile_size
        if screen_data[y_tile][x_tile] != ' ':
            self.y_vel = 0
            #self.y = self.tile_size * y_tile+1
            y_tile += 1
        if screen_data[y_tile][x_tile+1] != ' ':  # tile_infront
            self.reset()
        is_on_ground = (self.y >= y_floor)
        self.y = min(y_floor, self.y)

        if is_on_ground:
            self.y_vel = 0
            if self.keys[pygame.K_SPACE]:
                self.y_vel = self.jump_vel
        else:
            self.y_vel += self.jump_vel_inc
            self.rotation -= 4

        x_scroll_backshift = self.tile_size - int(self.x) % self.tile_size
        self.draw_level(screen, screen_data, x_scroll_backshift)

        rotated_image = pygame.transform.rotate(self.tiles['@'], self.rotation)
        rotated_rect = rotated_image.get_rect()
        rotated_rect.center = (self.tile_size//2, self.tile_size//2)
        rotated_rect.x = x_screen_offset
        rotated_rect.y = self.y
        #pygame.draw.rect(s, pygame.Color("#f00000"),rotated_rect)
        s.blit(rotated_image, rotated_rect)
        #s.blit(self.tiles['@'], (x_draw_offset, self.y))


if __name__ == '__main__':
    GeometryDash().run()
