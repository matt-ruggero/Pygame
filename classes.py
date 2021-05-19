from assets import *
import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 250
        self.speedx = -1

    def update(self):
        # Atualizando a posição do chão
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.rect.x = WIDTH

class Roof(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 0
        self.speedx = -1

    def update(self):
        # Atualizando a posição do chão
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.rect.x = WIDTH

class Astronaut(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.bottom = 300
        self.speedy = 0
    
    def jump(self):
        self.speedy = -1
    def fall(self):
        self.speedy = 1

    def update(self):
        # Atualização da posição do astronauta
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.top <= 50:
            self.rect.top = 50
            self.speedy = 0
        if self.rect.bottom >= 270:
            self.rect.bottom = 270
            self.speedy = 0