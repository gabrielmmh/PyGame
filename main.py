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
        self.font_name = pg.font.match_font(FONT_NAME)

    def new(self):
        plat = Platform(0,ALTURA - 40 , LARGURA , 40)
        plat2 = Platform(20,ALTURA - 300  , 100 , 40)
        # Coomeça um novo jogo
        self.score = 0
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
        # Quando estiver subindo o player 'n enconsta' na plataforma
        if self.player.vel.y > 0:
            colisao = pg.sprite.spritecollide(self.player,self.plataformas,False)
            #colisao na plataforma e  pulo automatico
            if colisao:
                self.player.pos.y = colisao[0].rect.top
                self.player.vel.y = 0
                self.player.vel.y = -15
        #Subir tela
        if self.player.rect.top <=  ALTURA/4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.plataformas:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= ALTURA:
                    plat.kill()
                    self.score += 10
        
        #player morre
        if self.player.rect.bottom > ALTURA:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.plataformas) == 0:
            self.playing = False

        #Criando plataformas novas
        while len(self.plataformas) < 6:
            largura = random.randrange(50, 100)
            p = Platform(random.randrange(0, LARGURA-largura),
                        random.randrange(-75, -30),
                         largura, 20)
            self.plataformas.add(p)
            self.all_sprites.add(p)


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
        self.draw_text(str(self.score), 40, BRANCO, LARGURA/2, 15)
        # Depois de desenhar tudo, rodar o display
        pg.display.flip()

    def show_start_screen(self):
        # tela de inicio
        pass

    def show_go_screen(self):
        # tela final
        pass

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Jogo()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
