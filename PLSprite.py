"""
┌───────────────────────────────────────────────┐
   ______   __    __   _        _    _   _    _
  |  __  \  \ \  / /  | |      | |  | | | |  | |
  | |__| |   \ \/ /   | |      | |  | | | |  | |
  | |____/    \  /    | |      | |  | | | |  | |
  | |         / /     | |____  | |__| | | |__| |
  |_|        /_/      |______| \______/ \______/
  Luís Henrique Alexandre dos S.
                      PyLuu of CnC(future Pit)
                        𝘼𝙣𝙮𝙤𝙣𝙚 𝙘𝙖𝙣 𝙙𝙚𝙫𝙚𝙡𝙤𝙥!
                           Pyluucatnet@gmail.com
└───────────────────────────────────────────────┘
"""

import pygame
from pygame.locals import *


print('I\'m PLSprite. Welcome!')


AHLV = 0
AHLH = 1
AVLH = 10
AVLV = 11

C_cima = 0
C_baixo = 1
C_esquerda = 10
C_direita = 11
C_lados = (C_cima, C_baixo, C_esquerda, C_direita)


def inverteh(sprites):
    """
       >>> Função responsável por inverter sprites na horizontal
             :sprites: Recebe uma lista/tupla com os sprites a serem invertidos na horizontal
             :return: Retorna uma lista dos sprites invertidos na horizontal
    """
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def invertev(sprites):
    """
       >>> Função responsável por inverter sprites na vertical
             :sprites: Recebe uma lista/tupla com os sprites a serem invertidos na vertical
             :return: Retorna uma lista dos sprites invertidos na vertical
    """
    return [pygame.transform.flip(sprite, False, true) for sprite in sprites]


class GerarSpriteSheet:
    """
    Classe responsável por gerar spritesheet
    
    # Forma de instanciar
    img1 = pygame.image.load('imagem/img1.png')
    img2 = pygame.image.load('imagem/img2.png')
    img3 = pygame.image.load('imagem/img3.png')
    
    img4 = pygame.image.load('imagem/img4.png')
    img5 = pygame.image.load('imagem/img5.png')
    img6 = pygame.image.load('imagem/img6.png')
    
    matriz_sprite = [[img1, img2, img3],
                     [img4, img5, img6]] # criando matriz de sprites
    
    meu_sprite = GerarSpriteSheet(matriz_sprite, 
                                  (100, 100),
                                  100,
                                  100,
                                  (100, 100),
                                  True).gerar()
    
    Estanciando a classe, lembre-se de utilizar o método gerar() para que ele retorne o spritesheet para o objeto meu_sprite
    """
    def __init__(self, 
                 matriz_sprites, 
                 dimensao_spritesheet, 
                 espaco_horizontal, 
                 espaco_vertical, 
                 dimensao_sprite=None, 
                 alfa=False):
        """
           Inicializando objeto
           
           :matriz_sprites: Uma matriz com cada sprite
           				Exemplo:
                                  [[img1, img2, img3],
                                   [img4, img5, img6],
                                   [img7, img8, img9]]
           				Contendo a imagem de todos os sprites que você deseja usar
           :dimensao_spritesheet: Recebe uma lista/tupla com as dimensões(largura, altura) do sprite
           :espaco_horizontal: Espaçamento horizontal entre os sprites
           :espaco_vertical: Espaçamento vertical entre os sprites
           :dimensao_sprite: Recebe uma lista/tupla com a nova dimensão(largura, altura) do sprite
           :alfa: Recebe um valor booleano. Se alfa == True os sprites tem o fundo com alfa
        """
        self.sprites = matriz_sprites
        self.dimensao = dimensao_spritesheet
        self.espacamento = (espaco_horizontal, espaco_vertical)
        self.dimensao_sprite = dimensao_sprite
        self.alfa = alfa
        self.cor_alvo = None
        self.spritesheet = None
    
    def gerar(self):
        """
        -> Método responsável por gerar o spritesheet
           :return: Retorna o spritesheet
        """
        self.spritesheet = pygame.Surface(self.dimensao)
        for i, linha in enumerate(self.sprites):
            for c, sprite in enumerate(linha):
                if self.dimensao_sprite:
                    sprite = pygame.transform.scale(sprite, self.dimensao_sprite)
                self.spritesheet.blit(sprite, (self.espacamento[0] * c, self.espacamento[1] * i))
            if self.alfa:
                self.cor_alvo = self.spritesheet.get_at((0, 0))
                self.spritesheet.set_colorkey(self.cor_alvo)
        return self.spritesheet


class FormatarSpriteSheet:
    pass


class AnimaSprites:
    """Classe responsável pela manipulação de spritesheets AHLV"""
    def __init__(self,
                 tela,
                 spritesheet,
                 teclas_controle,
                 largura,
                 altura,
                 p_img_x,
                 p_img_y,
                 x,
                 y,
                 num_animacao_h,
                 dimensao_sprite=None):
        """
        Inicializando objeto
        
        :tela: Recebe a superficie onde os sprites serão desenhados
        :spritesheet: Recebe o spritesheet que trabalharemos
        :teclas_controle: Recebe uma lista/tupla com as teclas de movimento do sprite
                        OBS.: As teclas devem ser passadas de acordo com a ordem do seu spritesheet
                        Exemplo:
                               Se o seu spritesheet tiver a primeira animação como andar para a esquerda 
                               a primeira tecla será responsável por ativar a animação da esquerda
        :largura: Recebe um valor do tipo int para definir a largura do sprite
        :altura: Recebe um valor do tipo int para definir a altura do sprite
        :p_img_X: Recebe um valor do tipo int para definir a posição x do sprite dentro do spritesheet
        :p_img_y: Recebe um valor do tipo int para definir a posição y do sprite dentro do spritesheet
        :x: Recebe um valor do tipo int para definir a posição x do sprite na superficie definida
        :y: Recebe um valor do tipo int para definir a posição y do sprite na superficie definida
        :num_animacao_h: Recebe um valor do tipo int, que é a quantidade de sprites na horizontal em uma mesma direção
        :dimensao_sprite: Recebe uma lista/tupla com a nova largura e altura do sprite
        """
        self.tela = tela
        self.spritesheet = spritesheet
        self.teclas_controle = teclas_controle
        self.largura = largura
        self.altura = altura
        self.p_img_x = p_img_x
        self.p_img_y = p_img_y
        self.x = x
        self.y = y
        self.num_animacao_h = num_animacao_h
        self.dimensao_sprite = dimensao_sprite
        self.atraso = 0
        self.velocidade_animacao = 0.1
        self.sprite_inicio = 0
        self.andar = False
        self.sprite_padrao_xy = (0, None)
    
    def iniciar(self):
        """Método responsável por iniciar a manipulação do spritesheet"""
        janela_avatar = pg.Surface((self.largura, self.altura))
        if self.dimensao_sprite:
            self.spritesheet = pg.transform.scale(self.spritesheet, self.dimensao_sprite)
        janela_avatar.blit(self.spritesheet, (0, 0), (self.p_img_x, self.p_img_y, self.largura, self.altura))
        self.tela.blit(janela_avatar, (self.x, self.y))
        self._controles()
    
    def _controles(self):
        """Método responsável por controlar as animações do sprite"""
        keys = pg.key.get_pressed()
        for i, key in enumerate(self.teclas_controle):
            if keys[key]:
                self.p_img_y = i * self.altura 
                self.andar = True
        if self.andar:
            self.atraso += 1
            if self.atraso > self.velocidade_animacao * 20: # definindo a velocidade da animação
                self.atraso = 0
                # cada vez que a p_img_x mais a largura da janela for menor que a largura do spritesheet ele pula para o proximo sprite
                if self.p_img_x + self.largura < self.num_animacao_h * self.largura:
                    self.p_img_x += self.largura
                else:
                    self.p_img_x = self.sprite_inicio * self.largura
                    self.animacao = 0
            self.andar = False
        else:
            self.p_img_x = self.sprite_padrao_xy[0]
            if self.sprite_padrao_xy[1]:
                self.p_img_y = self.sprite_padrao_xy[1]
    
    def set_sprite_inicio(self, num):
        """
        -> Método responsável por definir qual será o primeiro sprite após cada loop da animação
           :num: Recebe um valor, do tipo int, que define o p_img_x do primeiro sprite a ser exibido após cada loop da animação
        """
        self.sprite_inicio = num
    
    def set_posx(self, pos_x):
        """
        -> Método responsável por definir a posição x do sprite
           :pos_x: Recebe um valor, do tipo int, que será a nova posição x do sprite
        """
        self.x = pos_x
    
    def set_posy(self, pos_y):
        """
        -> Método responsável por definir a posição y do sprite
           :pos_y: Recebe um valor, do tipo int, que será a nova posição y do sprite
        """
        self.y = pos_y
    
    def set_sprite_padrao_xy(self, pos_xy):
        """
        -> Método responsável por definir a posição de repouso
           :pos_xy: Recebe uma lista/tupla com dois valores, posição x e posição y, caso queira definir 
                    somente uma das posições use None para invalidar a posição que não irá definir
           Exemplo: .set_sprite_padrao_xy([x, None]) # x, y
        """
        self.sprite_padrao_xy = pos_xy
    
    def set_velocidade_animacao(self, num):
        """
        -> Método responsável por definir a velocidade da animação
           :num: Recebe um valor, do tipo int, para definir a velocidade de transição da animação
        """
        self.velocidade_animacao = num
    
    def set_num_animacaoh(self, num):
        """
        -> Método responsável por definir a quatidade de sprites na horizontal
           :num: Recebe um valor do tipo int para definir quantos sprites há na horizontal
        """
        self.num_animacao_h = num
    
    def set_num_animacaov(self, num):
        """
        -> Método responsável por definir a quantidade de sprites na vertical
           :num: Recebe um valor do tipo int para definir quantos sprites há na vertical
        """
        self.num_animacao_v = num
    
    def get_dimensao_sprite(self):
        """
        -> Método responsável por retornar as dimensões do spritesheet em uso
           :return: Retorna uma lista/tupla com a largura e altura do spritesheet em uso
        """
        return self.sprite.get_rect()[2:]
    
    def get_posx(self):
        """
        -> Método responsável por retornar a posição x do sprite
           :return: Retorna um valor do tipo int da posição x do sprite
        """
        return self.x
    
    def get_posy(self):
        """
        -> Método responsável por retornar a posição y do sprite
           :return: Retorna um valor do tipo int da posição y do sprite
        """
        return self.y
    
    def get_velocidade_animacao(self):
        """
        -> Método responável por retornar a velocidade da animação
           :return: Retorna a velocidade da animação
        """
        return self.velocidade_animacao
    
    def get_num_animacaoh(self):
        """
        -> Método responsável por retornar o número de animações na horizontal
           :return: Retorna a quantidade de sprites na horizontal
        """
        return self.num_animacao_h


class Avatar:
    """
    Classe para manipulação de sprites padrão
    
    (v) Spritesheet AHLV(Animação na Horizontal e Lados na Vertical)
    """
    def __init__(self, tela,
                       spritesheet,
                       p_img_x,
                       p_img_y,
                       x,
                       y,
                       largura,
                       altura,
                       lado,
                       chave_lados,
                       animacao_h=False,
                       animacao_v=False,
                       num_animacao_h=0,
                       num_animacao_v=0,
                       dimensao=None):
        """
        Inicializando objeto
        
        :tela: Recebe uma superficie onde o sprite será desenhado
        :spritesheet: Recebe o sprite que vamos trabalhar
        :p_img_x: Recebe um valor do tipo int para a posição x do sprite dentro do spritesheet
        :p_img_y: Recebe um valor do tipo int para a posição y do sprite dentro do spritesheet
        :x: Recebe um valor do tipo int para a posição x do sprite na superficie
        :y: Recebe um valor do tipo int para a posição y do sprite na superficie
        :largura: Recebe um valor do tipo int para a largura do sprite
        :altura: Recebe um valor do tipo int para a altura do sprite
        :lado: Recebe uma chave de spritesheet
               Chaves existentes:
                   PLS.AHLV (Para animações na horizontal e lados na vertical)
                   PLS.AHLH (Para animaçõs na horizontal e lados na horizontal)
                   PLS.AVLH (Para animações na vertical e lados na horizontal)
                   PLS.AVLV (Para animações na vertical e lados na vertical)(Não disposível)
        :chave_lados: Recebe uma lista/tupla com chaves de direção de lados
                      Exemplo: [PLS.C_cima, PLS.C_baixo, PLS.C_esquerda, PLS.C_direita]
        :animacao_h: Recebe um valor booleano. Se as animações do spritesheet estiverem na horizontal animacao_h = True
        :animacao_v: Recebe um valor booleano. Se as animações do spritesheet estiverem na vertical animacao_v = True
        :num_animacao_h: Recebe um valor do tipo int para definir a quantidade de animações na horizontal do spritesheet
        :num_animacao_v: Recebe um valor do tipo int para definir a quantidade de animações na vertical do spritesheet
        :dimensao: Recebe uma lista/tupla com a largura e altura do sprite
        """
        self.tela = tela
        self.spritesheet = spritesheet
        self.p_img_x = p_img_x
        self.p_img_y = p_img_y
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.tipo_lado = lado
        self.chave_lados = chave_lados
        self.num_lado = len(self.chave_lados)
        self.num_animacao_h = num_animacao_h
        self.num_animacao_v = num_animacao_v
        self.dimensao_sprite = dimensao
        self.movimento = 1
        self.velocidade = 1
        self.atraso_animacao = 0
        self.pasos = 5
        self.acao_andando = False
        self.teclas_movimento = None
        self.avatar_visivel = True
        self.cor_fundo_avatar = (0, 0, 0)
    
    def _iniciar_sprite(self):
        """Método responsável por iniciar animação do spritesheet"""
        if self.avatar_visivel:
            if self.dimensao_sprite:
                self.sprite = pygame.transform.scale(self.spritesheet, self.dimensao_sprite)
            self.tela.blit(self.spritesheet, (self.x, self.y), (self.p_img_x, self.p_img_y, self.largura, self.altura))
        elif self.fundo_avatar:
            fundo_avatar = pygame.Surface((self.largura, self.altura))
            fundo_avatar.fill(self.cor_fundo_avatar)
            self.tela.blit(fundo_avatar, (self.x, self.y))
    
    def atualizar(self):
        """Método responsável por atualizar a animação do sprite"""
        self._iniciar_sprite()
        if self.dimensao_sprite:
            self.spritesheet = pygame.transform.scale(self.spritesheet, self.dimensao_sprite)
        rect_sprite = self.spritesheet.get_rect()
        if self.acao_andando: # se o sprite tiver em movimento ou definido para loop infinito
            if self.atraso_animacao > (20 * self.velocidade):
                # se movimento dividido por largura do avatar for igual
                # ao numero de sprites na horizontal volta mostrar o inicio da sprite
                if self.movimento // self.largura == self.num_animacao_h - 1:
                    self.movimento = 1
                else: # atualizando sprite
                    self.movimento += self.largura
                    self.p_img_x = self.movimento
                self.atraso_animacao = 0
        self.atraso_animacao += 1
    
    def controles(self, teclas, pasos=None):
        """
        -> Método responsável por controlar o movimento do sprite
           :teclas: Recebe uma lista/tupla com as chaves de movimento
                    Exemplo: (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
           :pasos: Se pasos não for definido recebe None e a velocidade será padrão
        """
        if pasos:
            self.pasos = pasos
        tecla = pygame.key.get_pressed()
        self.acao_andando = False
        if self.teclas_movimento: # teclas de movimento personalizada
            for c in range(4):
                if tecla[self.teclas_movimento[c]]:
                    if self.tipo_lado == AHLV:
                        self.p_img_y = self.altura * c
                        if self.chave_lados[c] == C_cima:
                            self.y -= self.pasos
                            self.acao_andando = True
                        elif self.chave_lados[c] == C_baixo:
                            self.y += self.pasos
                            self.acao_andando = True
                        if self.chave_lados[c] == C_esquerda:
                            self.x -= self.pasos
                            self.acao_andando = True
                        elif self.chave_lados[c] == C_direita:
                            self.x += self.pasos
                            self.acao_andando = True
        else:
            self.teclas_movimento = teclas
    
    def set_posx(self, pos_x):
        """
        -> Método responsável por definir a posição x do sprite
           :pos_x: Recebe um valor do tipo int que define a posição x do sprite
        """
        self.x = pos_x
    
    def set_posy(self, pos_y):
        """
        -> Método responsável por definir a posição y do sprite
           :pos_y: Recebe um valor do tipo int que define a posição y do sprite
        """
        self.y = pos_y
    
    def set_num_animacaoh(self, num_animacao):
        """
        -> Método responsável por definir o número de animações na horizontal
           :num_animacao: Recebe um valor do tipo int que define quantos sprites há na horizontal
        """
        self.num_animacao_h = num_animacao
    
    def set_num_animacaov(self, num_animacao):
        """
        -> Método responsável por definir o número de animações na vertical
           :num_animacao: Recebe um valor do tipo int que define quantos sprites há na vertical
        """
        self.num_animacao_v = num_animacao
    
    def set_imgx(self, pos_x):
        """
        -> Método responsável por definir a posição X da imagem dentro do spritesheet
           :pos_x: Recebe um valor int para definir a posição x do sprite
        """
        self.p_img_x = pos_x * self.largura
    
    def set_imgy(self, pos_y):
        """
        -> Método responsável por definir a posição Y da imagem dentro do spritesheet
           :pos_y: Recebe um valor int para definir a posição y do sprite
        """
        self.p_img_y = pos_y * self.altura
    
    def set_janelah(self, largura):
        """
        -> Método responsável por definir o comprimento da janela do sprite na horizontal
           :largura: Recebe um valor do tipo int que define a largura da janela
        """
        self.largura = largura
    
    def set_janelav(self, altura):
        """
        -> Método responsável por definir o comprimento da janela do sprite na vertical
           :altura: Recebe um valor do tipo int que define a altura da janela
        """
        self.altura = altura
    
    def set_dimensao_sprite(self, l_a):
        """
        -> Método responsável por definir nova dimensão do sprite
           :l_a: Recebe uma lista/tupla com a nova dimensão do sprite
        """
        self.dimensao_sprite = l_a
    
    def set_avatar_visivel(self, visivel, fundo_avatar=False, cor_fundo=(0, 0, 0)):
        """
        -> Método responsável por definir se o avatar ficará visível
           :visivel: Recebe um valor booleano
                     True visível
                     False invisível
           :fundo_avatar: Recebe um valor booleano. Se True, ficará uma quadrado no local do sprite
           :cor_fundo: Recebe uma lista/tupla com 3 valores para RGB
                       Se fundo_avatar não for definido a cor padrão é preto
        """
        if visivel:
            self.avatar_visivel = True
        else:
            if fundo_avatar:
                self.fundo_avatar = True
            else:
                self.fundo_avatar = False
            self.cor_fundo_avatar = cor_fundo
            self.avatar_visivel = False
    
    def set_acao(self, ativo):
        """
        -> Método responsável por definir o estado da animação
           :ativo: Recebe um valor booleano. Se ativo = True a animação ficará sempre ativa
        """
        self.acao_andando = ativo
    
    def set_velocidade(self, velocidade):
        """
        -> Método responsável por definir a velocidade da animação
           :velocidade: Recebe um valor int/float que define o atraso da animação
        """
        self.velocidade = velocidade
    
    def set_teclas(self, teclas):
        """
        -> Método responsável por definir teclas de movimento
           :teclas: Passe uma lista/tupla com os botões de controle na seguinte ordem:
                  Para cima     exemplo: pygame.K_w
                  Para baixo    exemplo: pygame.K_s
                  Para esquerda exemplo: pygame.K_a
                  Para direita  exemplo: pygame.K_d
        """
        self.teclas_movimento = teclas
    
    def set_pasos(self, pasos):
        """
        -> Método responsável por definir a velocidade de pasos do avatar
           :pasos: Recebe um valor int que define a velocidade do movimento do sprite
        """
        self.pasos = pasos
    
    def get_sprite_atual(self):
        """Método responsável por retornar o index do sprite atual"""
        return self.movimento // self.largura
    
    def get_posx(self):
        """Método responsável por retornar a posição x do sprite"""
        return self.x
    
    def get_posy(self):
        """Método respionsável por retornar a posição y do sprite"""
        return self.y
    
    def get_avatar_visivel(self):
        """
        -> Método responsável por retornar o estado do sprite
           :return: Retorna o estado do sprite
                               True se for visível
                               False se for invísivel
        """
        return self.avatar_visivel
    
    def get_velocidade(self):
        """Método responsável por retorna a velocidade da animação"""
        return self.velocidade
    
    def get_teclas(self):
        """Método responsável por retornar teclas de movimento atual"""
        return self.teclas_movimento
    
    def get_imgx(self):
        """Método responsável por retornar a posição x do sprite dentro do spritesheet"""
        return self.p_img_x
    
    def get_imgy(self):
        """Método responsável por retornar a posição y do sprite dentro do spritesheet"""
        return self.p_img_y
    
    def get_janelah(self):
        """Método responsável por retornar a largura da janela de exibição do sprite"""
        return self.largura
    
    def get_janelav(self):
        """Método responsável por retornar a altura da janela de exibição do sprite"""
        return self.altura
    
    def get_num_animacaoh(self):
        """
        -> Método responsável por retornar o número de animações na horizontal
           OBS.: Se as animações do sprite estiverem na vertical este método retornará 0
        """
        return self.num_animacao_h
    
    def get_num_animacaov(self):
        """
        -> Método responsável por retornar o número de animações na vertical
           OBS.: Se as animações do sprite estiverem na horizontal este método retornará 0
        """
        return self.num_animacao_v
    
    def get_dimensao_sprite(self):
        """Método responsável por retornar uma tupla com a dimensão(largura e altura) do sprite"""
        if self.dimensao_sprite:
            return self.dimensao_sprite
        return self.spritesheet.get_rect()[-2:]
        
    def get_acao(self):
        """
        -> Método responsável por retornar o estado do sprite
           :return: Retorna um valor booleano.
                    True se estiver em movimento
                    False se estiver parado
        """
        return self.acao_andando
    
    def get_pasos(self):
        """Método responsável por retornar o valor atual de pasos"""
        return self.pasos
