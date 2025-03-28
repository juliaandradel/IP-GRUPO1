import pygame as pg


class Jogador:
    def __init__(self, window, x, y, largura, altura, cor, velocidade, cima, baixo, esquerda, direita):
        self.window = window
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.velocidade = velocidade
        self.cima = cima
        self.baixo = baixo
        self.esquerda = esquerda
        self.direita = direita
    
    # agora, vamos criar os métodos para o player(movimentação, draw, etc)
    def movimentacao(self):
        keys = pg.key.get_pressed()
        if keys[self.cima] and self.y > 0:
            self.y -= self.velocidade
        if keys[self.baixo] and self.y < 720 - self.altura:
            self.y += self.velocidade
        if keys[self.esquerda] and self.x > 0:
            self.x -= self.velocidade
        if keys[self.direita] and self.x < 1280 - self.largura:
            self.x += self.velocidade
    
    def update(self):
        pg.draw.rect(self.window, self.cor, (self.x, self.y, self.largura, self.altura))