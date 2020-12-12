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

class Game(GameBase):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.image = pg.image.load('ball.png')
        super().__init__()
    def loop(self, screen, frame):
        if self.keys[pg.K_UP]:
            self.y += -1
        if self.keys[pg.K_DOWN]:
            self.y += 1
        if self.keys[pg.K_RIGHT]:
            self.x += 1
        if self.keys[pg.K_LEFT]:
            self.x += -1

        #pg.draw.rect(screen, 'green', (self.x, self.y, 70, 40), 2, border_radius=15)
        screen.blit(self.image, (self.x, self.y))


        # Task DVD menu
        # 1.) Square edged red rectangle - 50 50
        # 2.) It moves automatically (in the x direction only)
        # 3.) It bounces left and right from the edges of the screen
        # 4.) DVD screensaver - bounces of top bottom left right
        # 5.) Make the rectangle an image
        # 6.) Remove any hard coded values for width/height/imagesize/etc

if __name__ == '__main__':
    Game().run()
