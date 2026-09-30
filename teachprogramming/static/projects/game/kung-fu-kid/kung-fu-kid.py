# https://www.spriters-resource.com/master_system/kungfukid/
# https://www.smspower.org/Games/KungFuKid-SMS
# https://www.smspower.org/uploads/Maps/KungFuKid-SMS-Round1.png


import enum

import pygame
pygame.init()
screen = pygame.display.set_mode((480,270), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()


class Level():
    def __init__(self, filename):
        self.background = pygame.image.load(filename)
        self.x = 0
        self.y = 0

class SpriteState(enum.Flag):
    STAND = enum.auto()
    CROUCH = enum.auto()
    AIR = enum.auto()
    WALK = enum.auto()
    ATTACK = enum.auto()
    HURT = enum.auto()
    FALLEN = enum.auto()
    SPECIAL = enum.auto()

class Character():
    def __init__(self, filename: str):
        self.x = 0
        self.y = 0
        self.state = SpriteState.STAND
        self.sprites = pygame.image.load(filename)
        def s(x):
            return self.sprites.subsurface((x,8,32,32))
        self.frames = {
            SpriteState.STAND: [s(3)],
            SpriteState.WALK: [s(58), s(32), s(90), s(32)],
            SpriteState.STAND | SpriteState.ATTACK: [s(128), s(162)],
            SpriteState.CROUCH: [s(192), s(162)],
            SpriteState.CROUCH | SpriteState.ATTACK: [s(221)],
            SpriteState.AIR: [s(258), s(394)],
            SpriteState.AIR | SpriteState.ATTACK: [s(296)],
            SpriteState.SPECIAL: [s(332), s(364)],
            SpriteState.HURT: [s(426)],
            SpriteState.FALLEN: [s(464)],
        }

class Player():
    def __init__(self, character: Character):
        pass


level = Level("KungFuKid-SMS-Round1.png")
character = Character("wang.png")
frame = 0

while True:
    pygame.display.update()
    clock.tick(60)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

    level.x -= 1
    screen.blit(level.background, (level.x, level.y))
    walk_frames = character.frames[SpriteState.WALK]
    screen.blit(walk_frames[(frame//16)%len(walk_frames)], (100, 144))

    frame += 1

pygame.quit()

"""

STAND (left, right, jump, hit, collide_floor, attack)
WALK (left, right, jump, hit, collide_floor)
AIR (left, right, collide_floor, attack)
HURT (timer)

"""