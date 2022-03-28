#
# CONVERTENDO SPRITESHEET AVLH
#
from PLSprite import ConverteSpriteSheet, AVLH, C_cima, C_baixo, C_esquerda, C_direita, Avatar
import pygame

pygame.init()
l, a = (500, 500)
tela = pygame.display.set_mode((l, a))
run = True

nora_spritesheet = pygame.image.load('imagem/AVLH/nora_spritesheet1.png')

nora_spritesheet = ConverteSpriteSheet(nora_spritesheet,
                                       3,
                                       4,
                                       AVLH,
                                       (90//4-5, 32)).converter()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_LCTRL]:
            run = False
    tela.fill((10, 20, 30))
    
    # exibindo o spritesheet gerado
    tela.blit(nora_spritesheet, (l//2, a//2))
    
    pygame.display.flip()
