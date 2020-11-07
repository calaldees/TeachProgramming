import pygame as pg

class GameBase():
    def __init__(self, title="pg", resolution=(320,180), fps=60, color_background='black'):
        pg.init()
        pg.display.set_caption(title)
        screen = pg.display.set_mode(resolution, pg.SCALED | pg.RESIZABLE)
        clock = pg.time.Clock()
        frame = 0
        self.running = True
        while self.running:
            screen.fill(color_background)
            self.keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                    self.running = False
                if event.type == pg.VIDEORESIZE:
                    pg.display._resize_event(event)
                if (self.keys[pg.K_RALT] or self.keys[pg.K_LALT]) and self.keys[pg.K_RETURN]:
                    pg.display.toggle_fullscreen()
            clock.tick(fps)
            self.loop(screen, frame)
            pg.display.flip()
            frame += 1
        pg.quit()

    def loop(self, screen, frame):
        raise NotImplementedError('override loop method')

class Game(GameBase):
    def __init__(self):
        self.x = 100
        self.y = 100
        super().__init__()
    def loop(self, screen, frame):
        s = screen
        if self.keys[pg.K_UP]:
            self.y += -1
        if self.keys[pg.K_DOWN]:
            self.y += 1
        if self.keys[pg.K_RIGHT]:
            self.x += 1
        if self.keys[pg.K_LEFT]:
            self.x += -1
        pg.draw.rect(s, 'green', (self.x, self.y, 70, 40), 2, border_radius=15)

if __name__ == '__main__':
    Game()
