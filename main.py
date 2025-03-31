import pygame as pg
from sys import exit

from classes_jogador import Tiro_Jogador
from classes_jogador import Jogador
from random import randint
from classes_inimigo import Inimigo
from classes_jogo import Tela_de_escolha
from classes_coletaveis import Vida_extra, Energetico

pg.init()
largura = 1280
altura = 720
tela = pg.display.set_mode((largura, altura))
menu = Tela_de_escolha(tela)
player = Jogador(tela, 100, 100, 60, 60, 'BLUE', 3, pg.K_w, pg.K_s, pg.K_a, pg.K_d)
balas_jogador = []
inimigos = [Inimigo(tela, 1) for _ in range(5)]
coletaveis_vida = []
energeticos = []
dado_coletaveis = randint(1, 100)
fps = pg.time.Clock()

while menu.escolheu == False:
    fps.tick(15)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        menu.movimentacao_escolha(event)
    tela.fill((0, 0, 0))
    menu.mostrar_texto()
    menu.triangulos_de_escolha()
    menu.mostrar_imagem()
    pg.display.update()

while True:
    fps.tick(60)
    tela.fill((24, 164, 86))
    mouse_x, mouse_y = pg.mouse.get_pos()
    player.interface()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                balas_jogador.append(Tiro_Jogador(player.x + player.largura // 2, player.y + player.altura, mouse_x, mouse_y))

    player.movimentacao()
    player.update()

    for bala in balas_jogador[:]:
        bala.update(tela)

        for inimigo in inimigos[:]:
            if inimigo.vivo and pg.Rect(inimigo.posicao_x, inimigo.posicao_y, 32, 32).collidepoint(bala.rect.center):
                dado_coletaveis = randint(1, 100)
                if dado_coletaveis <= 10:
                    qual_coletavel = randint(1, 2)
                    if qual_coletavel == 1:
                        coletaveis_vida.append(Vida_extra(tela, inimigo.posicao_x, inimigo.posicao_y))
                    elif qual_coletavel == 2:
                        energeticos.append(Energetico(tela, inimigo.posicao_x, inimigo.posicao_y))
                inimigo.morrer()
                inimigos.remove(inimigo)
                balas_jogador.remove(bala)
                break

    for inimigo in inimigos:
        inimigo.movimentacao(player.x, player.y)

        if inimigo.rect.colliderect(player.rect):
            inimigo.morrer()
            inimigos.remove(inimigo)
            player.tomar_dano()

        inimigo.existir()

    for coletavel_vida in coletaveis_vida[:]:
        coletavel_vida.aparecer = True
        coletavel_vida.atualizar()
        if coletavel_vida.rect.colliderect(player.rect) and coletavel_vida.aparecer:
            player.recuperar_vida()
            coletaveis_vida.remove(coletavel_vida)
    for energetico in energeticos[:]:
        energetico.aparecer = True
        energetico.atualizar()
        if energetico.rect.colliderect(player.rect) and energetico.aparecer:
            player.tomar_energetico()
            energeticos.remove(energetico)
    pg.display.update()
