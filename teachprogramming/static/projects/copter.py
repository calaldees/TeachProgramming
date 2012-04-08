import pygame
import math

pygame.init()
screen = pygame.display.set_mode((320, 240))
clock  = pygame.time.Clock()

class callByRef:
    def __init__(self, **args):
        for (key, value) in args.items():
            setattr(self, key, value)
variables = callByRef(
    running           = True,
    color_background  = (  0,   0,   0, 255),
    color_exit        = (255, 255,   0, 255), # VER: level
    level_number      = 1,
    background_images = None, # VER: background
    view_x_pos        = None, # VER: background
    copter_image      = pygame.image.load("ship.gif"), # VER: copter
    copter_x_pos      = None, # VER: copter
    copter_y_pos      = None, # VER: copter
    copter_x_vel      = None, # VER: physics
    copter_y_vel      = None, # VER: physics
    copter_colision_points = [(0,0),(32,9),(17,2),(22,12),(2,12)], # VER: colision
)

def load_level(level_number):                                                                                             # VER: background
    variables.background_images = []                                                                                      # VER: paralax
    for layer in reversed(range(1,4)):                                                                                    # VER: paralax
        try   : variables.background_images.append(pygame.image.load("CopterLevel%d_layer%s.gif" % (level_number,layer))) # VER: paralax
        except: pass                                                                                                      # VER: paralax
    variables.background_images.append(pygame.image.load("CopterLevel%d.gif" % level_number))                             # VER: background
                                                                                                                          # VER: background
def reset():
    #pass                                                  # VER: 1 not background
    variables.view_x_pos        = 0                        # VER: background
    variables.copter_x_pos      = 50.0                     # VER: copter
    variables.copter_y_pos      = screen.get_height()/2    # VER: copter
    variables.copter_x_vel      = 0.0                      # VER: physics
    variables.copter_y_vel      = 0.0                      # VER: physics

load_level(variables.level_number) # VER: background
reset()
while variables.running:
    clock.tick(60)
    screen.fill(variables.color_background)
    
    variables.view_x_pos += 1                                               # VER: background
    #background_rectangle   = background_images[-1].get_rect()              # VER: background not paralax
    #background_rectangle.x = background_rectangle.x - variables.view_x_pos # VER: background not paralax
    #screen.blit(background_image, background_rectangle)                    # VER: background not paralax
    paralax_number = 1                                                      # VER: paralax
    for background_image in variables.background_images:                    # VER: paralax
        background_rectangle   = background_image.get_rect()                # VER: paralax
        background_rectangle.x = background_rectangle.x - int(variables.view_x_pos/math.pow(2,len(variables.background_images)-paralax_number)) # VER: paralax
        screen.blit(background_image, background_rectangle)                 # VER: paralax
        paralax_number += 1                                                 # VER: paralax
                                                                            # VER: background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            variables.running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE    ]:
        variables.running = False
    #if keys[pygame.K_SPACE ]: variables.copter_y_pos += -2  # VER: copter not physics
    #else                    : variables.copter_y_pos +=  1  # VER: copter not physics
    if keys[pygame.K_UP    ]: variables.copter_y_vel += -0.1 # VER: physics
    if keys[pygame.K_DOWN  ]: variables.copter_y_vel +=  0.1 # VER: physics
    if keys[pygame.K_LEFT  ]: variables.copter_x_vel += -0.1 # VER: physics HIDE
    if keys[pygame.K_RIGHT ]: variables.copter_x_vel +=  0.1 # VER: physics HIDE
                                                             # VER: copter
    variables.copter_x_vel  = variables.copter_x_vel * 0.99  # VER: physics
    variables.copter_y_vel  = variables.copter_y_vel * 0.99  # VER: physics
    variables.copter_y_vel += float(0.025)                   # VER: physics
    variables.copter_x_pos += variables.copter_x_vel         # VER: physics
    variables.copter_y_pos += variables.copter_y_vel         # VER: physics
                                                             # VER: physics
    copter_pos = (int(variables.copter_x_pos+variables.view_x_pos), int(variables.copter_y_pos)) # VER: colision
    for colision_point in variables.copter_colision_points:                                      # VER: colision
        colision_point = (copter_pos[0]+colision_point[0], copter_pos[1]+colision_point[1])      # VER: colision
        try   : pixel = variables.background_images[-1].get_at(colision_point)                   # VER: colision
        except: pixel = None                                                                     # VER: colision
        if pixel and pixel == variables.color_exit:                                              # VER: level
            variables.level_number += 1                                                          # VER: level
            load_level(variables.level_number)                                                   # VER: level
        if pixel and pixel != (255,255,255,255):                                                 # VER: colision
            reset()                                                                              # VER: colision
                                                                                                 # VER: colision
    copter_rectangle = variables.copter_image.get_rect()  # VER: copter
    copter_rectangle.x = int(variables.copter_x_pos)      # VER: copter
    copter_rectangle.y = int(variables.copter_y_pos)      # VER: copter
    screen.blit(variables.copter_image, copter_rectangle) # VER: copter
                                                          # VER: copter
    pygame.display.flip()

pygame.quit()