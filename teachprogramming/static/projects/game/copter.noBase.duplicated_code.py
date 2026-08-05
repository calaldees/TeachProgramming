import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640,360), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 36)

level = 1

background_image = pygame.image.load(f"background{level}.png")
background_x_pos = 0

def reset():
    global background_image
    global background_x_pos
    background_image = pygame.image.load(f"background{level}.png")
    background_x_pos = 0
    #copter_x_pos = 100
    #copter_y_pos = 100

while True:
    pygame.display.update()
    clock.tick(60)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: break

    background_x_pos += 1
    print(background_x_pos)
    if background_x_pos > 500:
        level = level + 1
        if level >= 3:
            print("You completed my game")
            break
        reset()

    # if COLIDE:
    #    ....

    screen.fill('black')
    screen.blit(background_image, (-background_x_pos, 0))
    text_surface = font.render('Hello world', antialias=False, color=(255, 255, 255))
    screen.blit(text_surface, dest=(50,50))

pygame.quit()
sys.exit()
