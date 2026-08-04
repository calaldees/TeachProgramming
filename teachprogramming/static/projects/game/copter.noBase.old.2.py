import pygame

pygame.init()
screen = pygame.display.set_mode((320,180), pygame.SCALED | pygame.RESIZABLE)
clock  = pygame.time.Clock()

class callByRef:
    def __init__(self, **args):
        for (key, value) in args.items():
            setattr(self, key, value)

v = callByRef(
    running = True,
    color_background = (0,0,0,255),
    background_image = pygame.image.load("redworld.gif"),
    view_x_pos = 0,
    player_image = pygame.image.load("nugget.gif"),
    player_x_pos = 50,
    player_y_pos = 50,
)

while v.running:
    clock.tick(60)
    screen.fill(v.color_background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: v.running = False

    if keys[pygame.K_SPACE]: v.player_y_pos += -2
    else                   : v.player_y_pos += 1
    
    colision_point = (v.player_x_pos + v.view_x_pos, v.player_y_pos)
    try   : pixel = v.background_image.get_at(colision_point)
    except: pixel = None
    if pixel and pixel != (85,255,255,255):
        v.view_x_pos = 0
        v.player_x_pos = 50
        v.player_y_pos = 50    

    v.view_x_pos += 1
    rectangle = v.background_image.get_rect()
    rectangle.x = rectangle.x - v.view_x_pos
    screen.blit(v.background_image, rectangle)

    player_rectangle = v.player_image.get_rect()
    player_rectangle.x = v.player_x_pos
    player_rectangle.y = v.player_y_pos
    screen.blit(v.player_image, player_rectangle)
    
    

    pygame.display.flip()

pygame.quit()
