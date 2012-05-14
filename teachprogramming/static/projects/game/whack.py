import pygame
import random

# Setup
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

black = (0, 0, 0)

# Variables
ball_image = pygame.image.load("ball.png")
ball_rect  = ball_image.get_rect()

time_elapsed = 0
score        = 0

def reset():
    screen.fill(black)
    screen.blit(ball_image, ball_rect)
    pygame.display.update()

# Main
reset()
running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if ball_rect.collidepoint(event.pos):
                ball_rect.x = random.randint(0,screen.get_width() )
                ball_rect.y = random.randint(0,screen.get_height())
                score += 1
                reset()
    
    if score >= 10:
        print(time_elapsed)
        running = False
    
    time_elapsed += 1
    
pygame.quit()