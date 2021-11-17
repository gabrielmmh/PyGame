import pygame
#import random
#from configs import *

largura = 360
altura = 480
FPS = 30

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Inicia o jogo e cria uma janela
pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo")
watch = pygame.time.Clock()


# Loop
estado = True
while estado:
    # Manter o loop na velocidade correta
    watch.tick(FPS)

    # Process input (events)
    for eventos in pygame.event.get():
        # verificar se está fechando a janela
        if eventos.type == pygame.QUIT:
            estado = False

    # Update

    # Desenhar / render
    tela.fill(preto)

    # ~Depois~ de desenhar tudo, flipar o display
    pygame.display.flip()

pygame.quit()