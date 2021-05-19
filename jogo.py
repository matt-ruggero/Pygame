#Importa e inicializa os pacotes
import pygame

pygame.init()

#Gera a tela principal
WIDTH = 600
HEIGHT = 300

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zero Gravity Run')

#Inicia os assets
background = pygame.image.load('imagens/background.jpeg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

game = True

#Loop principal
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    #Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    pygame.display.update()

#Finaliza o pygame
pygame.quit()