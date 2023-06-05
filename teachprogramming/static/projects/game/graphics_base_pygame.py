import pygame

class GameBase():
    def __init__(self, title="pg", resolution=(320,180), fps=60, color_background='black'):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(resolution, pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.color_background = color_background
    def run(self):
        frame = 0
        self.running = True
        while self.running:
            self.clock.tick(self.fps)
            self.keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                    self.running = False
                if event.type == pygame.VIDEORESIZE:
                    pygame.display._resize_event(event)
                if (self.keys[pygame.K_RALT] or self.keys[pygame.K_LALT]) and self.keys[pygame.K_RETURN]:
                    pygame.display.toggle_fullscreen()
            self.screen.fill(self.color_background)
            self.loop(self.screen, frame)
            pygame.display.flip()
            frame += 1
        self.quit()
        pygame.quit()
    def loop(self, screen, frame):
        raise NotImplementedError('override loop method')
    def quit(self):
        pass  # override to shutdown

class Game(GameBase):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.image = pygame.image.load('images/block.gif')
        super().__init__()
    def loop(self, screen, frame):
        s = screen
        width, height = s.get_size()

        t = frame % width
        pygame.draw.rect(s, pygame.Color("#f0b000"), (t, 10, 120, 80))

        t = frame % height
        pygame.draw.line(s, pygame.Color("red"), (t, t), (t+10, t+10), 5)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        s.blit(self.image, (mouse_x, mouse_y))

        if self.keys[pygame.K_UP]:
            self.y += -1
        if self.keys[pygame.K_DOWN]:
            self.y += 1
        if self.keys[pygame.K_RIGHT]:
            self.x += 1
        if self.keys[pygame.K_LEFT]:
            self.x += -1
        s.blit(self.image, (self.x, self.y))


        # Task DVD menu
        # 1.) Square edged red rectangle - 50 50
        # 2.) It moves automatically (in the x direction only)
        # 3.) It bounces left and right from the edges of the screen
        # 4.) DVD screensaver - bounces of top bottom left right
        # 5.) Make the rectangle an image
        # 6.) Remove any hard coded values for width/height/imagesize/etc

if __name__ == '__main__':
    Game().run()
