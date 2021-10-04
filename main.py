import pygame
import random

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

enemy_x_change = 0.1
enemy_y_change = 20


# draw the player
def Player(x, y):
    screen.blit(PlayerImg, (x, y))


def enemy(x, y):
    screen.blit(EnemyImg, (x, y))

# game loop
running = True
while running:
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
                player_x_change = -0.2
                last_key_down = 'left'
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.2
                last_key_down = 'right'

    # update player
    playerX += player_x_change
    # bounds checking
    if playerX < 0:
        playerX = 0
    # 800 - 64 = 763
    if playerX > 736:
        playerX = 736
    # set screen

    EnemyX += enemy_x_change

    if EnemyX < 0:
        EnemyX = 0
        enemy_x_change = 0.1
        EnemyY += enemy_y_change
    if EnemyX > 736:
        EnemyX = 736
        enemy_x_change = -0.1
        EnemyY += enemy_y_change
    screen.fill((0, 0, 0))

    Player(playerX, playerY)
    enemy(EnemyX, EnemyY)
    pygame.display.update()
