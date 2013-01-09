import pygame

pygame.init()
screen = pygame.display.set_mode((320, 240))
clock  = pygame.time.Clock()

class callByRef:
    def __init__(self, **args):
        for (key, value) in args.items():
            setattr(self, key, value)
v = callByRef(
    running           = True,
    color_background  = ( 52,  24,   236, 255),
    background_image  = pygame.image.load("images/CopterSimpleLevel.gif"),
    view_x_pos        = 0,
    
    copter_image      = pygame.image.load("images/CopterSimpleCopter.gif"),
    copter_x_pos      =  50,
    copter_y_pos      = 100,
)

while v.running:
    clock.tick(60)
    screen.fill(v.color_background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: v.running = False
    
    if keys[pygame.K_SPACE ]: v.copter_y_pos += -2
    else                    : v.copter_y_pos +=  1
    
    colision_point = (v.copter_x_pos + v.view_x_pos, v.copter_y_pos)
    try   : pixel = v.background_image.get_at(colision_point)
    except: pixel = None
    if pixel and pixel != (255,255,255,255):
        v.view_x_pos   =   0
        v.copter_x_pos =  50
        v.copter_y_pos = 100

    v.view_x_pos += 1
    rectangle   = v.background_image.get_rect()
    rectangle.x = rectangle.x - v.view_x_pos
    screen.blit(v.background_image, rectangle)

    copter_rectangle = v.copter_image.get_rect()
    copter_rectangle.x = v.copter_x_pos
    copter_rectangle.y = v.copter_y_pos
    screen.blit(v.copter_image, copter_rectangle)

    pygame.display.flip()

pygame.quit()