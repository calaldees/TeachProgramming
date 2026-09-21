# CAUTION: python noBase is problematic because                                 # VER: warning
#  !! functions cannot use assignment `=` operator on global variables !!       # VER: warning
                                                                                # VER: warning
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640,360), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()

background_image = pygame.image.load("images/CopterLevel1.png")                 # VER: background
background_x_pos = 0                                                            # VER: background
copter_image     = pygame.image.load("images/ship.gif")                         # VER: copter
copter_x_pos = 50                                                               # VER: copter
copter_y_pos = 100                                                              # VER: copter
copter_x_vel = 0                                                                # VER: physics
copter_y_vel = 0                                                                # VER: physics physics_flap OR_
                                                                                # VER: background
# def rotate_image_center(img, x, y, angle):                                      # VER: rotate
#     rotated_image = pygame.transform.rotate(img, angle)                         # VER: rotate
#     rotated_rect = rotated_image.get_rect()                                     # VER: rotate
#     rotate_offset_x = (rotated_rect.width-img.width)//2                         # VER: rotate
#     rotate_offset_y = (rotated_rect.height-img.height)//2                       # VER: rotate
#     rotated_rect.center = (img.width//2, img.height//2)                         # VER: rotate
#     rotated_rect.x = x - rotate_offset_x                                        # VER: rotate
#     rotated_rect.y = y - rotate_offset_y                                        # VER: rotate
#     return (rotated_image, rotated_rect)                                        # VER: rotate
#                                                                                 # VER: rotate
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
    #if keys[pygame.K_SPACE]: copter_y_vel = -2                                  # VER: physics_flap NOT physics
    if keys[pygame.K_UP   ]: copter_y_vel += -0.1                               # VER: physics
    if keys[pygame.K_DOWN ]: copter_y_vel +=  0.1                               # VER: physics
    if keys[pygame.K_LEFT ]: copter_x_vel += -0.1                               # VER: physics
    if keys[pygame.K_RIGHT]: copter_x_vel +=  0.1                               # VER: physics
    copter_x_vel  = copter_x_vel * 0.99                                         # VER: physics
    copter_y_vel  = copter_y_vel * 0.99                                         # VER: physics
    copter_y_vel += 0.025                                                       # VER: physics physics_flap OR_
    copter_x_pos += copter_x_vel                                                # VER: physics
    copter_y_pos += copter_y_vel                                                # VER: physics physics_flap OR_
                                                                                # VER: background
    background_x_pos += 1                                                       # VER: background
    point = (background_x_pos + int(copter_x_pos), int(copter_y_pos))           # VER: collision_single
    r,g,b,a = safe_get_background_pixel(point)                                  # VER: collision_single
    if a > 128:                                                                 # VER: collision_single
        background_x_pos = 0                                                    # VER: collision_single
        copter_x_pos = 50                                                       # VER: collision_single
        copter_y_pos = 100                                                      # VER: collision_single
        copter_y_vel = 0                                                        # VER: physics

    screen.fill('black')
    screen.blit(background_image, (-background_x_pos, 0))                       # VER: background
    screen.blit(copter_image, (copter_x_pos, copter_y_pos))                     # VER: copter
    #screen.blit(*rotate_image_center(copter_image, copter_x_pos, copter_y_pos, copter_y_vel*-20))  # VER: rotate

pygame.quit()  # fix for `Idle` on windows to kill subprocess
sys.exit()
