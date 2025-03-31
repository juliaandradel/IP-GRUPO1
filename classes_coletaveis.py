#aqui vão ficar as classes dos coletáveis: vida extra, chuteira e energético
import pygame as pg
from random import randint

class Vida_extra:
    def __init__(self, tela, posicao_x, posicao_y):
        self.tela = tela
        self.aparecer = False
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.rect = None
    def atualizar(self):
        if self.aparecer:
            pg.draw.rect(self.tela, ('RED'), (self.posicao_x, self.posicao_y, 16, 16))
            # Atualizar a posição do retângulo para calcular a colisão
            self.rect = pg.Rect(self.posicao_x, self.posicao_y, 16, 16)
        
class Energetico:
    def __init__(self, tela, posicao_x, posicao_y):
        self.tela = tela
        self.aparecer = False
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.rect = None
    def atualizar(self):
        if self.aparecer:
            pg.draw.rect(self.tela, ('YELLOW'), (self.posicao_x, self.posicao_y, 16, 16))
            # Atualizar a posição do retângulo para calcular a colisão
            self.rect = pg.Rect(self.posicao_x, self.posicao_y, 16, 16)