import pygame
import random

#----------------------------------------
# Pygame Setup
#----------------------------------------
pygame.init()     
pygame.display.set_mode((640, 480))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

#----------------------------------------
# Constants
#----------------------------------------
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

max_size   = 30
num_blocks = 50

#----------------------------------------
# Class's
#----------------------------------------

class Mass:
    def __init__(self): #xpos, ypos, size
        self.xpos  = 0 #xpos
        self.ypos  = 0 #ypos
        self.size  = 0 #size
        self.x_vel = 0
        self.y_vel = 0
        self.size  = 0

#----------------------------------------
# Variables
#----------------------------------------

player = pygame.Rect(100,100,10,10)
blocks = [Mass() for i in range(num_blocks)]

time_elapsed = 0

#----------------------------------------
# Subroutines
#----------------------------------------

def reset():
    for i in range(len(blocks)):
        m = Mass()
        m.x_pos = random.random() * screen.get_width()
        m.y_pos = random.random() * screen.get_height()
        m.size  = random.randint(0,max_size) + 5
        blocks[i] = m
    time_elapsed = 0


#----------------------------------------
# Main Loop
#----------------------------------------

reset()
running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.MOUSEMOTION:
            player.x = event.pos[0]
            player.y = event.pos[1]
    
    screen.fill(black)
    
    for m in blocks:
        if m.x_pos<0 or m.x_pos > screen.get_width():
            m.x_vel=-(m.x_vel/3)
        if m.y_pos<0 or m.y_pos > screen.get_height():
            m.y_vel=-(m.y_vel/3)
        m.x_vel += -(m.x_pos-player.x)/m.size/500
        m.y_vel += -(m.y_pos-player.y)/m.size/500
        m.x_pos += m.x_vel
        m.y_pos += m.y_vel
        pygame.draw.rect(screen, yellow, pygame.Rect(m.x_pos, m.y_pos, m.size, m.size))

    if not screen.get_at((player.x,player.y)) == black:
        print("Score: %s" % time_elapsed)
        reset()
    
    pygame.draw.rect(screen, white, player)
    
    time_elapsed += 1
    
    pygame.display.update()
pygame.quit()