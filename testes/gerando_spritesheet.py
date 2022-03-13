# A classe GerarSpriteSheet é responsável por pegar uma matriz de sprites e retornar
# uma spritesheet

import pygame as pg
from PLSprite import GerarSpriteSheet, inverteh

pg.init()
LARGURA, ALTURA = (1050, 550)
tela = pg.display.set_mode((LARGURA, ALTURA))
run = True

# primeiro usando o pygame pegaremos as fotos desejadas
naruto_correndo_direita1 = pg.image.load('imagem/correndo/naruto_correndo1.bmp')
naruto_correndo_direita2 = pg.image.load('imagem/correndo/naruto_correndo2.bmp')
naruto_correndo_direita3 = pg.image.load('imagem/correndo/naruto_correndo3.bmp')
naruto_correndo_direita4 = pg.image.load('imagem/correndo/naruto_correndo4.bmp')
naruto_correndo_direita5 = pg.image.load('imagem/correndo/naruto_correndo5.bmp')
naruto_correndo_direita6 = pg.image.load('imagem/correndo/naruto_correndo6.bmp')
naruto_correndo_direita7 = pg.image.load('imagem/correndo/naruto_correndo7.bmp')
naruto_correndo_direita8 = pg.image.load('imagem/correndo/naruto_correndo8.bmp')
# tupla com todos os sprites em ordem
naruto_correndo_direita = (naruto_correndo_direita1, naruto_correndo_direita2,
                           naruto_correndo_direita3, naruto_correndo_direita4,
                           naruto_correndo_direita5, naruto_correndo_direita6,
                           naruto_correndo_direita7, naruto_correndo_direita1)
# como podemos observar so tenho imagens do naruto correndo para a direita mais com a funçao inverth() posso inverter os sprites para esquerda e assim obter ele correndo para direita e esquerda
naruto_correndo_esquerda = inverteh(naruto_correndo_direita) # inverteh() retorna uma lista dos sprites invertidos horizontalmente

naruto_correndo = (naruto_correndo_direita,
                   naruto_correndo_esquerda) # matriz de sprites

# para mais informações leia as docstrings da classe
naruto_spritesheet = GerarSpriteSheet(matriz_sprites=naruto_correndo,
                                      dimensao_spritesheet=(800, 200),
                                      espaco_horizontal=100,
                                      espaco_vertical=100,
                                      dimensao_sprite=(100, 100),
                                      alfa=True).gerar()

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    tela.fill((0, 0, 0))
    tela.blit(naruto_spritesheet, (0, ALTURA // 2 - 100)) # exibindo spritesheet gerado na tela
    
    pg.display.flip()
