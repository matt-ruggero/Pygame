#Importa e inicializa os pacotes
import pygame
from classes import *
from assets import *


pygame.init()

#Gera a tela principal
WIDTH = 600
HEIGHT = 300

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zero Gravity Run')

#Inicia os assets
GROUND_WIDTH = 50
GROUND_HEIGHT = 50
background_img = pygame.image.load('imagens/background.jpeg').convert()
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
ground_img = pygame.image.load('imagens/pedra.png').convert_alpha()
ground = pygame.transform.scale(ground_img, (GROUND_WIDTH, GROUND_HEIGHT))

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

game = True

clock = pygame.time.Clock()
FPS = 100

all_grounds = pygame.sprite.Group()

for i in range(0, 600, 30):
    pedra = Ground(ground)
    pedra.rect.x += i
    all_grounds.add(pedra)

#Loop principal
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    all_grounds.update()

    #Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    all_grounds.draw(window)
    pygame.display.update()

#Finaliza o pygame
pygame.quit()