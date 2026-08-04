import pygame

pygame.init()
screen = pygame.display.set_mode((480,270), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()

# Load images
image = pygame.image.load('images/block.gif')

# Setup variables (state)
x = 0
y = 0

while True:
    # Timing and events - pygame/system/boilerplate
    pygame.display.update()
    clock.tick(60)
    pygame.event.get()
    keys = pygame.key.get_pressed()

    # Update model/state/variables
    if keys[pygame.K_ESCAPE]:
        break
    if keys[pygame.K_RIGHT]:
        x = x + 1

    # Draw
    screen.fill('black')
    pygame.draw.rect(screen, 'yellow', (100, 100, 10, 10))

    screen.blit(image, (x+100, 100))