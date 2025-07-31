import pygame
from animation_base_pygame import PygameBase
import pathlib   # VER: parallax

class CopterGame(PygameBase):
    def __init__(self):
        #self.background_image = pygame.image.load("images/CopterLevel1.gif")  # VER: background NOT parallax
        self.background_color = (0, 0, 0, 0)
        self.copter_image     = pygame.image.load("images/ship.gif")         # VER: copter
        self.copter_collision_points = ((0,0),(32,9),(17,2),(22,12),(2,12))  # VER: collision_multi
        self.level_color = (255, 255, 0, 255)                                # VER: level
        self.level_number = 1                                                # VER: level
        self.load_level()                                                    # VER: level
        #self.reset()                                                         # VER: level NOT_
        super().__init__(resolution=(640,360))
    def load_level(self):                                                                         # VER: level
        #self.background_image = pygame.image.load(f"images/CopterLevel{self.level_number}.gif")  # VER: level NOT parallax
        self.background_images = [                                                               # VER: parallax
            pygame.image.load(file)                                                              # VER: parallax
            for file in sorted(pathlib.Path('images').glob(f"*CopterLevel{self.level_number}*.png")) # VER: parallax
        ]                                                                                        # VER: parallax
        self.reset()                                                                             # VER: level
    def reset(self):
        #pass                      # VER: background NOT_
        self.background_x_pos = 0  # VER: background
        self.copter_x_pos = 50     # VER: copter
        self.copter_y_pos = 100    # VER: copter
        self.copter_x_vel = 0  # VER: physics
        self.copter_y_vel = 0  # VER: physics
    def loop(self, screen, frame):
        self.background_x_pos += 1   # VER: background
                                     # VER: background
        #if self.keys[pygame.K_SPACE]: self.copter_y_pos += -2  # VER: copter NOT physics
        #else                        : self.copter_y_pos +=  1  # VER: copter NOT physics
        if self.keys[pygame.K_UP   ]: self.copter_y_vel += -0.1 # VER: physics
        if self.keys[pygame.K_DOWN ]: self.copter_y_vel +=  0.1 # VER: physics
        if self.keys[pygame.K_LEFT ]: self.copter_x_vel += -0.1 # VER: physics HIDE
        if self.keys[pygame.K_RIGHT]: self.copter_x_vel +=  0.1 # VER: physics HIDE
                                                                # VER: copter
        self.copter_x_vel  = self.copter_x_vel * 0.99  # VER: physics
        self.copter_y_vel  = self.copter_y_vel * 0.99  # VER: physics
        self.copter_y_vel += float(0.025)              # VER: physics
        self.copter_x_pos += self.copter_x_vel         # VER: physics
        self.copter_y_pos += self.copter_y_vel         # VER: physics
                                                       # VER: physics
        def safe_get_pixel(p):                                   # VER: collision_single
            #try   : return self.background_image.get_at(p)   # VER: collision_single NOT parallax
            try   : return self.background_images[0].get_at(p)   # VER: parallax
            except: return (0,0,0,0)                             # VER: collision_single
        #if True:                                   # VER: collision_single NOT collision_multi
        for x, y in self.copter_collision_points:   # VER: collision_multi
            #point = (self.background_x_pos + int(self.copter_x_pos), int(self.copter_y_pos))  # VER: collision_single NOT collision_multi
            point = (self.background_x_pos + int(self.copter_x_pos) + x, int(self.copter_y_pos) + y)  # VER: collision_multi
            pixel = safe_get_pixel(point)           # VER: collision_single
            r,g,b,a = pixel                         # VER: collision_single
            if a < 10:                              # VER: collision_single
                pass                                # VER: collision_single
            elif pixel == self.level_color:         # VER: level
                self.level_number += 1              # VER: level
                self.load_level()                   # VER: level
            else:                                   # VER: collision_single
                self.reset()                        # VER: collision_single
                                                    # VER: collision_single
        pygame.draw.rect(screen, self.background_color, (0,0)+screen.get_size())
        #screen.blit(self.background_image, (-self.background_x_pos, 0))          # VER: background NOT parallax
        for parallax_number, background_image in sorted(enumerate(self.background_images), reverse=True): # VER: parallax
            screen.blit(background_image, (-self.background_x_pos/2**parallax_number, 0))                # VER: parallax
                                                                                 # VER: copter
        screen.blit(self.copter_image, (self.copter_x_pos, self.copter_y_pos))    # VER: copter

if __name__ == '__main__':
    CopterGame().run()