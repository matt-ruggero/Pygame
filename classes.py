from assets import *
import pygame
import random #Importa as bibliotecas

#Define a classe do chão
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

#Define a classe do teto
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

#Define a classe do astronauta
class Astronaut(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.frame = 0
        self.img = img

        self.image = self.img[self.frame]
        self.rect = self.image.get_rect()
        self.rect.centerx = 150
        self.rect.bottom = 300
        self.speedy = 0

        self.frame_ticks = 200
        self.last_update = pygame.time.get_ticks()
    
    def jump(self):
        self.speedy = -1
    def fall(self):
        self.speedy = 1

    def update(self):
        self.rect.y += self.speedy

        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1

            if self.frame > 3:
                self.frame = 0

            self.image = self.img[self.frame]

        if self.rect.top <= 50:
            self.rect.top = 50
            self.speedy = 0
        if self.rect.bottom >= 270:
            self.rect.bottom = 270
            self.speedy = 0
        
#Define a classe do tanque de oxigênio
class Tanque(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(50, 230)

        self.speedx = -1

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.rect.x = WIDTH
            self.rect.y = random.randint(80, 230)

#Define a classe do meteoro roxo (fase 1)
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

#Define a classe do meteoro amarelo (fase 2)
class Meteoro2(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1000, 1500)
        self.rect.y = random.randint(50, 230)
        self.speedx = -2
        self.speedy=0
        while self.speedy==0:
            self.speedy = random.randint(-2, 2)

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right < 0:
            self.rect.x = 600
            self.rect.y = random.randint(50, 230)

        while self.speedy==0:
            self.speedy = random.randint(-2, 2)
        
        if self.rect.top <= 40:
            self.rect.top = 40
            self.speedy = -self.speedy

        if self.rect.bottom >= 270:
            self.rect.bottom = 270
            self.speedy = -self.speedy

#Define a classe do meteoro verde (fase 3)
class Meteoro3(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1000, 1500)
        self.rect.y = random.randint(50, 230)
        self.speedx = - 4

    def update(self):

        self.rect.x += self.speedx

        if self.rect.right < 0:
            self.rect.x = 600
            self.rect.y = random.randint(50, 230)

#Define a classe do monstro
class Monstro(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.frame = 0
        self.img = img

        self.image = self.img[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = -20
        self.rect.y = 0

        self.frame_ticks = 300
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1

            if self.frame > 3:
                self.frame = 0

            self.image = self.img[self.frame]