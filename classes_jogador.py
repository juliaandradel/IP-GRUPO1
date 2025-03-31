import pygame as pg
from pygame.locals import *
from sys import exit
import math


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
        self.vida = 3
        self.rect = pg.Rect(self.x, self.y, self.largura, self.altura)

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

    def tomar_dano(self):
        self.vida -= 1

    def recuperar_vida(self):
        if self.vida < 3:
            self.vida += 1

    def tomar_energetico(self):
        if self.velocidade < 10:
            self.velocidade += 2

    def update(self):
        pg.draw.rect(self.window, self.cor, (self.x, self.y, self.largura, self.altura))
        self.rect = pg.Rect(self.x, self.y, self.largura, self.altura)

    def interface(self):
        fonte = pg.font.SysFont('pixel', 35, bold=False, italic=True)
        mostrar_vida = fonte.render(f'Vida: {self.vida}', True, ('WHITE'))
        self.window.blit(mostrar_vida, (10, 10))


class Tiro_Jogador:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.image = pg.image.load("bola3.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 6

        # Criar um vetor para a posição inicial e um para o mouse
        self.pos = pg.Vector2(x, y)
        target = pg.Vector2(mouse_x, mouse_y)

        # Calcular a direção normalizada
        self.direction = (target - self.pos).normalize() * self.speed

    def update(self, display):
        # Atualizar a posição do tiro
        self.pos += self.direction
        self.rect.center = self.pos  # Atualizar o rect da bola

        # Desenhar a bola na tela
        display.blit(self.image, self.rect.topleft)


