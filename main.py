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

# # Player and starting cord
# PlayerImg = pygame.image.load('player.png')
# playerX = 370
# playerY = 480
# # tracks where the player is moving
# player_x_change = 0
# tracks the last key pressed
# this is used so the controls are smother
last_key_down = 'none'

#  Background
background = pygame.image.load('background.png')



# bullet
bulletImg = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_change = 500
bullet_state = "ready"

#@score
score = 0

e = enemy.Enemy(random.randint(0, 735), 50)

def fire_bullet(x, y):
    global bullet_state
    global bullet_x
    bullet_state = "fire"
    bullet_x = x
    screen.blit(bulletImg, (x + 16, y + 10))


# draw the player
# def Player(x, y):
#     screen.blit(PlayerImg, (x, y))
p = player.Player()

# def enemy(x, y):
#     screen.blit(EnemyImg, (x, y))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


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
            # if event.key == pygame.K_SPACE and bullet_state == "ready":
            #     fire_bullet(playerX, playerY)

    # update player
    p.move(dt)
    # # bounds checking
    # if playerX < 0:
    #     playerX = 0
    # # 800 - 64 = 763
    # if playerX > 736:
    #     playerX = 736
    # set screen


    screen.fill((0, 0, 0))
    # Background
    screen.blit(background, (0, 0))
    p.draw(screen)
    # if bullet_state == "fire":
    #     bullet_y = bullet_y - (bullet_change * dt)
    #     if bullet_y < 0:
    #         bullet_y = 480
    #         bullet_state = "ready"
    #     else:
    #         fire_bullet(bullet_x, bullet_y)

    e.move(dt)
    e.draw(screen)
    # Collision
    # collision = is_collision(EnemyX, EnemyY, bullet_x, bullet_y)
    # if collision:
    #     bullet_y = 480
    #     bullet_state = "ready"
    #     score += 1
    #     EnemyX = random.randint(0, 735)
    #     EnemyY = 50

    pygame.display.update()
