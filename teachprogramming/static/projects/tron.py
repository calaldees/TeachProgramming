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
    color_exit        = (255,   0,   0, 255), # VER: maze
    level_number      = 1,                    # Ver: maze
    player1_color     = (255, 255,   0     ), # Ver: line
    player1_x_pos     = None,                 # Ver: line
    player1_y_pos     = None,                 # Ver: line
    player1_x_move    = None,                 # Ver: line
    player1_y_move    = None,                 # Ver: line
    player2_color     = (255,   0,   0     ), # Ver: player2
    player2_x_pos     = None,                 # Ver: player2
    player2_y_pos     = None,                 # Ver: player2
    player2_x_move    = None,                 # Ver: player2
    player2_y_move    = None,                 # Ver: player2
    player1_score     = 0,                    # Ver: score
    player2_score     = 0,                    # Ver: score
)

def reset():
    pygame.draw.rect(screen, variables.background_colour, pygame.Rect(0, 0, screen.get_width(), screen.get_height()))
    #level_image = pygame.image.load("MazeLevel%d.gif" % level_number) # VER: maze
    #screen.blit(level_image, level_image.get_rect())                  # VER: maze
    variables.player1_x_pos    = 100 # Ver: line
    variables.player1_y_pos    = 100 # Ver: line
    variables.player1_x_move   =   1 # Ver: line
    variables.player1_y_move   =   0 # Ver: line
    variables.player2_x_pos    = screen.get_width()  - 100 # Ver: player2
    variables.player2_y_pos    = screen.get_height() - 100 # Ver: player2
    variables.player2_x_move   =  -1                       # Ver: player2
    variables.player2_y_move   =   0                       # Ver: player2

reset()
while variables.running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            variables.running = False
    
    keys = pygame.key.get_pressed()   # Ver: input
    if keys[pygame.K_ESCAPE]:         # Ver: input
        variables.running = False     # Ver: input
                                      # Ver: input
    if keys[pygame.K_UP    ]:         # Ver: input
        variables.player1_x_move =  0 # Ver: input
        variables.player1_y_move = -1 # Ver: input
    if keys[pygame.K_RIGHT ]:         # Ver: input
        variables.player1_x_move =  1 # Ver: input HIDE
        variables.player1_y_move =  0 # Ver: input HIDE
    if keys[pygame.K_LEFT  ]:         # Ver: input HIDE
        variables.player1_x_move = -1 # Ver: input HIDE
        variables.player1_y_move =  0 # Ver: input HIDE
    if keys[pygame.K_DOWN  ]:         # Ver: input HIDE
        variables.player1_x_move =  0 # Ver: input HIDE
        variables.player1_y_move =  1 # Ver: input HIDE
                                      # Ver: player2
    if keys[pygame.K_w     ]:         # Ver: player2
        variables.player2_x_move =  0 # Ver: player2
        variables.player2_y_move = -1 # Ver: player2
    if keys[pygame.K_d     ]:         # Ver: player2
        variables.player2_x_move =  1 # Ver: player2 HIDE
        variables.player2_y_move =  0 # Ver: player2 HIDE
    if keys[pygame.K_a     ]:         # Ver: player2 HIDE
        variables.player2_x_move = -1 # Ver: player2 HIDE
        variables.player2_y_move =  0 # Ver: player2 HIDE
    if keys[pygame.K_s     ]:         # Ver: player2 HIDE
        variables.player2_x_move =  0 # Ver: player2 HIDE
        variables.player2_y_move =  1 # Ver: player2 HIDE
                                      # Ver: player2
    variables.player1_x_pos = variables.player1_x_pos + variables.player1_x_move # Ver: line
    variables.player1_y_pos = variables.player1_y_pos + variables.player1_y_move # Ver: line
                                                                                 # Ver: line
    variables.player2_x_pos = variables.player2_x_pos + variables.player2_x_move # Ver: player2
    variables.player2_y_pos = variables.player2_y_pos + variables.player2_y_move # Ver: player2 HIDE
                                                                                 # Ver: player2
    if variables.player1_x_pos<=0                  : variables.player1_x_pos = screen.get_width() -1 # VER: wrap
    if variables.player1_x_pos>=screen.get_width() : variables.player1_x_pos =                     1 # VER: wrap
    if variables.player1_y_pos<=0                  : variables.player1_y_pos = screen.get_height()-1 # VER: wrap HIDE
    if variables.player1_y_pos>=screen.get_height(): variables.player1_y_pos =                     1 # VER: wrap HIDE
    if variables.player2_x_pos<=0                  : variables.player2_x_pos = screen.get_width() -1 # VER: player2,wrap
    if variables.player2_x_pos>=screen.get_width() : variables.player2_x_pos =                     1 # VER: player2,wrap
    if variables.player2_y_pos<=0                  : variables.player2_y_pos = screen.get_height()-1 # VER: player2,wrap HIDE
    if variables.player2_y_pos>=screen.get_height(): variables.player2_y_pos =                     1 # VER: player2,wrap HIDE
                                                                                                     # VER: wrap
    try   : player1_at_pixel = screen.get_at((variables.player1_x_pos, variables.player1_y_pos)) # Ver: colide
    except: player1_at_pixel = None                                                              # Ver: colide
    if player1_at_pixel == variables.color_exit:                                                 # VER: maze
        variables.level_number += 1                                                              # VER: maze
    if player1_at_pixel != variables.background_colour:                                          # Ver: colide
        variables.player2_score = variables.player2_score + 1                                    # Ver: score
        reset()                                                                                  # Ver: colide
                                                                                                 # Ver: colide
    try   : player2_at_pixel = screen.get_at((variables.player2_x_pos, variables.player2_y_pos)) # Ver: player2
    except: player2_at_pixel = None                                                              # Ver: player2 HIDE
    if player2_at_pixel != variables.background_colour:                                          # Ver: player2
        variables.player1_score = variables.player1_score + 1                                    # Ver: score HIDE
        reset()                                                                                  # Ver: player2 HIDE
                                                                                                 # Ver: player2
    screen.set_at((variables.player1_x_pos, variables.player1_y_pos), variables.player1_color) # Ver: line
    screen.set_at((variables.player2_x_pos, variables.player2_y_pos), variables.player2_color) # Ver: player2 HIDE
                                                                                               # Ver: line
    if variables.player1_score == 5 or variables.player2_score == 5: # Ver: score
        variables.running = False                                    # Ver: score
                                                                     # Ver: score
    pygame.display.flip()

pygame.quit()
                               # Ver: score
print("Player 1 Score")        # Ver: score
print(variables.player1_score) # Ver: score
print("Player 2 Score")        # Ver: score
print(variables.player2_score) # Ver: score