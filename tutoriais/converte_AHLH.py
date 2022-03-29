#
# CONVERTENDO AHLH em AHLV
#
from PLSprite import ConverteSpriteSheet, AHLH
import pygame

pygame.init()
l, a = (500, 500)
tela = pygame.display.set_mode((l, a))
pygame.display.set_caption('Conversão de sprite AHLH')
run = True

# spritesheet AHLH com varios spritesheets
spritesheet_primo_mario = pygame.image.load('imagens/primo_mario_spritesheet.png')

# convertendo spritesheet AHLH para AHLV
spritesheet_primo_mario1 = ConverteSpriteSheet(
    spritesheet_primo_mario,
    3,
    3,
    AHLH,
    (50, 55), alfa=False).converter() # Para mais detalhes sobre os parâmetros leia as docstrings.

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    tela.fill((40, 40, 40))

    tela.blit(spritesheet_primo_mario, (10, 10)) # AHLH. O primeiro spritesheet é AHLH.
    tela.blit(spritesheet_primo_mario1, (l//2, 150)) # AHLV. O segundo spritesheet é AHLV, após a conversão.

    pygame.display.flip()
