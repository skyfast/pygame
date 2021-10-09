import pygame
import random
import time

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
# Icons made by https://www.flaticon.com/authors/smashicons from www.flaticon.com
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Player and starting cord
PlayerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
# tracks where the player is moving
player_x_change = 0
# tracks the last key pressed
# this is used so the controls are smother
last_key_down = 'none'

#  Enemy and starting cord
EnemyImg = pygame.image.load('trash.png')
EnemyX = random.randint(0, 800)
EnemyY = 50

#  Background
background = pygame.image.load('background.png')

enemy_x_change = 400
enemy_y_change = 20

# bullet
bulletImg = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_change = 500
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    global bullet_x
    bullet_state = "fire"
    bullet_x = x
    screen.blit(bulletImg, (x + 16, y + 10))


# draw the player
def Player(x, y):
    screen.blit(PlayerImg, (x, y))


def enemy(x, y):
    screen.blit(EnemyImg, (x, y))


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
                player_x_change = 0
                last_key_down = 'none'
        # checks to see if there was a key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -400
                last_key_down = 'left'
            if event.key == pygame.K_RIGHT:
                player_x_change = 400
                last_key_down = 'right'
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                fire_bullet(playerX, playerY)

    # update player
    playerX += player_x_change * dt
    # bounds checking
    if playerX < 0:
        playerX = 0
    # 800 - 64 = 763
    if playerX > 736:
        playerX = 736
    # set screen

    EnemyX += enemy_x_change * dt

    if EnemyX < 0:
        EnemyX = 0
        enemy_x_change = 400
        EnemyY += enemy_y_change
    if EnemyX > 736:
        EnemyX = 736
        enemy_x_change = -400
        EnemyY += enemy_y_change

    screen.fill((0, 0, 0))
    # Background
    screen.blit(background, (0, 0))
    Player(playerX, playerY)
    enemy(EnemyX, EnemyY)
    if bullet_state == "fire":
        bullet_y = bullet_y - (bullet_change * dt)
        if bullet_y < 0:
            bullet_y = 480
            bullet_state = "ready"
        else:
            fire_bullet(bullet_x, bullet_y)
    pygame.display.update()
