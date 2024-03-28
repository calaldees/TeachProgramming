import pygame

from animation_base_pygame import PygameBase

class SpriteDemo(PygameBase):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.size = 50
        # https://www.nicepng.com/maxp/u2w7e6i1u2w7w7q8/
        # 
        self.sprites = pygame.image.load("222-2222069_megaman-sprite-png.png")
        self.anim = [
            self.sprites.subsurface((100, 196, 50, 50)),
            self.sprites.subsurface((150, 196, 50, 50)),
            self.sprites.subsurface((200, 196, 50, 50)),
            self.sprites.subsurface((250, 196, 50, 50)),
        ]
        super().__init__()
    def loop(self, screen, frame):
        width, height = screen.get_size()

        if self.keys[pygame.K_UP]:
            self.y += -1
        if self.keys[pygame.K_DOWN]:
            self.y += 1
        #??? Left and Right
        #??? can you use a key to make the square bigger or smaller?
        if self.keys[pygame.K_SPACE]:
            self.size += 1

        animation_frame = (frame // 10) % len(self.anim)
        screen.blit(self.anim[animation_frame], (self.x, self.y)) ##
        #screen.blit(self.sprites, (0,0))
        #pygame.draw.rect(screen, pygame.Color("red"), (self.x, self.y, self.size, self.size))


try:                      
    SpriteDemo().run()
except:                   
    import traceback      
    traceback.print_exc() 
    pygame.quit()         
