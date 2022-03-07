import PLSprite as PLS
import pygame as pg

pg.init() # Inicializando o Pygame
largura = altura = 500 # dimensões da janela
janela = pg.display.set_mode((largura, altura)) # criando janela
adao_spritesheet = pg.image.load('imagens/adao_andando.png') # pegando a imagem do meu spritesheet
run = True # estado do programa

# criando objeto
adao = PLS.Avatar(janela,
              adao_spritesheet,
              0,
              130,
              largura//2,
              altura//2,
              60,
              60,
              (0, 130, 65, 190),
              animacao_h=True,
              num_animacao_h=9)

while run:
    for event in pg.event.get(): # verificando lista de eventos do Pygame
        if event.type == pg.QUIT: # ao clicar para fechar a janela o event.type sera QUIT
            run = False # estado do programa recebe False
  
    janela.fill((0, 0, 0)) # após cada loop preenche a janela com a cor RGB: (0, 0, 0), ou seja, preto
    adao.atualizar() # fará com que o seu sprite seja desenhado na janela
  
    pg.display.flip() # após cada loop atualiza a janela
