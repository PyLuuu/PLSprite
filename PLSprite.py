"""
┌───────────────────────────────────────────────┐
   ______   __    __   _        _    _   _    _
  |  __  \  \ \  / /  | |      | |  | | | |  | |
  | |__| |   \ \/ /   | |      | |  | | | |  | |
  | |____/    \  /    | |      | |  | | | |  | |
  | |         / /     | |____  | |__| | | |__| |
  |_|        /_/      |______| \______/ \______/
   LS                 PyLuu of CnC(future Pit)
                        𝘼𝙣𝙮𝙤𝙣𝙚 𝙘𝙖𝙣 𝙙𝙚𝙫𝙚𝙡𝙤𝙥!
                        Anyone can develop!
                          Pyluucatnet@gmail.com
└───────────────────────────────────────────────┘
"""

import pygame
from pygame.locals import *


print('I\'m PLSprite. Welcome!')

class FormasGeometricas:
    """Classe responsável por desenhar formas geométricas"""
    pass


class GerarSpriteSheet:
    """
    Classe responsável por gerar spritesheet
    
    Forma de instanciar
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
    
    Assim se instancia a classe lembre-se de utilizar o método gerar() para que ele retorne o spritesheet para o objeto meu_sprite
    """
    def __init__(self, 
                 matriz_sprites, 
                 dimensao, 
                 espaco_horizontal, 
                 espaco_vertical, 
                 dimensao_sprite=None, 
                 alfa=False):
        """
        -> Método construtor
           :matriz_sprites: Uma matriz com cada sprite
           				Exemplo:
           								[[img1, img2, img3],
           								 [img4, img5, img6],
           								 [img7, img8, img9]]
           				Contendo a imagem de todos os sprites que você deseja usar
           :dimensao: Recebe uma lista/tupla com as dimensões(largura, altura) do avatar
           :espaco_horizontal: Espaçamento horizontal entre os sprites
           :espaco_vertical: Espaçamento vertical entre os sprites
           :dimensao_sprite: Recebe uma lista/tupla com a nova dimensão(largura, altura) do sprite
           :alfa: Recebe um valor booleano. Se alfa == True os sprites tem o fundo com alfa
        """
        self.sprites = matriz_sprites
        self.dimensao = dimensao
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
            self.cor_alvo = self.spritesheet.get_at((0, 0))
            self.spritesheet.set_colorkey(self.cor_alvo)
        return self.spritesheet


class SpritesDiversos:
    '''
    Classe para manipulação de tipos diferentes de sprites
    
    Tipos de sprites usados pela classe:
        (v) Sprite com animações e lados na horizontal
        
        (v) Sprite com animação na vertical e lados na horizontal
        
        (x) Sprite com animação e lados na vertical (em breve)
    '''
    def __init__(self, 
                 tela, 
                 sprite, 
                 p_img_x, 
                 p_img_y, 
                 x, 
                 y, 
                 largura, 
                 altura, 
                 lados,
                 animacao_h=False,
                 animacao_v=False,
                 num_animacao_h=0,
                 num_animacao_v=0):
        '''
        Inicializando objeto
        
        :param tela: Recebe a interface onde será desenhado o avatar
        :param sprite: Recebe o sprite que iremos trabalhar
        :param p_img_x: Recebe a posição X da primeira imagem dentro do sprite
        :param p_img_y: Recebe a posição Y da primeira imagem dentro do sprite
        :param x: Recebe a posição X do avatar
        :param y: Recebe a posição Y do avatar
        :param largura: Recebe a largura do avatar
        :param altura: Recebe a altura do avatar
        :param lados: Recebe uma lista/tupla com os lados da sprite
                      Exemplo:
                             (0, 45, 90, 135)
                             0   = cima
                             45  = baixo
                             90  = esquerda
                             135 = direita
                      OBS.: Se o seu sprite so tiver dois lados como cima e baixo
                            (0, 45, None, None)
                            0    = cima
                            45   = baixa
                            None = seria esquerda
                            None = seria direita
                            Nesse caso você poderia utilizar (0, 45)
                            
                            Caso o seu sprite só tenha os lados esquerda e direita
                            (None, None, 0, 45)
                            Se não houver None ele irá usar 0 como cima e 45 como baixo
        :param animacao_h: Recebe um valor booleano. Se as animações(andar, pular entre outros)
                           do seu sprite estiverem na horizontal animacao_h deve receber True
        :param animacao_v: Recebe um valor booleano. Se as animações(andar, pular entre outros)
                           do seu sprite estiverem na vertical animacao_v deve receber True
        :param num_animacao_h: Número de animações no sprite na horizontal
        :param num_animacao_v: Número de animações no sprite na vertical
        '''
        self.tela = tela
        self.sprite = sprite
        self.p_img_x = p_img_x
        self.p_img_y = p_img_y
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.lados = lados
        self.animacao_h = animacao_h
        self.animacao_v = animacao_v
        self.num_animacao_h = num_animacao_h
        self.num_animacao_v = num_animacao_v
        self.movimento_avatar = 1
        self.pasos = 5
        self.andando = False
        self.animacao_padrao = None
        self.cont_animacao = 0
        self.lado_atual = 1
        self.avatar_visivel = True
        self.fundo_avatar = False
        self.cor_fundo_avatar = (0, 0, 0)
    
    def avatar(self, dimensao=None):
        '''
        -> Método responsável por criar o avatar
           :param dimensao: Recebe uma lista/tupla com a nova dimensão(largura, altura) do sprite 
           :return: Sem retorno
        '''
        if dimensao:
            self.sprite = pygame.transform.scale(self.sprite, dimensao)
        if self.avatar_visivel:
            self.tela.blit(self.sprite, (self.x, self.y), (self.p_img_x, self.p_img_y, self.largura, self.altura))
        elif self.fundo_avatar:
            fundo_avatar = pygame.Surface((self.largura, self.altura))
            fundo_avatar.fill(self.cor_fundo_avatar)
            self.tela.blit(fundo_avatar, (self.x, self.y))
    
    def d_animacao(self, acao=False, velocidade=1):
        '''
        -> Método responsável por fazer a animação do sprite
           :param acao: Recebe um valor booleano. Se acao = True a animação nunca ficará parada
           :param velocidade: Recebe um valor inteiro. Definir a velocidade da animação
        '''
        if acao or self.andando:
            if self.animacao_h: # se as animações do sprite forem na horizontal
                self.cont_animacao += 1
                if self.cont_animacao < self.num_animacao_h:
                    self.movimento_avatar += self.largura
                    self.p_img_x = self.movimento_avatar
                else:
                    self.p_img_x = self.movimento_avatar = self.lado_atual
                    self.andando = False
                    self.cont_animacao = 0
            elif self.animacao_v: # se as animações do sprite forem na vertical
                if self.movimento_avatar // self.altura == 1:
                    self.p_img_y = self.movimento_avatar = 1
                    self.andando = False
                else:
                    self.movimento_avatar += self.altura
                    self.p_img_y = self.movimento_avatar
        else:
            if self.animacao_padrao:
                if self.animacao_v:
                    self.p_img_y = self.animacao_padrao[1]
                elif self.animacao_h:
                    self.p_img_x = self.animacao_padrao[0]
        pygame.time.delay(velocidade * 50)
    
    def d_controles(self, teclas, inclinacao=None):
        '''
        -> Método responsável por controlar o avatar
           :param teclas: Recebe uma lista/tupla contendo as teclas de controle
                          As teclas devem ser passadas na seguinte ordem:
                          OBS.: Teclas usadas como exemplo
                                             (w) Andar p/ cima
                                             (s) Andar p/ baixo
                         [ q ]     [ e ]     (a) Andar p/ esquerda
                             \[ w ]/         (d) Andar p/ direita
                          [ a ]( )[ d ]      (q) Andar p/ canto superior esquerdo
                             /[ s ]\         (e) Andar p/ canto superior direito
                         [ z ]     [ x ]     (z) Andar p/ canto inferior esquerdo
                                             (x) Andar p/ canto inferior direito
                          Exemplo:
                                 (K_w, K_s, K_a, K_d)
                                 [K_UP, K_DOWN, K_LEFT, K_RIGHT]
                                 Caso sua sprite só tenha dois lados como esquerda e direita 
                                 [None, None, K_a, K_d]
                                 Passe as teclas na mesma ordem usando None para 
                                 invalidar os lados que não estão no seu sprite
        '''
        tecla = pygame.key.get_pressed()
        for n in range(len(teclas)):
            if teclas[n] is None:
                pass
            else:
                if n == 0 and tecla[teclas[0]]: # andar para cima
                    self.andando = True
                    self.y -= self.pasos
                    if self.animacao_v:
                        self.p_img_x = self.lados[0]
                    elif self.animacao_h:
                        self.lado_atual = self.lados[0]
                        self.p_img_y = self.lados[0] # se os lados estiverem na vertical
                
                elif n == 1 and tecla[teclas[1]]: # andar para baixo
                    self.andando = True
                    self.y += self.pasos
                    if self.animacao_v:
                        self.p_img_x = self.lados[1]
                    elif self.animacao_h:
                        self.lado_atual = self.lados[1]
                        self.p_img_y = self.lados[1] # lados na vertical
                
                elif n == 2 and tecla[teclas[2]]: # andar para a esquerda
                    self.andando = True
                    self.x -= self.pasos
                    if self.animacao_v:
                        self.p_img_x = self.lados[2]
                    elif self.animacao_h:
                        self.lado_atual = self.lados[2]
                        self.p_img_y = self.lados[2] # lados na vertical
                
                elif n == 3 and tecla[teclas[3]]: # andar para direita
                    self.andando = True
                    self.x += self.pasos
                    if self.animacao_v:
                        self.p_img_x = self.lados[3]
                    elif self.animacao_h:
                        self.lado_atual = self.lados[3]
                        self.p_img_y = self.lados[3] # lados na vertical
                
                elif n == 4 and tecla[teclas[4]]: # andar para canto superior esquerdo
                    self.andando = True
                    if inclinacao:
                        if len(inclinacao) > 1: # definindo a velocidade da inclinacao x,y
                            self.x -= inclinacao[0]
                            self.y -= inclinacao[1]
                        else:
                            self.x -= inclinacao
                            self.y -= inclinacao
                    if self.animacao_v:
                        self.p_img_x = self.lados[4]
                    elif self.animacao_h:
                        self.lado_atual = self.lados[4]
                        self.p_img_y = self.lados[4] # lados na vertical
                
                elif n == 5 and tecla[teclas[5]]: # andando para canto superior direito
                    self.andando = True
                    if len(inclinacao) > 1: # definindo inclinacao x,y
                        self.x += inclinacao[0]
                        self.y -= inclinacao[1]
                    else:
                        self.x += inclinacao
                        self.y -= inclinacao
                    if self.animacao_v:
                        self.p_img_x = self.lados[5]
                    elif self.animacao_h:
                        self.lado_atual = self.lados[5]
                        self.p_img_y = self.lados[5]
                
                elif n == 6 and tecla[teclas[6]]: # andar para canto inferior esquerdo
                    self.andando = True
                    if len(inclinacao) > 1:
                        self.x -= inclinacao[0]
                        self.y += inclinacao[1]
                    else:
                        self.x -= inclinacao
                        self.y += inclinacao
                    if self.animacao_v:
                        self.p_img_x = self.lados[6]
                    elif self.animacao_h:
                        self.lado_atual = self.lados[6]
                
                elif n == 7 and tecla[teclas[7]]: # andar para canto inferior direito
                    self.andando = True
                    if len(inclinacao) > 1:
                        self.x += inclinacao[0]
                        self.y += inclinacao[1]
                    else:
                        self.x += inclinacao
                        self.y += inclinacao
                    if self.animacao_v:
                        self.p_img_x = self.lados[7]
                    elif self.animacao_h:
                        self.lado_atual = self.lados[7]
    
    def set_animacao_inatividade(self, p_img_xy):
        '''
        -> Método responsável por definir qual será o sprite de inatividade
           :param p_img_xy: Recebe uma lista/tupla com a posição de x e y
                                              OBS.: personagem_imagem_xy
        '''
        self.animacao_padrao = p_img_xy


class Avatar(SpritesDiversos):
    '''
    Classe para manipulação de sprites padrão
    
    (v) Animação na horizontal e lados na vertical
    '''
    def __init__(self, tela, 
                       sprite, 
                       p_img_x, 
                       p_img_y, 
                       x, 
                       y, 
                       largura, 
                       altura, 
                       lados, 
                       animacao_h=False,
                       animacao_v=False,
                       num_animacao_h=0,
                       num_animacao_v=0,
                       dimensao=None):
        super().__init__(tela, 
                         sprite, 
                         p_img_x,
                         p_img_y,
                         x,
                         y,
                         largura,
                         altura,
                         lados,
                         animacao_h,
                         animacao_v,
                         num_animacao_h,
                         num_animacao_v)
        self.tela = tela
        self.sprite = sprite
        self.p_img_x = p_img_x
        self.p_img_y = p_img_y
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.num_animacao_h = num_animacao_h
        self.num_animacao_v = num_animacao_v
        self.coords_lados = lados
        self.dimensao_sprite = dimensao
        self.movimento = 1
        self.velocidade = 1
        self.atraso_animacao = 0
        self.pasos = 5
        self.acao_parado = False
        self.teclas_movimento = None
        self.avatar_visivel = True
        self.cor_fundo_avatar = (0, 0, 0)
    
    def _gerar_corpo(self):
        '''Método responsável por criar corpo do avatar'''
        if self.avatar_visivel:
            if self.dimensao_sprite:
                self.sprite = pygame.transform.scale(self.sprite, self.dimensao_sprite)
            self.tela.blit(self.sprite, (self.x, self.y), (self.p_img_x, self.p_img_y, self.largura, self.altura))
        elif self.fundo_avatar:
            fundo_avatar = pygame.Surface((self.largura, self.altura))
            fundo_avatar.fill(self.cor_fundo_avatar)
            self.tela.blit(fundo_avatar, (self.x, self.y))
    
    def _acao(self):
        '''Método responsável por verificar se o usuário pressionou alguma tecla de movimento'''
        tecla = pygame.key.get_pressed()
        if self.teclas_movimento:
            if tecla[self.teclas_movimento[0]] or tecla[self.teclas_movimento[1]] or tecla[self.teclas_movimento[2]] or tecla[self.teclas_movimento[3]]:
                self.acao_andando = True
            else:
                self.acao_andando = False
                if self.animacao_padrao:
                    self.p_img_x = self.animacao_padrao[0]
                    if self.animacao_padrao[1]:
                        self.p_img_y = self.animacao_padrao[1]
        else:
            if tecla[K_w] or tecla[K_s] or tecla[K_a] or tecla[K_d]:
                self.acao_andando = True
            else:
                self.acao_andando = False
                if self.animacao_padrao:
                    self.p_img_x = self.animacao_padrao[0]
                    if self.animacao_padrao[1]:
                        self.p_img_y = self.animacao_padrao[1]
    
    def atualizar(self):
        '''Método responsável por atualizar a animação do avatar'''
        self._gerar_corpo()
        self._acao() # verificando se há alguma tecla de movimento sendo pressionada
        if self.dimensao_sprite:
            self.sprite = pygame.transform.scale(self.sprite, self.dimensao_sprite)
        rect_sprite = self.sprite.get_rect()
        if self.acao_parado or self.acao_andando:
            if self.atraso_animacao >= (10 * self.velocidade):
                # se movimento dividido por largura do avatar for igual
                # ao numero de sprites na horizontal volta mostrar o inicio da sprite
                if self.movimento // self.largura == self.num_animacao_h - 1:
                    self.movimento = 1
                else: # atualizando sprite
                    self.movimento += self.largura
                    self.p_img_x = self.movimento
                self.atraso_animacao = 0
        else:
            self.movimento = 1
            if self.animacao_padrao:
                self.movimento = self.animacao_padrao[0]
            self.p_img_x = self.movimento
        #pygame.time.delay(self.velocidade * 50) # definindo delay da animação
        self.atraso_animacao += 1
    
    def controles(self, pasos=None):
        '''
        -> Método responsável por controlar o movimento do avatar
           :param pasos: Se pasos não for definido recebe None e a velocidade será padrão
        Info:
            Teclas de movimento(padrão)
                W = andar para cima
                S = andar para baixo
                A = andar para esquerda
                D = andar para direita
        '''
        if pasos:
            self.pasos = pasos
        tecla = pygame.key.get_pressed()
        # sprites com animaçao na horizontal e lados na vertical
        if self.teclas_movimento:
            # teclas de movimento personalizada
            if tecla[self.teclas_movimento[0]]: # andar para cima
                self.p_img_y = self.coords_lados[0]
                self.y -= self.pasos
            elif tecla[self.teclas_movimento[1]]: # andar para baixo
                self.p_img_y = self.coords_lados[1]
                self.y += self.pasos
            elif tecla[self.teclas_movimento[2]]: # andar para esquerda
                self.p_img_y = self.coords_lados[2]
                self.x -= self.pasos
            elif tecla[self.teclas_movimento[3]]: # andar para direita
                self.p_img_y = self.coords_lados[3]
                self.x += self.pasos
        else:
            # teclas de movimento padrão
            if tecla[K_w]:
                self.p_img_y = self.coords_lados[0]
                self.y -= self.pasos
            elif tecla[K_s]:
                self.p_img_y = self.coords_lados[1]
                self.y += self.pasos
            if tecla[K_a]:
                self.p_img_y = self.coords_lados[2]
                self.x -= self.pasos
            elif tecla[K_d]:
                self.p_img_y = self.coords_lados[3]
                self.x += self.pasos
    
    def set_num_animacaoh(self, num):
        """Método responsável por definir o número de animações na horizontal"""
        self.num_animacao_h = num
    
    def set_num_animacaov(self, num):
        """Método responsável por definir o número de animações na vertical"""
        self.num_animacao_v = num
    
    def set_imgx(self, pos_x):
        """Método responsável por definir a posição X da imagem dentro do spritesheet"""
        self.p_img_x = pos_x
    
    def set_imgy(self, pos_y):
        """Método responsável por definir a posição Y da imagem dentro do spritesheet"""
        self.p_img_y = pos_y
    
    def set_janelah(self, num):
        """Método responsável por definir o comprimento da janela do sprite na horizontal"""
        self.largura = num
    
    def set_janelav(self, num):
        """Método responsável por definir o comprimento da janela do sprite na vertical"""
        self.altura = num
    
    def set_dimensao(self, l_a):
        """
        -> Método responsável por definir nova dimensão do sprite
           :l_a: Recebe uma lista/tupla com dois valores Largura e Altura
        """
        self.dimensao_sprite = l_a
    
    def set_avatar_visivel(self, visivel, fundo_avatar=False, cor_fundo=(0, 0, 0)):
        '''
        -> Método responsável por definir se o avatar ficará visível
           :param visivel: Recebe valores booleanos 
                                  True visível
                                  False invisível
           :param fundo_avatar: Recebe um valor booleano. Se True aparecerá um quadrado na posição onde o avatar está
           :param cor_fundo: Recebe uma tupla/lista com 3 valores para RGB
                             Se fundo_avatar não for definido este parâmetro não precisa ser passado
           :return: Sem retorno
        '''
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
        '''
        -> Método responsável por definir o estado da animação
           :param ativo: True ou False. Se ativo = True a animação ficará ativa mesmo sem o usuário pressionar teclas de movimento
           :return: Sem retorno
        '''
        if ativo is True:
            self.acao_parado = ativo
    
    def set_velocidade(self, velocidade):
        '''
        -> Método responsável por definir a velocidade da animação
           :param velocidade: Recebe um valor int/float que define o atraso da animação
                              Aceita valores entre 0 e 1, com somente uma casa decimal.
           :return: Sem retorno
        '''
        if 0 < velocidade <= 1:
            self.velocidade = velocidade
        else:
            self.velocidade = 1
    
    def set_teclas(self, teclas):
        '''
        -> Método responsável por definir teclas de movimento
           :param teclas: Passe uma lista/tupla com os botões de controle na seguinte ordem:
                          Para cima     exemplo: K_w
                          Para baixo    exemplo: K_s
                          Para esquerda exemplo: K_a
                          Para direita  exemplo: K_d
           :return: Sem retorno
        '''
        self.teclas_movimento = teclas
    
    def set_pasos(self, pasos):
        '''
        -> Método responsável por definir a velocidade de pasos do avatar
           :param pasos: Recebe um valor inteiro que define a velocidade do movimento do avatar
           :return: Sem retorno
        '''
        self.pasos = pasos
    
    def get_avatar_visivel(self):
        '''
        -> Método responsável por retornar se o avatar está visível
           :return: Retorna o estado do avatar.
                               True se for visível
                               False se for invísivel
        '''
        return self.avatar_visivel
    
    def get_velocidade(self):
        '''
        -> Método responsável por retorna a velocidade da animação
           :return: Retorna a velocidade atual da animação
        '''
        return self.velocidade
    
    def get_teclas(self):
        '''
        -> Método responsável por retornar teclas de movimento atual
           :return: Retorna as teclas de movimento atual
        '''
        if self.teclas_movimento is None:
            return (K_w, K_s, K_a, K_d)
        else:
            return self.teclas_movimento
    
    def get_acao(self):
        """
        -> Método responsável por retornar o estado do avatar
           :return: Retorna um valor booleano.
                    True se estiver em movimento
                    False se estiver parado
        """
        return self.acao_andando
    
    def get_pasos(self):
        '''
        -> Método responsável por retornar o valor atual de pasos
           :return: Retorna o valor da velocidade dos pasos atual
        '''
        return self.pasos
