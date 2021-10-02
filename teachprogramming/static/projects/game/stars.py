import pygame as pg

class GameBase():
    def __init__(self, title="pg", resolution=(320,180), fps=60, color_background='black'):
        pg.init()
        pg.display.set_caption(title)
        self.screen = pg.display.set_mode(resolution, pg.SCALED | pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.fps = fps
        self.color_background = color_background
    def run(self):
        frame = 0
        self.running = True
        while self.running:
            self.clock.tick(self.fps)
            self.keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                    self.running = False
                if event.type == pg.VIDEORESIZE:
                    pg.display._resize_event(event)
                if (self.keys[pg.K_RALT] or self.keys[pg.K_LALT]) and self.keys[pg.K_RETURN]:
                    pg.display.toggle_fullscreen()
            self.screen.fill(self.color_background)
            self.loop(self.screen, frame)
            pg.display.flip()
            frame += 1
        self.quit()
        pg.quit()
    def loop(self, screen, frame):
        raise NotImplementedError('override loop method')
    def quit(self):
        pass  # override to shutdown

import random

class Star():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random.randint(0, self.width)
        self.y = random.randint(0, self.height)
        self.speed = random.randint(1,8)
    def __repr__(self):
        return f'Star({self.x}, {self.y})'
    def move(self):
        self.x += self.speed
        if self.x > self.width:
            self.x = 0
            self.y = random.randint(0, self.height)

class Game(GameBase):
    def __init__(self):
        self.stars = [Star(320, 180) for i in range(200)]
        super().__init__()
    def loop(self, screen, frame):
        for star in self.stars:
            pg.draw.rect(screen, (255,255,255), (star.x, star.y, 1, 1))
            star.move()


if __name__ == '__main__':
    Game().run()
