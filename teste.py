#Importa e inicializa os pacotes
import pygame
from classes import *
from assets import *


pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zero Gravity Run')

background_img = pygame.image.load('imagens/background.jpeg').convert()
background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
ground_img = pygame.image.load('imagens/pedra.png').convert_alpha()
ground = pygame.transform.scale(ground_img, (GROUND_WIDTH, GROUND_HEIGHT))
astronaut_img = pygame.image.load('imagens/astronauta_novo.png').convert_alpha()
astronaut = pygame.transform.scale(astronaut_img, (ASTRO_WIDTH, ASTRO_HEIGHT))
tanque_o2_img = pygame.image.load('imagens/o2.png')
tanque_o2 = pygame.transform.scale(tanque_o2_img, (TANQUE_WIDTH, TANQUE_HEIGHT))
meteoro_img = pygame.image.load('imagens/pedra.png').convert_alpha()
meteoro = pygame.transform.scale(meteoro_img, (METEORO_WIDTH, METEORO_HEIGHT))

#########
mov1_img = pygame.image.load('imagens/movimento1.png').convert_alpha()
mov1 = pygame.transform.scale(mov1_img, (ASTRO_WIDTH, ASTRO_HEIGHT))
mov2_img = pygame.image.load('imagens/movimento2.png').convert_alpha()
mov2 = pygame.transform.scale(mov2_img, (ASTRO_WIDTH, ASTRO_HEIGHT))
andando_anim = []
andando_anim.append(mov1)
andando_anim.append(astronaut)
andando_anim.append(mov2)
#########


game = True

clock = pygame.time.Clock()
FPS = 100

tanques = pygame.sprite.Group()
all_meteoros = pygame.sprite.Group()
all_grounds = pygame.sprite.Group()
all_roofs = pygame.sprite.Group()

for i in range(0, 650, 50):
    pedra = Ground(ground)
    pedra.rect.x += i
    all_grounds.add(pedra)

for i in range(0, 650, 50):
    pedra = Roof(ground)
    pedra.rect.x += i
    all_roofs.add(pedra)

for i in range(3):
    meteor = Meteoro(meteoro)
    all_meteoros.add(meteor)

###
astronauta = Astronaut(andando_anim)
tanque = Tanque(tanque_o2)
tanques.add(tanque)

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
    tanques.update()
    all_meteoros.update()

    hits = pygame.sprite.spritecollide(astronauta, tanques, True, pygame.sprite.collide_mask)

    for tanque in hits:
        t = Tanque(tanque_o2)
        tanques.add(t)
    
    hits = pygame.sprite.spritecollide(astronauta, all_meteoros, False, pygame.sprite.collide_mask)
    if len(hits) > 0:
        game = False

    #Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(astronauta.image, astronauta.rect)
    tanques.draw(window)
    all_meteoros.draw(window)
    all_grounds.draw(window)
    all_roofs.draw(window)
    pygame.display.update()

#Finaliza o pygame
pygame.quit()