from collections.abc import Mapping, Sequence
from pathlib import Path

import pygame

from animation_base_pygame import PygameBase


type LevelData = Sequence[str]
type LevelDataSlice = Sequence[str]
type Tile = str
type Tiles = Mapping[str, pygame.Surface]


def load_levels(path: Path, width=120) -> LevelData:
    lines = []
    with path.open() as f:
        while line := f.readline():
            lines.append(line.removesuffix('\n').ljust(width, ' '))
    return lines


def load_tiles(path: Path, seq: str, w: int, h: int = 0) -> Tiles:
    h = h or w
    img = pygame.image.load(path)
    ww, hh = img.get_size()
    return {
        seq[i]: img.subsurface(((i*w)%ww, ((i*w)//ww)*h, w, h))
        for i in range(min((ww//w)*(hh//h), len(seq)))
    }


def draw_tiles(screen: pygame.Surface, tiles: Tiles, screen_data: LevelData, x: int, y: int) -> None:
    t_reference = next(iter(tiles.values()))  # get first tile and extract the tile dimensions
    tw, th = (t_reference.width, t_reference.height)
    stw, sth = (screen.width//tw, screen.height//th)
    tx, ty = (x//tw, y//th)
    x_offset, y_offset = (x%tw, y%th)
    for _y in range(sth+1):
        for _x in range(stw+1):
            t = screen_data[_y+ty][_x+tx]
            if t == ' ': continue
            screen.blit(tiles[t], ((_x*tw)-x_offset, (_y*th)-y_offset))


def rotate_image_center(img:pygame.image, x:float, y:float, angle:float) -> tuple[pygame.image, pygame.rectangle]:
    rotated_image = pygame.transform.rotate(img, angle)
    rotated_rect = rotated_image.get_rect()
    rotate_offset_x = (rotated_rect.width-img.width)//2
    rotate_offset_y = (rotated_rect.height-img.height)//2
    rotated_rect.center = (img.width//2, img.height//2)
    rotated_rect.x = x - rotate_offset_x
    rotated_rect.y = y - rotate_offset_y
    return (rotated_image, rotated_rect)



class GeometryDash(PygameBase):
    def __init__(self):
        self.level_data = load_levels(Path('geometry_dash.txt'))
        self.tile_size = 32
        self.tiles = load_tiles(Path('geometry_dash.png'), '@^#_', self.tile_size)

        self.level: int = 0

        self.screen_speed: float = 2.5
        self.jump_vel: float = -5
        self.jump_vel_inc: float = 0.2
        self.rotate_inc: float = -4
        self.reset()

        super().__init__(fps=60)

    def reset(self) -> None:
        self.x: float = 0.0
        self.y: float = 150
        self.y_vel:float = 0
        self.rotation:float = 0

    def loop(self, screen, frame):
        s = screen

        y_floor_max = self.height - self.tile_size
        x_screen_offset = (s.width // self.tile_size) * self.screen_speed

        self.x += self.screen_speed
        self.y += self.y_vel

        x_tile = int(self.x+x_screen_offset)//self.tile_size
        y_tile = int(self.y)//self.tile_size
        if self.level_data[y_tile+1][x_tile] not in (' ', '^'):  # Title below
            pygame.draw.rect(s, pygame.Color("#f0b000"), (x_screen_offset, self.y, self.tile_size, self.tile_size))
            y_floor_max = y_tile * self.tile_size
        if self.level_data[y_tile][x_tile] not in (' ', '_'):  # Tile above?
            self.y_vel = 0
            y_tile += 1  # HACK: for future collisions, treat this as the tile below
        if self.level_data[y_tile][x_tile+1] not in (' ', '_'):  # tile_infront
            self.reset()

        is_on_ground = (self.y >= y_floor_max)
        self.y = min(y_floor_max, self.y)
        if is_on_ground:
            self.y_vel = 0
            if self.keys[pygame.K_SPACE]:
                self.y_vel = self.jump_vel
        else:
            self.y_vel += self.jump_vel_inc
            self.rotation += self.rotate_inc

        draw_tiles(screen, self.tiles, self.level_data, int(self.x), 0)

        #s.blit(self.tiles['@'], (x_draw_offset, self.y))
        s.blit(*rotate_image_center(self.tiles['@'], x_screen_offset, self.y, self.rotation))


if __name__ == '__main__':
    GeometryDash().run()
