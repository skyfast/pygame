import pygame
import random
import time

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
score_vale = 0
font = pygame.font.Font('freesansbold.ttf', 32)

text_x = 10
text_y = 10

e1 = enemy.Enemy(random.randint(0, 735), 50)
e2 = enemy.Enemy(random.randint(0, 735), 90)
e3 = enemy.Enemy(random.randint(0, 735), 90)
e4 = enemy.Enemy(random.randint(0, 735), 90)
e5 = enemy.Enemy(random.randint(0, 735), 90)
enemy_list = [e1, e2, e3, e4, e5]


def add_enemy(e_list):
    new_e = enemy.Enemy(random.randint(0, 735), 50)
    e_list.append(new_e)


def show_score():
    score = font.render("Score = {}".format(str(score_vale)), True, (255, 255, 255))
    screen.blit(score, (text_x, text_y))


# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


p = player.Player()

dt = 0
prev_time = time.time()
level = 1
enemy_left_to_lvl = 4
# game loop
running = True
in_game = True
while running:
    while in_game:
        now = time.time()
        dt = now - prev_time
        prev_time = now
        # check all game events
        for event in pygame.event.get():
            # quits the game
            if event.type == pygame.QUIT:
                running = False
                in_game = False

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

        for e in enemy_list:
            e.move(dt)
            if p.check_hit(e.x_cord, e.y_cord):
                e.x_cord = random.randint(0, 735)
                e.y_cord = 50
                score_vale += 1
                enemy_left_to_lvl -= 1
                if enemy_left_to_lvl <= 0:
                    add_enemy(enemy_list)
                    level += 1
                    enemy_left_to_lvl = level * 4

            if e.y_cord > 440:
                in_game = False
            e.draw(screen)

        p.draw(screen)
        show_score()
        pygame.display.update()

    for event in pygame.event.get():
        # quits the game
        if event.type == pygame.QUIT:
            running = False
    p.draw(screen)
    game_over()
    show_score()
    pygame.display.update()
