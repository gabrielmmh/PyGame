import pygame as pg
import random
from settings import *
from sprites import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

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
        self.load_data() 
    
    def load_data(self):
        # insere a maior pontuação
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, MAIOR_PONT), 'w') as f:
            try:
                self.maior_pont = int(f.read())
            except:
                self.maior_pont = 0

    def new(self):
        plat = Platform(0,ALTURA - 40 , LARGURA , 40)
        plat2 = Platform(20,ALTURA - 300  , 100 , 40)
        # Coomeça um novo jogo
        self.fundo = pg.image.load(path.join(img_dir, 'fundo.png')).convert()
        self.fundo_ret = self.fundo.get_rect()
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.plataformas = pg.sprite.Group()
        #Cria o player
        self.player = Player()
        self.all_sprites.add(self.player)
        #Cria as plataformas
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
        # Quando estiver subindo o player 'n encosta' na plataforma
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
        
        #Player morre
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
        self.screen.fill(AZULCLARO)
        self.screen.blit(self.fundo, self.fundo_ret)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 40, BRANCO, LARGURA/2, 15)
        # Depois de desenhar tudo, rodar o display
        pg.display.flip()

    def show_start_screen(self):
        # tela de inicio
        self.screen.fill(AZULCLARO)
        self.fundo1 = pg.image.load(path.join(img_dir, 'fundo_inicio1.png')).convert()
        self.fundo1_ret = self.fundo1.get_rect()
        self.fundo2 = pg.image.load(path.join(img_dir, 'fundo_inicio2.png')).convert()
        self.fundo2_ret = self.fundo2.get_rect()
        self.fundo3 = pg.image.load(path.join(img_dir, 'fundo_inicio3.png')).convert()
        self.fundo3_ret = self.fundo3.get_rect()
        self.fundo4 = pg.image.load(path.join(img_dir, 'fundo_inicio4.png')).convert()
        self.fundo4_ret = self.fundo4.get_rect()
        self.tela_inicio1 = [self.fundo1, self.fundo2, self.fundo3, self.fundo4]
        self.tela_inicio2 = [self.fundo1_ret, self.fundo2_ret, self.fundo3_ret, self.fundo4_ret]
        '''i=1
        while i <= len(self.tela_inicio1):
            self.screen.blit(self.tela_inicio1[i], self.tela_inicio2[i]) '''  
        self.screen.blit(self.fundo1, self.fundo1_ret)     
        pg.display.flip()
        self.esperando_clique()
        pass

    def show_go_screen(self):
        # tela final
        if not self.running:
            return # Fecha o app se estiver no meio do jogo
        self.screen.fill(PRETO)
        self.draw_text('Você matou o sapo!', 30, BRANCO, LARGURA/2, ALTURA/4)
        self.draw_text('Pontuação: '+ str(self.score), 22, BRANCO, LARGURA/2, ALTURA/2)
        self.draw_text('Clique em qualquer tecla para jogar novamente', 22, BRANCO, LARGURA/2, ALTURA * 4/5)
        if self.score > self.maior_pont:
            self.maior_pont = self.score
            self.draw_text('NOVO RECORDE!', 22, BRANCO, LARGURA/2, ALTURA/2 + 50)
            #abrir as f, para ser mais pratico para escrever (as file)
            with open(path.join(self.dir, MAIOR_PONT), 'w') as f: 
                f.write(str(self.score))
        
        else:
            self.draw_text('Maior Pontuação: ' + str(self.maior_pont), 22, PRETO, LARGURA/2, ALTURA/2 + 40)

        pg.display.flip()
        self.esperando_clique()
        pass

    # Saindo da tela inicial ou final
    def esperando_clique(self):
         esperando = True
         while esperando:
             # Manter a tela enquanto esperand = True
             self.clock.tick(FPS)
             for evento in pg.event.get():
                 # Click
                 if evento.type == pg.QUIT:
                    esperando = False
                    self.running = False
                 if evento.type == pg.KEYUP:
                    esperando = False

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
