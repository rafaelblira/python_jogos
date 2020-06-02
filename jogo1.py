import pygame
from random import randint
pygame.init()

x = 170
y = 100 #define a posicao do carro
pos_x = 200
pos_y = 800
pos_y_a = 800
pos_y_r = 800
pos_y_v = 800
timer = 0
tempo_segundo = 0
velocidade = 10 #quantos pixels vai andar quando for pressionado
velocidade_outros = 5
fundo = pygame.image.load('pista1.png') #salvando imagem de fundo
carro = pygame.image.load('carrinho_azul.png') #salvando imagem do carro
caminhonete = pygame.image.load('caminhonete_cinza.png')
c_amarelo = pygame.image.load('carrinho_amarelo.png')
c_rosa = pygame.image.load('carrinho_rosa.png')
c_verde = pygame.image.load('carrinho_verde.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render('Tempo: ', True, (255, 255, 255), (0, 0, 0) )
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)


janela = pygame.display.set_mode((800, 600)) #definindo o tamanho da janela

pygame.display.set_caption('Criando jogo com python') #definindo o nome que vai aparecer na janela

janela_aberta = True
while janela_aberta: #mantendo a janela aberta
    pygame.time.delay(50) # delay da tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    
    if comandos[pygame.K_RIGHT] and x<=400:
        x += velocidade

    if comandos[pygame.K_LEFT] and x>= 170:
        x -= velocidade

    #detecta colisao
    if ((x + 80 < pos_x and y - 180 < pos_y)): #colisao lado esquerdo
        y = 1200

    if ((x - 80 > pos_x + 150 and y + 180 > pos_y_a)): #colisao lado direito
         y = 1200
    
    if ((x - 80 > pos_x + 200 and y + 180 > pos_y_r)): #colisao lado direito
         y = 1200

    if ((x - 80 > pos_x + 80 and y + 180 > pos_y_v)): #colisao lado direito
         y = 1200

    if (pos_y <= -100):
        pos_y = randint(800, 1000)
    
    if (pos_y_a <= -100):
        pos_y_a = randint(1200, 2000)

    if (pos_y_r <= -100):
        pos_y_r = randint(2200, 3000)
        
    if (pos_y_v <= -100):
        pos_y_v = randint(1100, 2500)

    if (timer < 20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render('Tempo: ' + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0) )
        timer = 0

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros + 2
    pos_y_r -= velocidade_outros + 3
    pos_y_v -= velocidade_outros + 4

    janela.blit(fundo, (0, 0)) #adiciona imagem no fundo
    janela.blit(carro, (x, y))
    janela.blit(caminhonete, (pos_x, pos_y))
    janela.blit(c_amarelo, (pos_x + 150, pos_y_a))
    janela.blit(c_rosa, (pos_x + 200, pos_y_r))
    janela.blit(c_verde, (pos_x + 80, pos_y_v))
    janela.blit(texto, pos_texto)



    pygame.display.update() #atualiza a tela
        
pygame.quit()
    