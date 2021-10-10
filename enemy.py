import pygame


class Enemy:
    EnemyImg = pygame.image.load('trash.png')
    enemy_y_change = 20
    enemy_x_change = 400

    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
        self.going_right = True

    def move(self, dt):
        if self.going_right:
            self.x_cord = self.x_cord + (dt * self.enemy_x_change)
        else:
            self.x_cord = self.x_cord - (dt * self.enemy_x_change)
        if self.x_cord < 0:
            self.x_cord = 0
            self.going_right = True
            self.y_cord += self.enemy_y_change
        if self.x_cord > 736:
            self.x_cord = 736
            self.going_right = False
            self.y_cord += self.enemy_y_change


    def draw(self, screen):
        screen.blit(self.EnemyImg, (self.x_cord, self.y_cord))

