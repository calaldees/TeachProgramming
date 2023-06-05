#!/usr/bin/env python
import pygame

#--Initalize and Setup--
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock  = pygame.time.Clock()
pygame.key.set_repeat(True)
running = True

#--VARIABLES--
background_color = 0, 0, 0
ball_image = pygame.image.load("images/block.gif")
ball_rect  = ball_image.get_rect()

def timerEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT   : stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP     : ball_rect.y += -1
            if event.key == pygame.K_DOWN   : ball_rect.y +=  1
            if event.key == pygame.K_RIGHT  : ball_rect.x +=  1
            if event.key == pygame.K_LEFT   : ball_rect.x += -1
            if event.key == pygame.K_ESCAPE : stop()
    screen.fill(background_color)
    screen.blit(ball_image, ball_rect)
    pygame.display.flip()

def stop():
    global running
    running = False
    
#--MAIN--
while running:
    clock.tick(60)
    timerEvent()
pygame.quit()