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


def draw_tiles(screen: pygame.Surface, tiles: Tiles, screen_data: LevelData, screen_x: int, screen_y: int) -> None:
    max_x, max_y = (len(screen_data[0]), len(screen_data))
    t_reference = next(iter(tiles.values()))  # get first tile and extract the tile dimensions
    tw, th = (t_reference.width, t_reference.height)
    stw, sth = (screen.width//tw, screen.height//th)
    tx, ty = (screen_x//tw, screen_y//th)
    x_offset, y_offset = (screen_x%tw, screen_y%th)
    for _y in range(sth+2):
        for _x in range(stw+2):
            x, y = (_x+tx, _y+ty)
            if x<0 or y<0 or x>=max_x or y>=max_y: continue
            t = screen_data[y][x]
            if t == ' ': continue
            screen.blit(tiles[t], ((_x*tw)-x_offset, (_y*th)-y_offset))


class MouseBlast(PygameBase):
    def __init__(self):
        self.level_data = load_levels(Path('geometry_dash.txt'))
        self.tile_size = 32
        self.tiles = load_tiles(Path('geometry_dash.png'), '@^#_', self.tile_size)
        super().__init__(fps=60)
        self.reset()

    def reset(self) -> None:
        self.x: float = self.screen.width
        self.y: float = self.screen.height

    def loop(self, screen, frame):
        if self.keys[pygame.K_w]: self.y-=1
        if self.keys[pygame.K_s]: self.y+=1
        if self.keys[pygame.K_a]: self.x-=1
        if self.keys[pygame.K_d]: self.x+=1
        mouse_x, mouse_y = pygame.mouse.get_pos()
        fire = self.keys[pygame.K_SPACE]

        screen_x = self.x-(screen.width //2) + (mouse_x-(screen.width //2))
        screen_y = self.y-(screen.height//2) + (mouse_y-(screen.height//2))
        draw_tiles(screen, self.tiles, self.level_data, screen_x, screen_y)

        player_x, player_y = (self.x-screen_x, self.y-screen_y)
        pygame.draw.rect(screen, pygame.Color("#f0b000"), (player_x, player_y, 5, 5))
        pygame.draw.rect(screen, pygame.Color("#f00000"), (mouse_x, mouse_y, 5, 5))
        if fire:
            pygame.draw.line(screen, pygame.Color("#00ffff"), (player_x, player_y), (mouse_x, mouse_y), 1)

if __name__ == '__main__':
    MouseBlast().run()
