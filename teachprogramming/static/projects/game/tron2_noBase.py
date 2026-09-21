import pygame

pygame.init()
screen = pygame.display.set_mode((480,270), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()

DIRECTION_RIGHT = 0     # VER: keys_direction
DIRECTION_LEFT = 1      # VER: keys_direction
DIRECTION_UP = 2        # VER: keys_direction
DIRECTION_DOWN = 3      # VER: keys_direction
                        # VER: keys_direction
# x = 50                       # VER: keys_move
# y = 50                       # VER: keys_move
# direction = DIRECTION_RIGHT  # VER: keys_direction
                               # VER: keys_move
while True:
    pygame.display.update()
    clock.tick(60)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

    # if keys[pygame.K_RIGHT]:   # VER: keys_move NOT keys_direction
        # x = x + 1              # VER: keys_move NOT keys_direction
    # if keys[pygame.K_LEFT]:    # VER: keys_move NOT keys_direction
        # x = x - 1              # VER: keys_move NOT keys_direction
    # if keys[pygame.K_UP]:      # VER: keys_move NOT keys_direction
        # y = y - 1              # VER: keys_move NOT keys_direction
    # if keys[pygame.K_DOWN]:    # VER: keys_move NOT keys_direction
        # y = y + 1              # VER: keys_move NOT keys_direction
                                 # VER: keys_move NOT keys_direction
    # if keys[pygame.K_RIGHT]:          # VER: keys_direction NOT keys_direction_protect
        # direction = DIRECTION_RIGHT   # VER: keys_direction NOT keys_direction_protect
    # if keys[pygame.K_LEFT]:           # VER: keys_direction NOT keys_direction_protect
        # direction = DIRECTION_LEFT    # VER: keys_direction NOT keys_direction_protect
    # if keys[pygame.K_UP]:             # VER: keys_direction NOT keys_direction_protect
        # direction = DIRECTION_UP      # VER: keys_direction NOT keys_direction_protect
    # if keys[pygame.K_DOWN]:           # VER: keys_direction NOT keys_direction_protect
        # direction = DIRECTION_DOWN    # VER: keys_direction NOT keys_direction_protect
                                        # VER: keys_direction NOT keys_direction_protect
    # if keys[pygame.K_RIGHT] and direction != DIRECTION_LEFT:  # VER: keys_direction_protect
    #     direction = DIRECTION_RIGHT                           # VER: keys_direction_protect
    # if keys[pygame.K_LEFT] and direction != DIRECTION_RIGHT:  # VER: keys_direction_protect
    #     direction = DIRECTION_LEFT                            # VER: keys_direction_protect
    # if keys[pygame.K_UP] and direction != DIRECTION_DOWN:     # VER: keys_direction_protect
    #     direction = DIRECTION_UP                              # VER: keys_direction_protect
    # if keys[pygame.K_DOWN] and direction != DIRECTION_UP:     # VER: keys_direction_protect
    #     direction = DIRECTION_DOWN                            # VER: keys_direction_protect
                                                                # VER: keys_direction_protect
    # if direction == DIRECTION_RIGHT:  # VER: keys_direction
        # x = x + 1                     # VER: keys_direction
    # if direction == DIRECTION_LEFT:   # VER: keys_direction
        # x = x - 1                     # VER: keys_direction
    # if direction == DIRECTION_UP:     # VER: keys_direction
        # y = y - 1                     # VER: keys_direction
    # if direction == DIRECTION_DOWN:   # VER: keys_direction
        # y = y + 1                     # VER: keys_direction
                                        # VER: keys_direction
    # pixel = screen.get_at((x, y))         # VER: collision
    # try:                                  # VER: collision
        # pixel = screen.get_at((x, y))     # VER: collision
    # except:                               # VER: collision
        # pixel = None                      # VER: collision
                                            # VER: collision
    # if pixel != pygame.Color('black'):    # VER: collision
        # screen.fill('black')              # VER: collision
        # x = 50                            # VER: collision
        # y = 50                            # VER: collision
        # direction = 2                     # VER: collision
                                            # VER: collision
    #pygame.draw.rect(screen, 'yellow', (x, y, 1, 1))   # VER: keys_move
