import pygame
from animation_base_pygame import PygameBase

class CopterGame(PygameBase):
    def __init__(self):
        self.background_color = (0, 0, 255, 255)
        self.background_image = pygame.image.load("images/FishLevel1.gif")
        self.copter_image     = pygame.image.load("images/fish.gif")
        self.reset()
        super().__init__()
    def reset(self):
        self.background_x_pos = 0
        self.copter_x_pos = 50
        self.copter_y_pos = 100
    def loop(self, screen, frame):

        self.background_x_pos += 1
        if self.keys[pygame.K_SPACE]: 
            self.copter_y_pos += -2
        else: 
            self.copter_y_pos +=  1

        collision_point = (self.copter_x_pos + self.background_x_pos, self.copter_y_pos)
        try   : pixel = self.background_image.get_at(collision_point)
        except: pixel = None
        if pixel and pixel != (255,255,255,255):
            self.reset()

        pygame.draw.rect(screen, self.background_color, (0,0)+screen.get_size())
        screen.blit(self.background_image, (-self.background_x_pos, 0))
        screen.blit(self.copter_image, (self.copter_x_pos, self.copter_y_pos))

if __name__ == '__main__':
    CopterGame().run()