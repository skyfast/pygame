import pygame


class Player:
    PlayerImg = pygame.image.load('player.png')
    x_change = 400

    def __init__(self):
        self.x_cord = 370
        self.y_cord = 480
        self.moving = "none"

    def move(self, dt):
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