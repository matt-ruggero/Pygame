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