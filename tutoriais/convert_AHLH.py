#
# CONVERTENDO AHLH em AHLV
#
from PLSprite import ConverteSpriteSheet, AHLV, AHLH
import pygame

pygame.init()
l, a = (1050, 550)
tela = pygame.display.set_mode((l, a))
run = True
# spritesheet AHLH com varios spritesheets
spritesheet_primo_mario = pygame.image.load('imagem/AHLH/primo_mario_andando.png') # 3 lados

# convertendo spritesheet AHLH para AHLV
spritesheet_primo_mario1 = ConverteSpriteSheet(spritesheet_primo_mario,
                                              3,
                                              3,
                                              AHLH,
                                              (60, 84),
                                              d_spritesheet=(500, 500)).converter()

spritesheet_primo_mario2 = ConverteSpriteSheet(spritesheet_primo_mario,
                                               3,
                                               3,
                                               AHLH,
                                               (60, 84),
                                               index_spritesheet_v=3,
                                               d_spritesheet=(500, 500)).converter()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    tela.fill((40, 40, 40))
    
    tela.blit(spritesheet_primo_mario1, (l//2, 100)) # exibindo spritesheet do index 0
    tela.blit(spritesheet_primo_mario2, (l//2+200, 100)) # exibindo spritesheet do index 2
        
    pygame.display.flip()
