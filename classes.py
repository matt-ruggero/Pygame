from assets import *
import pygame
import random

class Ground(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 250
        self.speedx = -1

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.rect.x = WIDTH

class Roof(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speedx = -1

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.rect.x = WIDTH

class Astronaut(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = 300
        self.speedy = 0
    
    def jump(self):
        self.speedy = -1
    def fall(self):
        self.speedy = 1

    def update(self):
        self.rect.y += self.speedy

        if self.rect.top <= 50:
            self.rect.top = 50
            self.speedy = 0
        if self.rect.bottom >= 270:
            self.rect.bottom = 270
            self.speedy = 0

class Tanque(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.speedx = - 1

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.rect.x = WIDTH
            self.rect.y = random.randint(80, 230)

class Meteoro(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1000, 1500)
        self.rect.y = random.randint(50, 230)
        self.speedx = - 2

    def update(self):

        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.rect.x = 600
            self.rect.y = random.randint(50, 230)
