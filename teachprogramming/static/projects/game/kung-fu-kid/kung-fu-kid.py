# https://www.spriters-resource.com/master_system/kungfukid/
# https://www.smspower.org/Games/KungFuKid-SMS
# https://www.smspower.org/uploads/Maps/KungFuKid-SMS-Round1.png

from collections.abc import Sequence, Mapping
from typing import NamedTuple
import enum

import pygame

pygame.init()
screen = pygame.display.set_mode((480, 270), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()


class Level:
    def __init__(self, filename):
        self.background = pygame.image.load(filename)


class ActionState(enum.Flag):
    NONE = enum.auto()
    STAND = enum.auto()
    CROUCH = enum.auto()
    AIR = enum.auto()
    WALK = enum.auto()
    ATTACK = enum.auto()
    HURT = enum.auto()
    FALLEN = enum.auto()
    ATTACK_RANGE = enum.auto()


class Character:
    def __init__(self, filename: str):
        self.sprites = pygame.image.load(filename)

        def s(x, y=8):
            return self.sprites.subsurface((x, y, 32, 32))

        self.frames = {
            ActionState.STAND: [s(3)],
            ActionState.WALK: [s(58), s(32), s(90), s(32)],
            ActionState.STAND | ActionState.ATTACK: [s(128), s(162)],
            ActionState.CROUCH: [s(192), s(162)],
            ActionState.CROUCH | ActionState.ATTACK: [s(221)],
            ActionState.AIR: [s(258), s(394)],
            ActionState.AIR | ActionState.ATTACK: [s(292, 12)],  # 296
            ActionState.ATTACK_RANGE: [s(332), s(364)],
            ActionState.HURT: [s(426)],
            ActionState.FALLEN: [s(464)],
        }


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, b) -> "Point":
        return Point(self.x + b.x, self.y + b.y)

    def __sub__(self, b) -> "Point":
        return Point(self.x - b.x, self.y - b.y)

    def __neg__(self) -> "Point":
        return Point(-self.x, -self.y)


class SpriteDirection(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()


class Char:
    def __init__(
        self,
        c: Character,
        p: Point = Point(0, 0),
        s: ActionState = ActionState.STAND,
        d: SpriteDirection = SpriteDirection.RIGHT,
    ):
        self.c = c
        self.p = p
        self.s = s
        self.d = d
        self.impulse = 0
        self.frame = 0


class Input(enum.Flag):
    NONE = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()
    LEFT = enum.auto()
    RIGHT = enum.auto()
    JUMP = enum.auto()
    ATTACK = enum.auto()


player_key_mapping_to_input: Mapping[pygame.key, Input] = {
    pygame.K_UP: Input.UP,
    pygame.K_DOWN: Input.DOWN,
    pygame.K_RIGHT: Input.RIGHT,
    pygame.K_LEFT: Input.LEFT,
    pygame.K_z: Input.JUMP,
    pygame.K_x: Input.ATTACK,
}


def keys_to_input(key_mapping: Mapping[pygame.key, Input], keys: pygame.keys) -> Input:
    # def f(input: Input, i:tuple[pygame.key, Input]) -> Input:
    #    return (input | i[1] if keys[i[0]] else Input.NONE)
    # ii = reduce(f, mapping.items(), Input.NONE)
    input = Input.NONE
    for k, i in key_mapping.items():
        # if k == pygame.K_SPACE and keys[pygame.K_SPACE]:
        #    breakpoint()
        input |= i if keys[k] else Input.NONE
    return input


class CharStateTransformer:
    def transform(self, c: Char, i: Input) -> Char:
        # if Input.JUMP in i:
        #    breakpoint()
        p = c.p
        s = c.s
        d = c.d
        if (Input.DOWN in i and ActionState.STAND in s) or (
            Input.DOWN not in i and ActionState.CROUCH in s
        ):
            s ^= ActionState.CROUCH
            s ^= ActionState.STAND
        if ActionState.WALK in s and not ((Input.LEFT | Input.RIGHT) & i):
            s = ActionState.STAND
        if (ActionState.ATTACK in s and Input.ATTACK not in i) or (
            ActionState.ATTACK not in s and Input.ATTACK in i
        ):
            s ^= ActionState.ATTACK
        if ActionState.ATTACK in s and ActionState.WALK in s:
            s ^= ActionState.WALK
            s |= ActionState.STAND
        if (Input.LEFT | Input.RIGHT) & i and (
            ActionState.STAND in s and ActionState.ATTACK not in s
        ):
            s = ActionState.WALK
        # LEFT or RIGHT
        if (ActionState.AIR | ActionState.WALK) & s:
            if Input.LEFT in i:
                p = c.p + Point(-1, 0)
                d = SpriteDirection.LEFT
            if Input.RIGHT in i:
                p = c.p + Point(1, 0)
                d = SpriteDirection.RIGHT
        # Check FALL (only when walking)
        if ActionState.WALK in s:
            pass  # TODO check standing on ground else transition to air
        # Fall
        if ActionState.AIR in c.s:
            p = p + Point(0, 1)
            if p.y > 144:
                return Char(c.c, Point(p.x, 144), ActionState.STAND, d)
        if (ActionState.CROUCH | ActionState.STAND | ActionState.WALK) & s:
            if Input.JUMP in i:
                return Char(c.c, Point(p.x, p.y - 100), ActionState.AIR, d)
        return Char(c.c, p, s, d)


level = Level("KungFuKid-SMS-Round1.png")
character = Character("wang.png")
char_transformer = CharStateTransformer()

chars: Sequence[Char] = [
    Char(character, Point(100, 144), ActionState.STAND),
    Char(character, Point(30, 100), ActionState.AIR),
    Char(
        character,
        Point(300, 60),
        ActionState.AIR | ActionState.ATTACK,
        SpriteDirection.LEFT,
    ),
]
frame = 0
viewport = Point(0, 0)

while True:
    pygame.display.update()
    clock.tick(60)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

    # viewport = Point(viewport.x + 1, viewport.y)
    screen.blit(level.background, -viewport)
    walk_frames = character.frames[ActionState.WALK]
    # screen.blit(walk_frames[(frame//16)%len(walk_frames)], (100, 144))

    input = keys_to_input(player_key_mapping_to_input, keys)
    # if frame == 120:
    #    breakpoint()
    chars[0] = char_transformer.transform(chars[0], input)

    for char in chars:
        screen.blit(
            pygame.transform.flip(
                char.c.frames[char.s][0],
                flip_x=char.d == SpriteDirection.LEFT,
                flip_y=False,
            ),
            char.p - viewport,
        )

    frame += 1

pygame.quit()

"""

STAND (left, right, jump, hit, collide_floor, attack)
WALK (left, right, jump, hit, collide_floor)
AIR (left, right, collide_floor, attack)
HURT (timer)

"""
