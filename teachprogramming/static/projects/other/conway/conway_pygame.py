import pygame

import sys
filename = sys.argv[1] if len(sys.argv) == 2 else 'conway.txt'

from conway_2 import ConwayFactory
conway = ConwayFactory.conway_from_file(filename)


class Variables():
    running = True
    paused = True
    color_background = (0, 0, 0)
    color_cell_alive = (255, 255, 255)
    view_x = 0
    view_y = 0
    move = 4
v = Variables()


if __name__ == "__main__":
    pygame.init()
    RESOLUTION = (640, 480)
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_mode(RESOLUTION, 0, 16)
    clock  = pygame.time.Clock()


    while v.running:
        clock.tick(60)
        screen.fill(v.color_background)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                v.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    v.paused = not v.paused

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            v.running = False

        if keys[pygame.K_UP   ]: v.view_y += -v.move
        if keys[pygame.K_DOWN ]: v.view_y +=  v.move
        if keys[pygame.K_LEFT ]: v.view_x += -v.move
        if keys[pygame.K_RIGHT]: v.view_x +=  v.move

        for i in conway._state:
            x, y = i
            screen.set_at((x-v.view_x, y-v.view_y), v.color_cell_alive)

        pygame.display.flip()

        if not v.paused:
            conway.next()

    pygame.quit()
