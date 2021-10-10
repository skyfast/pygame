import pygame
import random
import time
import math

import enemy
import player

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
# Icons made by https://www.flaticon.com/authors/smashicons from www.flaticon.com
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# tracks the last key pressed
# this is used so the controls are smother
last_key_down = 'none'

#  Background
background = pygame.image.load('background.png')


# @score
score = 0

e = enemy.Enemy(random.randint(0, 735), 50)
p = player.Player()


dt = 0
prev_time = time.time()
# game loop
running = True
while running:
    now = time.time()
    dt = now - prev_time
    prev_time = now
    # check all game events
    for event in pygame.event.get():
        # quits the game
        if event.type == pygame.QUIT:
            running = False

        # check to see if the current key is released
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT and last_key_down == 'left') or (event.key == pygame.K_RIGHT and
                                                                            last_key_down == 'right'):
                p.moving = "none"
        # checks to see if there was a key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p.moving = "left"
                last_key_down = 'left'
            if event.key == pygame.K_RIGHT:
                p.moving = "right"
                last_key_down = 'right'
            if event.key == pygame.K_SPACE:
                p.shoot()

    screen.fill((0, 0, 0))
    # Background
    screen.blit(background, (0, 0))
    p.move(dt)
    e.move(dt)
    if p.check_hit(e.x_cord, e.y_cord):
        e.x_cord = random.randint(0, 735)
        e.y_cord = 50

    p.draw(screen)
    e.draw(screen)

    pygame.display.update()
