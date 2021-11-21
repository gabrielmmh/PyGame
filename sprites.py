import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def _init_(self):
        pg.sprite.Sprite._init_(self)
        self.image = pg.Surface((30,40))
        self.image.fill(vermelho)
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA / 2, ALTURA / 2)
        self.vx = 0
        self.vy = 0
    
    def movimentacao(self):
        self.vx=0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -5
        if keys[pg.K_RIGHT]:
            self.vx = 5
        
        self.rect.x += self.vx
        self.rect.y += self.vy