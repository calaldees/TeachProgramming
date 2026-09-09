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


def draw_tiles(screen: pygame.Surface, tiles: Tiles, screen_data: LevelData, x:int, y:int) -> None:
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

        self.speed: float = 2.5
        self.jump_vel: float = -5
        self.jump_vel_inc: float = 0.2
        self.reset()

        super().__init__(fps=60)

    def reset(self) -> None:
        self.x: float = 0.0
        self.y: float = 150
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
        x_screen_offset = 50 # (self.width / self.tile_size) * self.speed * 4

        self.x += self.speed
        self.y += self.y_vel
        #if self.keys[pygame.K_RIGHT]:
        #    self.x += 1
        #if self.keys[pygame.K_LEFT]:
        #    self.x += -1
        screen_data = self.data_slice_screen(self.level, self.x)

        x_tile = int(x_screen_offset)//self.tile_size
        y_tile = int(self.y)//self.tile_size
        if screen_data[y_tile+1][x_tile] not in (' ', '^'):  # Title below
            pygame.draw.rect(s, pygame.Color("#f0b000"), (x_screen_offset, self.y, self.tile_size, self.tile_size))
            y_floor = y_tile * self.tile_size
        if screen_data[y_tile][x_tile] not in (' ', '_'):
            self.y_vel = 0
            #self.y = self.tile_size * y_tile+1
            y_tile += 1
        if screen_data[y_tile][x_tile+1] not in (' ', '_'):  # tile_infront
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
        #self.draw_level(screen, screen_data, x_scroll_backshift)
        draw_tiles(screen, self.tiles, self.level_data, int(self.x), 0)

        #s.blit(self.tiles['@'], (x_draw_offset, self.y))
        s.blit(*rotate_image_center(self.tiles['@'], x_screen_offset, self.y, self.rotation))


if __name__ == '__main__':
    GeometryDash().run()
