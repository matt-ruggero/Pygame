#Importa bibliotecas
import pygame, sys
from classes import *
from assets import *
from pygame.locals import *

#Inicia Pygame
pygame.init()

#Define a janela e nome do jogo
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zero Gravity Run')
font = pygame.font.SysFont(None, 20)

#Função para texto dos botões
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
 
#Função para tela de início e fim
def main_menu():
    x = True
    while x:
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(240, 200, 100, 15)
        button_2 = pygame.Rect(240, 230, 100, 15)
        menu_img = pygame.image.load('imagens/menu.jpeg').convert()
        menu = pygame.transform.scale(menu_img, (WIDTH, HEIGHT))
        window.blit(menu, [0, 0])
        pygame.draw.rect(window, (150, 69, 255,), button_1)
        pygame.draw.rect(window, (200, 69, 69,), button_2)
        draw_text('click to start', font, (255, 255, 255), window, 250, 200)
        draw_text('quit game',font,(255,255,255),window,258,230)
        pygame.display.update()

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pontuacao = 0
    
        if button_1.collidepoint((mx, my)):
            if click:
                pontuacao = game()
                x = False
                rejogar = True
                while rejogar:
                    #Define a pontuação mais alta
                    with open('highscore.txt', 'r') as highscore: 
                        maior_score = int(highscore.read())
                    if maior_score < pontuacao:
                        with open('highscore.txt', 'w') as hs:
                            hs.write('{0}'.format(pontuacao))
                    #_______________________________

                    #Define e mostra a tela de GAME OVER
                    window.blit(fim, (0, 0)) 
                    pygame.mixer.music.play(0)
                    fonte = pygame.font.SysFont('Verdana', 15)
                    fonte_2 = pygame.font.SysFont('Verdana', 25)
                    space = fonte.render('Pressione SPACE para retornar ao menu principal', True, (255, 255, 255))
                    pontos = fonte_2.render('Pontuação: {0}'.format(pontuacao), True, (255, 255, 255))
                    pont_maior = fonte_2.render('Highscore: {0}'.format(maior_score), True, (255, 255, 255))
                    window.blit(space, (130, 200))
                    window.blit(pontos, (170,230))
                    window.blit(pont_maior, (170,260))
                    #_______________________________
                    
                    #Finalizar jogo
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                x = True
                                rejogar = False
                    pygame.display.update()
                    
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
                x = False

#Função do jogo
def game():
    running = True
    while running:
        
        #Carrega imagens
        background_img = pygame.image.load('imagens/background.jpeg').convert()
        background = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
        background2_img = pygame.image.load('imagens/fundo_amarelo.jpeg').convert()
        background2 = pygame.transform.scale(background2_img, (WIDTH, HEIGHT))
        background3_img = pygame.image.load('imagens/fundo_verde.jpg').convert()
        background3 = pygame.transform.scale(background3_img, (WIDTH, HEIGHT))
        ground_img = pygame.image.load('imagens/pedra.png').convert_alpha()
        ground = pygame.transform.scale(ground_img, (GROUND_WIDTH, GROUND_HEIGHT))
        astronaut_img = pygame.image.load('imagens/astronauta_novo.png').convert_alpha()
        astronaut = pygame.transform.scale(astronaut_img, (ASTRO_WIDTH, ASTRO_HEIGHT))
        mov1_img = pygame.image.load('imagens/movimento1.png').convert_alpha()
        mov1 = pygame.transform.scale(mov1_img, (ASTRO_WIDTH, ASTRO_HEIGHT))
        mov2_img = pygame.image.load('imagens/movimento2.png').convert_alpha()
        mov2 = pygame.transform.scale(mov2_img, (ASTRO_WIDTH, ASTRO_HEIGHT))
        caminhar = [astronaut, mov1, astronaut, mov2]
        tanque_o2_img = pygame.image.load('imagens/o2.png')
        tanque_o2 = pygame.transform.scale(tanque_o2_img, (TANQUE_WIDTH, TANQUE_HEIGHT))
        meteoro_img = pygame.image.load('imagens/pedra_azul.png').convert_alpha()
        meteoro = pygame.transform.scale(meteoro_img, (METEORO_WIDTH, METEORO_HEIGHT))
        meteoro2_img = pygame.image.load('imagens/pedra_amarela.PNG').convert_alpha()
        meteoro2 = pygame.transform.scale(meteoro2_img, (METEORO_WIDTH, METEORO_HEIGHT))
        meteoro3_img = pygame.image.load('imagens/pedra_verde.PNG').convert_alpha()
        meteoro3 = pygame.transform.scale(meteoro3_img, (METEORO3_WIDTH, METEORO3_HEIGHT))
        monstro_img = pygame.image.load('imagens/monstro.png')
        monstro = pygame.transform.scale(monstro_img, (MONSTRO_WIDTH, MONSTRO_HEIGHT))
        monstro2_img = pygame.image.load('imagens/frame_1.png')
        monstro2 = pygame.transform.scale(monstro2_img, (MONSTRO_WIDTH, MONSTRO_HEIGHT))
        monstro3_img = pygame.image.load('imagens/frame_2.png')
        monstro3 = pygame.transform.scale(monstro3_img, (MONSTRO_WIDTH, MONSTRO_HEIGHT))
        monstro_anim = [monstro3, monstro, monstro2, monstro]
        heart_img = pygame.image.load('imagens/coracao.png')
        heart = pygame.transform.scale(heart_img, (30, 30))

        #Define quantidade de vidas
        lives = 3

        # Carrega os sons do jogo
        #Som de background com mais de 1 vida
        if lives > 1:
            pygame.mixer.music.load('audios/space.mp3')
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(lives > 1)
        
        #Sons de efeitos sonoros
        meteoro_sound = pygame.mixer.Sound('audios/impact.mp3')
        oxygen_sound = pygame.mixer.Sound('audios/oxygen1.mp3')
        pygame.mixer.Sound.set_volume(oxygen_sound, 0.1)
        vida = pygame.mixer.Sound('audios/1vida.mp3')
        pygame.mixer.Sound.set_volume(vida, 0.4)

        #Função que desenha as vidas na tela do jogo
        def draw_lives(surf, x, y, lives, img):
            for i in range(lives):
                img_rect = img.get_rect()
                img_rect.x = x
                img_rect.y = y + 30 * i
                surf.blit(img, img_rect)

        #Define a pontuação inicial
        score = 0
        font = pygame.font.SysFont('Verdana', 20)

        game = True

        #Define FPS do jogo
        clock = pygame.time.Clock()
        FPS = 100

        #Cria grupos de Sprites
        tanques = pygame.sprite.Group()
        meteoros_azul = pygame.sprite.Group()
        all_grounds = pygame.sprite.Group()
        all_roofs = pygame.sprite.Group()
        meteoros_verde = pygame.sprite.Group()
        meteoros_amarelo = pygame.sprite.Group()

        #Cria os Sprites e coloca nos grupos
        for i in range(0, 650, 50):
            pedra = Ground(ground)
            pedra.rect.x += i
            all_grounds.add(pedra)

        for i in range(0, 650, 50):
            pedra = Roof(ground)
            pedra.rect.x += i
            all_roofs.add(pedra)

        for i in range(4):
            meteor = Meteoro(meteoro)
            meteoros_azul.add(meteor)

        astronauta = Astronaut(caminhar)
        tanque = Tanque(tanque_o2)
        tanques.add(tanque)
        monstroo = Monstro(monstro_anim)

        parar = []
        parar_2 = []

        #Loop do jogo
        while game:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                #Define a movimentação
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_UP:
                        astronauta.jump()
                    if event.key == pygame.K_DOWN:
                        astronauta.fall()

            #Condição de derrota
            if astronauta.rect.centerx == 90:
                game = False
            
            #Mudança de fases
            if score == 100:
                background = background2
                if parar == []:
                    for i in range(2):
                        meteor = Meteoro2(meteoro2)
                        meteoros_amarelo.add(meteor)
                    parar.append(1)
            
            if score == 200: 
                background = background3
                if parar_2 == []:
                    for i in range(3):
                        meteor = Meteoro3(meteoro3)
                        meteoros_verde.add(meteor)
                    parar_2.append(1)

            #Mostra pontuação na tela
            texto = font.render('Pontuação: {0}'.format(score), True, (255, 255, 255))

            #Atualiza a posição de todos os Sprites
            all_grounds.update()
            all_roofs.update()
            astronauta.update()
            monstroo.update()
            tanques.update()
            meteoros_azul.update()
            meteoros_verde.update()
            meteoros_amarelo.update()

            #Define eventos para pontuação 
            hits = pygame.sprite.spritecollide(astronauta, tanques, True, pygame.sprite.collide_mask)

            for tanque in hits:
                t = Tanque(tanque_o2)
                tanques.add(t)
                score += 10
                oxygen_sound.play()

            #Define eventos para danos 
            hits = pygame.sprite.spritecollide(astronauta, meteoros_azul, True, pygame.sprite.collide_mask)

            for meteor in hits:
                astronauta.rect.x -= 20
                m = Meteoro(meteoro)
                meteoros_azul.add(m)
                lives -= 1
                meteoro_sound.play()
            
            hits = pygame.sprite.spritecollide(astronauta, meteoros_amarelo, True, pygame.sprite.collide_mask)

            for meteor in hits:
                astronauta.rect.x -= 20
                m = Meteoro2(meteoro2)
                meteoros_amarelo.add(m)
                lives -= 1
                meteoro_sound.play()
                
            hits = pygame.sprite.spritecollide(astronauta, meteoros_verde, True, pygame.sprite.collide_mask)

            for meteor in hits:
                astronauta.rect.x -= 20
                m = Meteoro3(meteoro3)
                meteoros_verde.add(m)
                lives -= 1
                meteoro_sound.play()  

            #Troca trilha sonora para quando tem 1 vida
            if lives == 1:
                pygame.mixer.music.stop()
                vida.play(-1)

            #Troca música de 1 vida para a música inicial
            if lives == 0:
                vida.stop()

            #Desenha os Sprites na tela
            window.fill((0, 0, 0))
            window.blit(background, (0, 0))
            window.blit(astronauta.image, astronauta.rect)
            tanques.draw(window)
            meteoros_azul.draw(window)
            meteoros_amarelo.draw(window)
            meteoros_verde.draw(window)
            all_grounds.draw(window)
            all_roofs.draw(window)
            window.blit(monstroo.image, monstroo.rect)
            window.blit(texto, (10,10))
            draw_lives(window, 10, 30, lives, heart)
            pygame.display.update()
        #Condição de finaização do jogo
        if lives == 0:
            running = False
    return score

#Define a imagem de GAME OVER
fim_img = pygame.image.load('imagens/tela_final.png')
fim = pygame.transform.scale(fim_img, (WIDTH, HEIGHT))

#Roda o jogo 
while True:
    main_menu()