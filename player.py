import pygame

from bullet import Bullet


class Player:
    PlayerImg = pygame.image.load('player.png')
    x_change = 400

    def __init__(self):
        self.x_cord = 370
        self.y_cord = 480
        self.moving = "none"
        self.bullet = Bullet()

    def move(self, dt):
        self.bullet.move(dt)
        if self.moving == "none":
            return
        elif self.moving == "left":
            self.x_cord -= self.x_change * dt
            if self.x_cord < 0:
                self.x_cord = 0
        elif self.moving == "right":
            self.x_cord += self.x_change * dt
            if self.x_cord > 736:
                self.x_cord = 736



    def draw(self, screen):
        screen.blit(self.PlayerImg, (self.x_cord, self.y_cord))
        self.bullet.draw(screen)

    def shoot(self):
        self.bullet.fire_bullet(self.x_cord)

    def check_hit(self, x, y):
        return self.bullet.check_hit(x, y)
