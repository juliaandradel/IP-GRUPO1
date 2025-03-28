import pygame as pg
from sys import exit
from classes_jogo import Jogador

pg.init()
largura_tela = 1280
altura_tela = 720
tela = pg.display.set_mode((largura_tela, altura_tela))
player = Jogador(tela, 100, 100, 30, 30, 'RED', 6, pg.K_w, pg.K_s, pg.K_a, pg.K_d)
fps = pg.time.Clock()

while True:
    fps.tick(144)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    tela.fill((0, 0, 0))
    player.movimentacao()
    player.update()
    pg.display.update()