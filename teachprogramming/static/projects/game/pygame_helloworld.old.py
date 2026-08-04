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
    color_background  = (  0,   0,   0, 255),
)

while v.running:
    clock.tick(60)
    screen.fill(v.color_background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: v.running = False

    pygame.display.flip()

pygame.quit()