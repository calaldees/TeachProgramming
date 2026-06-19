import math
from collections.abc import Sequence
from typing import NamedTuple, Self

import pygame

from animation_base_pygame import PygameBase

class Point():
    x: float
    y: float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    @classmethod
    def from_array(cls, x:float, y:float) -> Self:
        return cls(x, y)
    @property
    def to_array(self):
        return (self.x, self.y)
    def translate(self, b: Self) -> None:
        self.x += b.x
        self.y += b.y
    def euclidean_distance(self, p) -> float:
        return pow(self.x - p.x, 2) + pow(self.y - p.y, 2)
    def distance(self, p) -> float:
        return math.sqrt(self.euclidean_distance(p))

class Line():
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    @classmethod
    def from_array(cls, x1:float, y1:float, x2:float, y2:float) -> Self:
        return cls(Point(x1, y1), Point(x2, y2))
    @property
    def to_array(self) -> Sequence[float]:
        return (self.p1.x, self.p1.y, self.p2.x, self.p2.y)
    def translate(self, p: Point) -> None:
        self.p1.translate(p)
        self.p2.translate(p)
    @staticmethod
    def _gradient(p1:Point, p2:Point) -> float:
        return (p1.x-p2.x)/(p1.y-p2.y)
    @property
    def gradient(self) -> float:
        return self._gradient(self.p1, self.p2)
    @property
    def length(self) -> float:
        return self.p1.distance(self.p2)
    def intersect(self, line) -> Point | bool:
        """
        https://paulbourke.net/geometry/pointlineplane/javascript.txt
        line intercept math by Paul Bourke http://paulbourke.net/geometry/pointlineplane/
        Determine the intersection point of two line segments - Return FALSE if the lines don't intersect
        intersect(x1, y1, x2, y2, x3, y3, x4, y4) {
        """
        (x1, y1, x2, y2, x3, y3, x4, y4) = self.to_array + line.to_array
        if ((x1==x2 and y1==y2) or (x3==x4 and y3==y4)):
            return False  # Check if none of the lines are of length 0
        # Perhaps this zero length can be removed because `new Line(0,0,0,0)` would error
        denominator = ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
        if denominator == 0:
            return False  # Lines are parallel
        ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator
        ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator
        if (ua < 0 or ua > 1 or ub < 0 or ub > 1):
            return False  # is the intersection along the segments
        return Point(x1 + ua * (x2 - x1), y1 + ua * (y2 - y1))  # return [x, y] of intersect point


class Vector():
    """
    >>> v = Vector()
    """
    x: float
    y: float
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, b: Self) -> None:
        self.x += b.x
        self.y += b.y
    def __iadd__(self, b: Self) -> Self:
        self.add(b)
        return self
    # def __add__(a: Self, b: Self) -> Self:
    #    return None
    def reset(self) -> None:
        self.x = 0
        self.y = 0

class Mass(NamedTuple):
    p: Point
    f: Vector
    m: float
    def add_force(self, f: Vector) -> None:
        self.f.add(f)
    def apply_force(self) -> None:
        self.p.x += self.f.x
        self.p.y += self.f.y
        self.f.reset()

class Spring():
    a: Mass
    b: Mass
    initial_length: float
    def __init__(self, a: Mass, b: Mass):
        self.a = a
        self.b = b
        self.line = Line(a.p, b.p)
        self.initial_length = self.line.length


class GameDemo(PygameBase):
    def __init__(self):
        self.x = 100
        self.y = 100
        # self.image = pygame.image.load('images/block.gif')
        super().__init__()

    def loop(self, screen, frame):
        s = screen
        width, height = s.get_size()

        t = frame % width
        pygame.draw.rect(s, pygame.Color("#f0b000"), (t, 10, 120, 80))

        t = frame % height
        pygame.draw.line(s, pygame.Color("red"), (t, t), (t+10, t+10), 5)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        # s.blit(self.image, (mouse_x, mouse_y))

        if self.keys[pygame.K_UP]:
            self.y += -1
        if self.keys[pygame.K_DOWN]:
            self.y += 1
        if self.keys[pygame.K_RIGHT]:
            self.x += 1
        if self.keys[pygame.K_LEFT]:
            self.x += -1
        # s.blit(self.image, (self.x, self.y))


        # Task DVD menu
        # 1.) Square edged red rectangle - 50 50
        # 2.) It moves automatically (in the x direction only)
        # 3.) It bounces left and right from the edges of the screen
        # 4.) DVD screensaver - bounces of top bottom left right
        # 5.) Make the rectangle an image
        # 6.) Remove any hard coded values for width/height/imagesize/etc

if __name__ == '__main__':
    GameDemo().run()
