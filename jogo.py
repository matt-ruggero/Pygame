#Importa e inicializa os pacotes
import pygame
from pygame.constants import K_UP
from classes import *
from assets import *


pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zero Gravity Run')

background_img = pygame.image.load('imagens/background.jpeg').convert()
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
ground_img = pygame.image.load('imagens/pedra.png').convert_alpha()
ground = pygame.transform.scale(ground_img, (GROUND_WIDTH, GROUND_HEIGHT))
astronaut_img = pygame.image.load('imagens/astronauta.png').convert_alpha()
astronaut = pygame.transform.scale(astronaut_img, (ASTRO_WIDTH, ASTRO_HEIGHT))

game = True

clock = pygame.time.Clock()
FPS = 100

all_grounds = pygame.sprite.Group()
all_roofs = pygame.sprite.Group()

for i in range(0, 600, 30):
    pedra = Ground(ground)
    pedra.rect.x += i
    all_grounds.add(pedra)

for i in range(0, 600, 30):
    pedra = Roof(ground)
    pedra.rect.x += i
    all_roofs.add(pedra)

astronauta = Astronaut(astronaut)

#Loop principal
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                astronauta.jump()
            if event.key == pygame.K_DOWN:
                astronauta.fall()

    all_grounds.update()
    all_roofs.update()
    astronauta.update()

    #Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(astronauta.image, astronauta.rect)
    all_grounds.draw(window)
    all_roofs.draw(window)
    pygame.display.update()

#Finaliza o pygame
pygame.quit()