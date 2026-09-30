import random


class Star:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def __repr__(self):
        return f"Star(({self.x}, {self.y}), {self.speed=})"
    def move(self):
        self.x += self.speed


class Stars:
    def __init__(self, width: int, height: int, density: float = 0.001):
        self.density = density
        self.resize(width, height)
    def resize(self, width:int, height:int) -> None:
        self.width = width or self.width
        self.height = height or self.height
        self.stars = [
            Star(
                random.randint(0, self.width),
                random.randint(0, self.height),
                random.randint(1, 6),
            )
            for i in range(int(self.width * self.height * self.density))
        ]
    def move(self) -> None:
        for s in self.stars:
            s.move()
            if s.x > self.width:
                s.x = 0
                s.y = random.randint(0, self.height)


stars = Stars(width=480, height=270)


import pygame
pygame.init()
screen = pygame.display.set_mode((480,270), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()
while True:
    pygame.display.update()
    clock.tick(60)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

    stars.move()

    screen.fill('black')
    for star in stars.stars:
        pygame.draw.rect(screen, (255,255,255), (star.x, star.y, star.speed, 1))

pygame.quit()