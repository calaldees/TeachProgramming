import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock  = pygame.time.Clock()

class callByRef:
    def __init__(self, **args):
        for (key, value) in args.items():
            setattr(self, key, value)
variables = callByRef(
    running           = True,
    background_colour = (  0,   0,   0, 255),
    player1_color     = (255, 255,   0     ), # Ver: 2
    player1_x_pos     = None,                 # Ver: 2
    player1_y_pos     = None,                 # Ver: 2
    player1_x_move    = None,                 # Ver: 2
    player1_y_move    = None,                 # Ver: 2
    player2_color     = (255,   0,   0     ), # Ver: 5
    player2_x_pos     = None,                 # Ver: 5
    player2_y_pos     = None,                 # Ver: 5
    player2_x_move    = None,                 # Ver: 5
    player2_y_move    = None,                 # Ver: 5
    player1_score     = 0, # Ver: 6
    player2_score     = 0, # Ver: 6
)

def reset():
    pygame.draw.rect(screen, variables.background_colour, pygame.Rect(0, 0, screen.get_width(), screen.get_height()))
    variables.player1_x_pos    = 100 # Ver: 2
    variables.player1_y_pos    = 100 # Ver: 2
    variables.player1_x_move   =   1 # Ver: 2
    variables.player1_y_move   =   0 # Ver: 2
    variables.player2_x_pos    = screen.get_width()  - 100 # Ver: 5
    variables.player2_y_pos    = screen.get_height() - 100 # Ver: 5
    variables.player2_x_move   =  -1                       # Ver: 5
    variables.player2_y_move   =   0                       # Ver: 5

reset()
while variables.running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            variables.running = False
            
    keys = pygame.key.get_pressed()   # Ver: 3
    if keys[pygame.K_UP    ]:         # Ver: 3
        variables.player1_x_move =  0 # Ver: 3
        variables.player1_y_move = -1 # Ver: 3
    if keys[pygame.K_RIGHT ]:         # Ver: 3
        variables.player1_x_move =  1 # Ver: 3 hidden
        variables.player1_y_move =  0 # Ver: 3 hidden
    if keys[pygame.K_LEFT  ]:         # Ver: 3 hidden
        variables.player1_x_move = -1 # Ver: 3 hidden
        variables.player1_y_move =  0 # Ver: 3 hidden
    if keys[pygame.K_DOWN  ]:         # Ver: 3 hidden
        variables.player1_x_move =  0 # Ver: 3 hidden
        variables.player1_y_move =  1 # Ver: 3 hidden
                                      # Ver: 5
    if keys[pygame.K_w     ]:         # Ver: 5 
        variables.player2_x_move =  0 # Ver: 5
        variables.player2_y_move = -1 # Ver: 5
    if keys[pygame.K_d     ]:         # Ver: 5
        variables.player2_x_move =  1 # Ver: 5 hidden
        variables.player2_y_move =  0 # Ver: 5 hidden
    if keys[pygame.K_a     ]:         # Ver: 5 hidden
        variables.player2_x_move = -1 # Ver: 5 hidden
        variables.player2_y_move =  0 # Ver: 5 hidden
    if keys[pygame.K_s     ]:         # Ver: 5 hidden
        variables.player2_x_move =  0 # Ver: 5 hidden
        variables.player2_y_move =  1 # Ver: 5 hidden
                                      # Ver: 5
    if keys[pygame.K_ESCAPE]:         # Ver: 3
        variables.running = False     # Ver: 3
                                      # Ver: 3
    variables.player1_x_pos = variables.player1_x_pos + variables.player1_x_move # Ver: 2
    variables.player1_y_pos = variables.player1_y_pos + variables.player1_y_move # Ver: 2
                                                                                 # Ver: 2
    variables.player2_x_pos = variables.player2_x_pos + variables.player2_x_move # Ver: 5
    variables.player2_y_pos = variables.player2_y_pos + variables.player2_y_move # Ver: 5
                                                                                 # Ver: 5
    try   : player1_at_pixel = screen.get_at((variables.player1_x_pos, variables.player1_y_pos)) # Ver: 4
    except: player1_at_pixel = None                                                              # Ver: 4
    if player1_at_pixel != variables.background_colour:                                          # Ver: 4
        variables.player2_score = variables.player2_score + 1                                    # Ver: 6
        reset()                                                                                  # Ver: 4
                                                                                                 # Ver: 4
    try   : player2_at_pixel = screen.get_at((variables.player2_x_pos, variables.player2_y_pos)) # Ver: 5
    except: player2_at_pixel = None                                                              # Ver: 5
    if player2_at_pixel != variables.background_colour:                                          # Ver: 5
        variables.player1_score = variables.player1_score + 1                                    # Ver: 6
        reset()                                                                                  # Ver: 5
                                                                                                 # Ver: 5
    screen.set_at((variables.player1_x_pos, variables.player1_y_pos), variables.player1_color) # Ver: 2
    screen.set_at((variables.player2_x_pos, variables.player2_y_pos), variables.player2_color) # Ver: 5
                                                                                               # Ver: 2
    if variables.player1_score == 5 or variables.player2_score == 5: # Ver: 6
        variables.running = False                                    # Ver: 6
                                                                     # Ver: 6
    pygame.display.flip()


pygame.quit()
                               # Ver: 6
print("Player 1 Score")        # Ver: 6
print(variables.player1_score) # Ver: 6
print("Player 2 Score")        # Ver: 6
print(variables.player2_score) # Ver: 6