import pygame

pygame.init()
screen  = pygame.display.set_mode((640, 480))
clock   = pygame.time.Clock()

class callByRef:
    def __init__(self, **args):
        for (key, value) in args.items():
            setattr(self, key, value)

variables = callByRef(
    running        = True,
    player1_x_pos  = 100,
    player1_y_pos  = 100,
    player1_x_move =   1,
    player1_y_move =   0,
    player1_color  = (0,255,255),
)

def timerEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT   : variables.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP     : variables.player1_x_move= 0 ; variables.player1_y_move=-1
            if event.key == pygame.K_DOWN   : variables.player1_x_move= 0 ; variables.player1_y_move= 1
            if event.key == pygame.K_RIGHT  : variables.player1_x_move= 1 ; variables.player1_y_move= 0
            if event.key == pygame.K_LEFT   : variables.player1_x_move=-1 ; variables.player1_y_move= 0
            if event.key == pygame.K_ESCAPE : variables.running = False
            
    variables.player1_x_pos = variables.player1_x_pos + variables.player1_x_move
    variables.player1_y_pos = variables.player1_y_pos + variables.player1_y_move
    screen.set_at((variables.player1_x_pos, variables.player1_y_pos), variables.player1_color)

    pygame.display.flip()

#--MAIN--
while variables.running:
    clock.tick(60)
    timerEvent()
pygame.quit()