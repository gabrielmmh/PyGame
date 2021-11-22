import pygame as pg
import random
from settings import *
from sprites import *

class Jogo:
    def __init__(self):
        # Inicializa a janela do jogo
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((LARGURA, ALTURA))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # Coomeça um novo jogo
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # Loop do jogo
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Loop do jogo - Update
        self.all_sprites.update()

    def events(self):
        # Loop do jogo - eventos
        for event in pg.event.get():
            # checar se está fechando a janela
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Loop do jogo - desenho
        self.screen.fill(PRETO)
        self.all_sprites.draw(self.screen)
        # Depois de desenhar tudo, rodar o display
        pg.display.flip()

    def show_start_screen(self):
        # tela de inicio
        pass

    def show_go_screen(self):
        # tela final
        pass

g = Jogo()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()