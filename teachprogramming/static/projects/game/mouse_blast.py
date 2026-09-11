import math
from collections.abc import Mapping, Sequence, MutableSequence
from pathlib import Path

import pygame

from animation_base_pygame import PygameBase


type TileID = str  # str of length 1
type LevelRow = str
type LevelData = Sequence[LevelRow]
type Tiles = Mapping[str, pygame.Surface]


class TileManager():

    @staticmethod
    def load_levels(path: Path, width=120) -> LevelData:
        lines = []
        with path.open() as f:
            while line := f.readline():
                lines.append(line.removesuffix('\n').ljust(width, ' '))
        return lines

    @staticmethod
    def load_tiles(path: Path, seq: str, w: int, h: int = 0) -> Tiles:
        h = h or w
        img = pygame.image.load(path)
        ww, hh = img.get_size()
        return {
            seq[i]: img.subsurface(((i*w)%ww, ((i*w)//ww)*h, w, h))
            for i in range(min((ww//w)*(hh//h), len(seq)))
        }

    def __init__(self, tiles: Tiles, level_data: LevelData):
        self.tiles = tiles
        self.level_data = level_data

        self.level_width, self.level_height = (len(level_data[0]), len(level_data))
        _t = next(iter(tiles.values()))  # get first tile and extract the tile dimensions
        self.tile_width, self.tile_height = (_t.width, _t.height)

    def draw_tiles(self, screen: pygame.Surface, screen_x: int, screen_y: int) -> None:
        tw, th = (self.tile_width, self.tile_height)
        stw, sth = (screen.width//tw, screen.height//th)
        tx, ty = (screen_x//tw, screen_y//th)
        x_offset, y_offset = (screen_x%tw, screen_y%th)
        for _y in range(sth+2):
            for _x in range(stw+2):
                x, y = (_x+tx, _y+ty)
                if x<0 or y<0 or x>=self.level_width or y>=self.level_height: continue
                t:TileID = self.level_data[y][x]
                if t == ' ': continue
                screen.blit(self.tiles[t], ((_x*tw)-x_offset, (_y*th)-y_offset))

    def get_tile(self, x:int, y:int) -> TileID:
        return self.level_data[y//self.tile_height][x//self.tile_width]


class Bullet():
    def __init__(self, x:float, y:float, x_vel:float, y_vel:float):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.duration:int = 0

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.duration += 1


def angle(p1_x, p1_y, p2_x, p2_y) -> float:
    dx_dy = (p1_x-p2_x) / (p1_y-p2_y) if p1_y!=p2_y else math.inf
    if dx_dy==math.inf and p1_x > p2_x:
        return math.pi/2  # This is a weird special case I don't understand
    angle = math.atan(dx_dy)
    if p1_y <= p2_y:
        angle += math.pi
    return angle


class MouseBlast(PygameBase):
    def __init__(self):
        self.tiles = TileManager(
            tiles=TileManager.load_tiles(Path('geometry_dash.png'), '@^#_', 32),
            level_data=TileManager.load_levels(Path('geometry_dash.txt')),
        )
        super().__init__(fps=60)
        self.reset()

    def reset(self) -> None:
        self.x: float = self.screen.width
        self.y: float = self.screen.height
        self.bullets: MutableSequence[Bullet] = []

    def loop(self, screen, frame):
        if self.keys[pygame.K_w]: self.y-=1
        if self.keys[pygame.K_s]: self.y+=1
        if self.keys[pygame.K_a]: self.x-=1
        if self.keys[pygame.K_d]: self.x+=1
        mouse_x, mouse_y = pygame.mouse.get_pos()
        fire = self.keys[pygame.K_SPACE]

        screen_x = self.x - (screen.width //2) + (mouse_x-(screen.width //2))
        screen_y = self.y - (screen.height//2) + (mouse_y-(screen.height//2))
        screen_x = min(max(0, screen_x), self.tiles.level_width*self.tiles.tile_width)
        screen_y = min(max(0, screen_y), self.tiles.level_height*self.tiles.tile_height)
        player_x, player_y = (self.x-screen_x, self.y-screen_y)

        a = angle(mouse_x, mouse_y, player_x, player_y)
        vel = 2.5
        if fire:
            self.bullets.append(Bullet(self.x, self.y, x_vel=math.sin(a)*vel, y_vel=math.cos(a)*vel))
        for b in self.bullets:
            b.move()
        self.bullets = [
            b
            for b in self.bullets
            if b.duration<200 and self.tiles.get_tile(int(b.x), int(b.y)) == ' '
        ]

        self.tiles.draw_tiles(screen, screen_x, screen_y)
        pygame.draw.rect(screen, pygame.Color("#f0b000"), (player_x, player_y, 5, 5))
        pygame.draw.rect(screen, pygame.Color("#f00000"), (mouse_x, mouse_y, 5, 5))
        if fire:
            pygame.draw.line(screen, pygame.Color("#00ffff"), (player_x, player_y), (mouse_x, mouse_y), 1)

        for b in self.bullets:
            pygame.draw.rect(screen, pygame.Color("#ffffff"), (b.x-screen_x, b.y-screen_y, 1, 1))


if __name__ == '__main__':
    MouseBlast().run()
