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
        plat = Platform(0,ALTURA - 40 , LARGURA , 40)
        plat2 = Platform(20,ALTURA - 300  , 100 , 40)
        # Coomeça um novo jogo
        self.all_sprites = pg.sprite.Group()
        self.plataformas = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        for p in LISTA_PLATS:
            p = Platform(*p)
            self.all_sprites.add(p)
            self.plataformas.add(p)
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
        if self.player.vel.y > 0:
            colisao = pg.sprite.spritecollide(self.player,self.plataformas,False)
            if colisao:
                self.player.pos.y = colisao[0].rect.top
                self.player.vel.y = 0
                self.player.vel.y = -15

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