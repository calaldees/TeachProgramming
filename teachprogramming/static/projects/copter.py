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
    background_colour = (  0,   0,   0, 255),
    level_number      = 1,
    copter_image      = pygame.image.load("ship.gif"),
    copter_colision_points = [(0,0),(32,9),(17,2),(22,12),(2,12)],
    background_images = None,
    view_x_pos        = None,
    copter_x_pos      = None,
    copter_y_pos      = None,
    copter_x_vel      = None,
    copter_y_vel      = None,
)

def reset():
    #pygame.draw.rect(screen, variables.background_colour, pygame.Rect(0, 0, screen.get_width(), screen.get_height()))
    variables.background_images = []
    variables.background_images.append(pygame.image.load("CopterLevel%d_bg2.png" % variables.level_number))
    variables.background_images.append(pygame.image.load("CopterLevel%d_bg1.png" % variables.level_number))
    variables.background_images.append(pygame.image.load("CopterLevel%d.png" % variables.level_number))    
    
    variables.view_x_pos       = 0
    
    variables.copter_x_pos      = 50.0
    variables.copter_y_pos      = 50.0
    variables.copter_x_vel      = 0.0
    variables.copter_y_vel      = 0.0

reset()
while variables.running:
    clock.tick(60)
    screen.fill(variables.background_colour)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            variables.running = False
    
    keys = pygame.key.get_pressed()   # Ver: 3
    if keys[pygame.K_ESCAPE    ]:
        variables.running = False
    if keys[pygame.K_UP    ]:         # Ver: 3
        variables.copter_y_vel += -0.1
    if keys[pygame.K_DOWN  ]:         
        variables.copter_y_vel +=  0.1
    if keys[pygame.K_LEFT  ]:
        variables.copter_x_vel += -0.1
    if keys[pygame.K_RIGHT ]:
        variables.copter_x_vel +=  0.1

    copter_rectangle = variables.copter_image.get_rect()

    variables.copter_x_vel  = variables.copter_x_vel * 0.99
    variables.copter_y_vel  = variables.copter_y_vel * 0.99
    variables.copter_y_vel += float(0.025)
    if (variables.copter_y_pos < 0 or variables.copter_y_pos > screen.get_height()-copter_rectangle.height):
        variables.copter_y_vel = -variables.copter_y_vel
    
    variables.copter_x_pos += variables.copter_x_vel
    variables.copter_y_pos += variables.copter_y_vel
    
    variables.view_x_pos += 1
    
    copter_pos = (int(variables.copter_x_pos+variables.view_x_pos), int(variables.copter_y_pos))
    for colision_point in variables.copter_colision_points:
        colision_point = (copter_pos[0]+colision_point[0], copter_pos[1]+colision_point[1])
        try   : pixel = variables.background_images[-1].get_at(colision_point)
        except: pixel = None
        if pixel and pixel[3] > 0:
            reset()
    
    paralax_number = 1
    for background_image in variables.background_images:
        background_rectangle   = background_image.get_rect()
        background_rectangle.x = background_rectangle.x - int(variables.view_x_pos/math.pow(2,len(variables.background_images)-paralax_number))
        screen.blit(background_image, background_rectangle)
        paralax_number += 1
    
    copter_rectangle.x = int(variables.copter_x_pos)
    copter_rectangle.y = int(variables.copter_y_pos)
    screen.blit(variables.copter_image, copter_rectangle)
    
    pygame.display.flip()

pygame.quit()