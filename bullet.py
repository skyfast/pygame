import pygame
import math


class Bullet:
    bullet_img = pygame.image.load('bullet.png')
    base_y = 480
    bullet_change = 550

    def __init__(self):
        self.x_cord = 0
        self.y_cord = self.base_y
        self.is_ready = True

    def fire_bullet(self, x):
        if self.is_ready:
            self.x_cord = x
            self.is_ready = False

    def move(self, dt):
        if not self.is_ready:
            self.y_cord -= self.bullet_change * dt
            if self.y_cord <= 0:
                self.y_cord = self.base_y
                self.is_ready = True

    def check_hit(self, x, y):
        distance = math.sqrt(math.pow(x - self.x_cord, 2) + math.pow(y - self.y_cord, 2))
        if distance < 30:
            self.is_ready = True
            self.y_cord = self.base_y
            return True
        else:
            return False

    def draw(self, screen):
        if not self.is_ready:
            screen.blit(self.bullet_img, (self.x_cord, self.y_cord))
