import math
from collections.abc import Sequence
from typing import NamedTuple, Self
from itertools import chain

import pygame

from animation_base_pygame import PygameBase

class Point():
    x: float
    y: float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x},{self.y})'
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
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.p1},{self.p2})'
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
    def _dx_dy(p1:Point, p2:Point) -> float:
        if (p1.y==p2.y):
            return math.inf
        return (p1.x-p2.x)/(p1.y-p2.y)
    @property
    def dx_dy(self) -> float:
        return self._dx_dy(self.p1, self.p2)
    @property
    def length(self) -> float:
        return self.p1.distance(self.p2)
    @property
    def angle(self) -> float:
        dx_dy = self.dx_dy
        if dx_dy==math.inf and self.p1.x > self.p2.x:
            # This is a weird special case I don't understand
            return math.pi/2
        angle = math.atan(dx_dy)
        if self.p1.y <= self.p2.y:
            angle += math.pi
        return angle
        
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
    def __init__(self, x:float=0, y:float=0):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x:.2f},{self.y:.2f})'
    @property
    def to_array(self) -> Sequence[float]:
        return (self.x, self.y)
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
    @classmethod
    def from_angle(cls, angle: float, value: float) -> Self:
        return cls(x=math.sin(angle)*value,y=math.cos(angle)*value)
    def __neg__(self):
        return Vector(-self.x, -self.y)

class Mass():
    def __init__(self, p: Point, mass: float):
        self.p = p
        self.mass = mass
        self.force = Vector()
        self.vel = Vector()
    def add_force(self, f: Vector) -> None:
        self.force.add(f)
    def apply_force(self) -> None:
        self.vel.x += self.force.x / self.mass
        self.vel.y += self.force.y / self.mass
        self.force.reset()
        self.p.x += self.vel.x
        self.p.y += self.vel.y

class SpringMaterial(NamedTuple):
    tension: float
    compression: float

class Spring():
    def __init__(self, a: Mass, b: Mass, mat: SpringMaterial):
        self.a = a
        self.b = b
        self.mat = mat
        self.line = Line(a.p, b.p)
        self.initial_length = self.line.length
    def add_force(self) -> None:
        length = self.line.length
        length_factor = (length-self.initial_length)/self.initial_length
        force_mat = (self.mat.tension if length > self.initial_length else self.mat.compression)
        force_magnitude = length_factor * force_mat
        # positive = line is longer = apply force to attract masses
        # negative = line is shorter = apply force to repl masses
        angle = self.line.angle
        force_vector = Vector.from_angle(angle, force_magnitude)
        self.a.add_force(-force_vector)
        self.b.add_force(force_vector)


class Lattice(NamedTuple):
    masses: Sequence[Mass]
    springs: Sequence[Spring]

    @classmethod
    def build(
        cls,
        x_start:int, 
        y_start:int, 
        width:int, 
        height:int, 
        unit_length: float, 
        unit_mass: float, 
        mat: SpringMaterial,
    ) -> Self:
        m: Sequence[Mass] = tuple(
            Mass(Point(x_start+(x*unit_length),y_start+(y*unit_length)), unit_mass)
            for x in range(width+1)
            for y in range(height+1)
        )
        def xy_to_i(x,y):
            return x+y*(width+1)
        s: Sequence[Spring] = tuple(chain.from_iterable(
            (
                Spring(m[xy_to_i(x  ,y  )], m[xy_to_i(x+1,y  )], mat), # top
                Spring(m[xy_to_i(x+1,y  )], m[xy_to_i(x+1,y+1)], mat), # right
                Spring(m[xy_to_i(x+1,y+1)], m[xy_to_i(x  ,y+1)], mat), # bottom
                Spring(m[xy_to_i(x  ,y+1)], m[xy_to_i(x  ,y  )], mat), # left
                Spring(m[xy_to_i(x  ,y  )], m[xy_to_i(x+1,y+1)], mat), # top-left to bottom-right
                Spring(m[xy_to_i(x+1,y  )], m[xy_to_i(x  ,y+1)], mat), # top-right to bottom-left
            )
            for x in range(width)
            for y in range(height)
        ))
        return cls(m,s)

class GameDemo(PygameBase):
    def __init__(self):
        self.l = Lattice.build(100,100,3,3,10,1,SpringMaterial(1,1))
        # m1 = Mass(Point(100,100), 10)
        # m2 = Mass(Point(110,100), 10)
        # self.l = Lattice(
        #    masses=(m1,m2,),
        #    springs=(Spring(m1,m2,SpringMaterial(1,1)),)
        # )
        # m2.p.x += 2
        # m2.p.y += 2
        super().__init__()

    def loop(self, screen, frame):
        s = screen
        width, height = s.get_size()

        # m2 =self.l.masses[1]
        # m2.p.x = 100 + math.sin(frame/60)*12
        # m2.p.y = 100 + math.cos(frame/60)*12
        # if self.keys[pygame.K_UP]:
        #     m2.p.y += -1
        # if self.keys[pygame.K_DOWN]:
        #     m2.p.y += 1
        # if self.keys[pygame.K_RIGHT]:
        #     m2.p.x += 1
        # if self.keys[pygame.K_LEFT]:
        #     m2.p.x += -1

        for mass in self.l.masses:
            mass.add_force(Vector(0,mass.mass*0.01))  # Gravity
            #mass.add_force(Vector(-mass.vel.x/300,-mass.vel.y/300))  # Air Viscosity
            mass.vel.x *= 0.99
            mass.vel.y *= 0.99
        for spring in self.l.springs:
            spring.add_force()
        c = pygame.Color("green")
        for mass in self.l.masses:
            pygame.draw.line(s, c, mass.p.to_array , (mass.p.x+(mass.force.x*20), mass.p.y+(mass.force.y*20)), 1)
            mass.apply_force()  # move all the masses with force - remove the accumulated force
            #mass.force.reset()
        for mass in self.l.masses:
            if mass.p.y > height:
                mass.p.y = float(height)
                mass.vel.y = -mass.vel.y * 0.8

        c = pygame.Color("white")
        for spring in self.l.springs:
            pygame.draw.line(s, c, spring.a.p.to_array , spring.b.p.to_array, 1)
        c = pygame.Color("yellow")
        for mass in self.l.masses:
            x, y = mass.p.to_array
            pygame.draw.rect(s, c, (x-1, y-1, 3, 3))


if __name__ == '__main__':
    GameDemo().run()
