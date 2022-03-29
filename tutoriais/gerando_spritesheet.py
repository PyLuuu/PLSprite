#
# GERANDO UM SPRITESHEET AHLV
#
from PLSprite import GerarSpriteSheet, inverteh
import pygame as pg

pg.init()
l, a = (1000, 600)
pg.display.set_caption('Gerando um spritesheet')
tela = pg.display.set_mode((l, a))
run = True

# importando meus sprites
naruto1_dir = pg.image.load('imagens/naruto_sprites/naruto_correndo1.bmp')
naruto2_dir = pg.image.load('imagens/naruto_sprites/naruto_correndo2.bmp')
naruto3_dir = pg.image.load('imagens/naruto_sprites/naruto_correndo3.bmp')
naruto4_dir = pg.image.load('imagens/naruto_sprites/naruto_correndo4.bmp')
naruto5_dir = pg.image.load('imagens/naruto_sprites/naruto_correndo5.bmp')
naruto6_dir = pg.image.load('imagens/naruto_sprites/naruto_correndo6.bmp')
naruto7_dir = pg.image.load('imagens/naruto_sprites/naruto_correndo7.bmp')
naruto8_dir = pg.image.load('imagens/naruto_sprites/naruto_correndo8.bmp')
# criando lista com sprites indo para direita
naruto_sprites_dir = [naruto1_dir, naruto2_dir, naruto3_dir, naruto4_dir, naruto5_dir, naruto6_dir, naruto7_dir, naruto8_dir]
# criando lista com sprites indo para esquerda
naruto_sprites_esq = inverteh(naruto_sprites_dir) # a funçao inverteh() inverte horizontalmente os sprites

# criando a matriz de sprites
matriz_sprites_naruto = [
    naruto_sprites_dir,
    naruto_sprites_esq
    ]

# instanciando a classe
naruto_spritesheet = GerarSpriteSheet(
    matriz_sprites=matriz_sprites_naruto, 
    dimensao_spritesheet=(800, 200), 
    espaco_horizontal=100, 
    espaco_vertical=100, 
    dimensao_sprite=(100, 100), 
    alfa=True).gerar() # ao final use o metodo gerar() para que o objeto naruto_spritesheet receba o spritesheet pronto
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    tela.fill((10, 20, 30))

    tela.blit(naruto_spritesheet, (100, 100)) # exibindo spritesheet pronto 
    # OBS.: A classe GerarSpriteSheet gera apenas spritesheets AHLV

    pg.display.flip()
