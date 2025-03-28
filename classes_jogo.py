import pygame as pg
from pygame.locals import *
from sys import exit


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

# ---------------------- Tela de escolha ----------------------

import pygame as pg
class Tela_de_escolha:
    def __init__(self, window):
        self.window = window
        self.fonte = pg.font.SysFont('arial', 50)
        self.opcao = '1'
        self.distancia_opcoes = 300
        self.triangulo_1 = [(300, 600), (380, 600), (340, 540)]
        self.triangulo_2 = [(580, 600), (660, 600), (620, 540)]
        self.triangulo_3 = [(860, 600), (940, 600), (900, 540)]
        self.nome_messi = ['Lionel Messi',(200,620)]
        self.nome_cr7 = ['Cristiano Ronaldo',(430,620)]
        self.nome_neymar = ['Neymar Jr.',(790,620)]

    def movimentacao_escolha(self, evento):
        if evento.type == KEYDOWN:
            if evento.key == K_a:
                if self.opcao == '2':
                    self.opcao = '1'
                elif self.opcao == '3':
                    self.opcao = '2'
            if evento.key == K_d:
                if self.opcao == '1':
                    self.opcao = '2'
                elif self.opcao == '2':
                    self.opcao = '3'

    def mostrar_texto(self):
        texto = self.fonte.render('ESCOLHA SEU PERSONAGEM', True, ('WHITE'))
        self.window.blit(texto, (300, 100))

    def triangulos_de_escolha(self):
        if self.opcao == '1':
            texto_jogador = self.fonte.render(self.nome_messi[0], True, ('White'))
            self.window.blit(texto_jogador, (self.nome_messi[1]))
            pg.draw.polygon(self.window, ('DARK RED'), (self.triangulo_1[0], self.triangulo_1[1], self.triangulo_1[2]))
        elif self.opcao == '2':
            texto_jogador = self.fonte.render(self.nome_cr7[0], True, ('White'))
            self.window.blit(texto_jogador, (self.nome_cr7[1]))
            pg.draw.polygon(self.window, ('DARK RED'), (self.triangulo_2[0], self.triangulo_2[1], self.triangulo_2[2]))
        elif self.opcao == '3':
            texto_jogador = self.fonte.render(self.nome_neymar[0], True, ('White')) 
            self.window.blit(texto_jogador, (self.nome_neymar[1]))
            pg.draw.polygon(self.window, ('DARK RED'), (self.triangulo_3[0], self.triangulo_3[1], self.triangulo_3[2]))
