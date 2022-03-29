import PLSprite as PLS
import pygame as pg

pg.init()
l, a = (500, 500) # largura, altura
pg.display.set_caption('Criando Avatar') # nomeando janela
tela = pg.display.set_mode((l, a)) # criando janela
run = True

adao_spritesheet = pg.image.load('imagens/adao_spritesheet.png')

# Instanciando a classe
adao = PLS.Avatar(
    tela=tela,
    spritesheet=adao_spritesheet,
    p_img_x=0,
    p_img_y=0,
    x=0,
    y=0,
    largura=60,
    altura=60,
    chave_lados=PLS.C_lados,
    num_animacao_h=9)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    tela.fill((10, 20, 30))

    adao.atualizar() # método atualizar() atualiza a animação do sprite

    pg.display.flip()