import pygame

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
# Icons made by https://www.flaticon.com/authors/smashicons from www.flaticon.com
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)
# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # set screen
    screen.fill((255, 0, 0))
    pygame.display.update()
