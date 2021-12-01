# Sprite classes for platform game
import pygame as pg
from pygame.sprite import groupcollide
from settings import *
from os import path
vec = pg.math.Vector2





class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.current_frame = 0
        self.last_update = 0
        self.load_image()
        self.image = self.stand[0]
        self.image = pg.transform.scale(self.stand[0], (60, 60))
        self.image.set_colorkey(PRETO)
        self.rect = self.image.get_rect()
        self.rect.center = (0, ALTURA - 40,)
        self.pos = vec(0, ALTURA - 40,)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.tempo = 0 
        self.index_image = 0

    #--------------------------------------------------------------------------------------------------------
    def load_image(self):
        #personagem
        img_dir = path.join(path.dirname(__file__),'img')
        # Carregando as imagens
        froggy1 = pg.image.load(path.join(img_dir,"Froggy1(1).png")).convert()
        froggy2 = pg.image.load(path.join(img_dir,"Froggy2(1).png")).convert()
        froggy3 = pg.image.load(path.join(img_dir,"Froggy3(1).png")).convert()
        #------------------------------------------------------------------------------
        self.stand = [froggy1,froggy2,froggy2,froggy2]
        for a in self.stand:
            a = pg.transform.scale(a,(60,60))
            a.set_colorkey(PRETO) 
          
        self.air = [froggy3]
        for a in self.air:
            a = pg.transform.scale(a,(60,60))
            a.set_colorkey(PRETO)

        self.animation = {'stand':self.stand, 'air':self.air}
    #---------------------------------------------------------------------------------------------------
    def update(self):
        #movimentacao com setas do teclado
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vel.x = -7
        if keys[pg.K_RIGHT]:
            self.vel.x = 7

        # Desaceleracao e Movimentacao
        self.acc.x += self.vel.x * DESACELERACAO
        
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # Permite a movimentacao nos lados da tela 
        if self.pos.x > LARGURA:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = LARGURA

        self.rect.midbottom = self.pos
        ''' self.status()
        anime = self.animation[self.status]
        if self.vel.y > 0:
            
            center = self.rect.center
            self.image = anime[0]
            self.rect = self.image.get_rect()
            self.rect.center = center '''
    #---------------------------------------------------------------------------------------------------
    def status(self):
        if self.pos.y > 1 or self.pos.y < -1 :
            self.status = 'air'
        else:
            self.status = 'stand'
    #---------------------------------------------------------------------------------------------------
    def animacao(self):
        now = pg.time.get_ticks()
        if self.status == 'stand':
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.stand)
                self.image = self.stand[self.current_frame]
                # alinhando imagem e personagem // Fisica Melhor
                bottom = self.rect.bottom
                self.image = self.standing_frame[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        if self.status == 'air':
            
            self.last_update = now
            self.image = self.air[0]
            # alinhando imagem e personagem // Fisica Melhor
            bottom = self.rect.bottom
            self.image = self.standing_frame[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom

        
    

class Platform(pg.sprite.Sprite):
    def __init__( self,x,y,l,h):
        #Plataformas
        
        img_dir = path.join(path.dirname(__file__),'img')
        # Carregando as imagens
        pg.sprite.Sprite.__init__(self)
        nuvem = pg.image.load(path.join(img_dir,"Nuvem.png")).convert()
        self.image = nuvem
        self.image = pg.transform.scale (nuvem, (l+40, h*1.9))
        self.image.set_colorkey(PRETO)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y