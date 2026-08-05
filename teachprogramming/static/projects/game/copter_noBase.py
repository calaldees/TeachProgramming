import pygame

pygame.init()
screen = pygame.display.set_mode((640,360), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()

background_image = pygame.image.load("images/CopterLevel1.png")                 # VER: background
background_x_pos = 0                                                            # VER: background
copter_image     = pygame.image.load("images/ship.gif")                         # VER: copter
copter_x_pos = 50                                                               # VER: copter
copter_y_pos = 100                                                              # VER: copter
copter_x_vel = 0                                                                # VER: physics
copter_y_vel = 0                                                                # VER: physics
                                                                                # VER: background
def safe_get_background_pixel(point):                                           # VER: collision_single
    try   : return background_image.get_at(point)                               # VER: collision_single
    except: return (0,0,0,0)                                                    # VER: collision_single
                                                                                # VER: collision_single
while True:
    pygame.display.update()
    clock.tick(60)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: break
                                                                                # VER: copter
    #if keys[pygame.K_SPACE]: copter_y_pos += -2                                 # VER: copter NOT physics
    #else                   : copter_y_pos +=  1                                 # VER: copter NOT physics
    if keys[pygame.K_UP   ]: copter_y_vel += -0.1                               # VER: physics
    if keys[pygame.K_DOWN ]: copter_y_vel +=  0.1                               # VER: physics
    if keys[pygame.K_LEFT ]: copter_x_vel += -0.1                               # VER: physics
    if keys[pygame.K_RIGHT]: copter_x_vel +=  0.1                               # VER: physics
    copter_x_vel  = copter_x_vel * 0.99                                         # VER: physics
    copter_y_vel  = copter_y_vel * 0.99                                         # VER: physics
    copter_y_vel += float(0.025)                                                # VER: physics
    copter_x_pos += copter_x_vel                                                # VER: physics
    copter_y_pos += copter_y_vel                                                # VER: physics
                                                                                # VER: background
    background_x_pos += 1                                                       # VER: background
    point = (background_x_pos + int(copter_x_pos), int(copter_y_pos))           # VER: collision_single
    r,g,b,a = safe_get_background_pixel(point)                                  # VER: collision_single
    if a > 128:                                                                 # VER: collision_single
        background_x_pos = 0                                                    # VER: collision_single
        copter_x_pos = 50                                                       # VER: collision_single
        copter_y_pos = 100                                                      # VER: collision_single

    screen.fill('black')
    screen.blit(background_image, (-background_x_pos, 0))                       # VER: background
    screen.blit(copter_image, (copter_x_pos, copter_y_pos))                     # VER: copter
