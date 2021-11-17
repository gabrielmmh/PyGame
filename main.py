import pygame as pg
import random
from settings import *

# Opções de jogo 
TITLE = "Meu jogo"
LARGURA = 360
ALTURA = 480
FPS = 30

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

class Jogo:
    # sprite do Player
    def __init__(self):
        # Inicia a tela do jogo
        pg.init()
        pg.mixer.init()
        self.tela = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption(TITLE)
        self.watch = pg.time.Clock()
        self.estado = True
    
    def new(self):
        # Começa um novo jogo
        self.all_sprites = pg.sprites.Group()
        self.run()

    def run(self):
        # Loop do jogo
        self.jogando = True
        while self.jogando:
            self.watch.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Loop do jogo - update
        self.all_sprites.update()

    def events(self):
        # Loop do jogo - eventos
        for eventos in pg.event.get():
            # verificar se está fechando a janela
            if eventos.type == pg.QUIT:
                if self.jogando:
                    self.jogando = False
                estado = False

    def draw(self):
        # Loop do jogo - desenhos
        self.tela.fill(preto)
        self.all_sprites.draw(self.tela)

        # Depois de desenhar tudo, flipar o display
        pg.display.flip()

    def show_start_screen(self):
        # Tela inicial
        pass

    def show_go_screen(self):
        # Tela de fim do jogo
        pass

j = Jogo()
j.show_start_screen()

while j.estado:
    j.new()
    j.show_go_screen()

pg.quit()