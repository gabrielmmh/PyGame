# Sprite classes for platform game
import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        #personagem
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA / 2, ALTURA / 2)
        self.pos = vec(LARGURA / 2, ALTURA / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

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
        self.image.fill(AMARELO)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y