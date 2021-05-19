#Importa e inicializa os pacotes
import pygame

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
ground_x = 0
ground_y = 250
ground_speed_x = -0.1

game = True

clock = pygame.time.Clock()
FPS = 15

#Loop principal
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    ground_x += ground_speed_x

    if ground_x + GROUND_WIDTH < 0:
        ground_x = WIDTH

    #Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(ground, (ground_x, ground_y))
    pygame.display.update()

#Finaliza o pygame
pygame.quit()