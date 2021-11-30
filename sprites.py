# Sprite classes for platform game
import pygame as pg
from settings import *
from os import path
vec = pg.math.Vector2





class Player(pg.sprite.Sprite):
    def __init__(self):
        #personagem
        img_dir = path.join(path.dirname(__file__),'img')
        # Carregando as imagens
        froggy1 = pg.image.load(path.join(img_dir,"Froggy1.png")).convert()
        pg.sprite.Sprite.__init__(self)
        self.image = froggy1

        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA / 2, ALTURA / 2)
        self.pos = vec(LARGURA / 2, ALTURA / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def import_image(self):

        self.animacao = {'puland':[] , 'caindo':[]}


    def animacao(self):
        animacao = self.animation[self.status]

        #loop para animar
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animacao):
            self.frame_index = 0
            # 'desbuga' o loop, sempre retoma ao inicio apos acabar as imagens
        self.image = animacao[int(self.frame_index)]
    
    def status(self):
        if self.vel.y < 0 :
            self.status = 'pulando'
        if self.vel.y > 0:
            self.status = 'caindo'


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

class Platform(pg.sprite.Sprite):
    def __init__( self,x,y,l,h ):
        #Plataformas
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((l,h))
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y