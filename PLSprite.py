"""
┌───────────────────────────────────────────────┐
   ______   __    __   _        _    _   _    _
  |  __  \  \ \  / /  | |      | |  | | | |  | |
  | |__| |   \ \/ /   | |      | |  | | | |  | |
  | |____/    \  /    | |      | |  | | | |  | |
  | |         / /     | |____  | |__| | | |__| |
  |_|        /_/      |______| \______/ \______/
  Luís H.A.S.         Seg, 28/03/2022
                      PyLuu of CnC(future Pit)
                           Pyluucatnet@gmail.com
└───────────────────────────────────────────────┘
"""

import pygame

print('I\'m PLSprite. Welcome!')

# Chaves de spritesheets
AHLV = 0
AHLH = 1
AVLH = 10
AVLV = 11
# Chaves de lados
C_cima = 0
C_baixo = 1
C_esquerda = 10
C_direita = 11
C_lados = (C_cima, C_baixo, C_esquerda, C_direita)


class SpriteModifier:
    def __init__(self, *args: pygame.SurfaceType):
        self.sprites = args
    
    def flipsprite(self, orientation_xy: tuple[bool, bool] = (False, False)):
        list_sprites = list()
        # Invertendo a orientação dos sprites
        for s in self.sprites:
            list_sprites.append(
                pygame.transform.flip(surface=s,
                                      flip_x=orientation_xy[0],
                                      flip_y=orientation_xy[1]))
        return list_sprites

    def spritescale(self, size: float | tuple[float, float]):
        new_list_sprite = list()

        if isinstance(size, float) or isinstance(size, int):
            size = (size, size)

        for sprite in self.sprites:
            new_list_sprite.append(pygame.transform.scale(sprite, size))

        return new_list_sprite

    @staticmethod
    def savesprite(sprites):
        for i, sprite in enumerate(sprites):
            pygame.image.save(sprite, f'Nova_foto_{i + 1}.png')


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
    
    Instanciando a classe. Lembre-se de utilizar o método gerar() para que ele retorne o spritesheet para o objeto meu_sprite
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
           :dimensao_spritesheet: Recebe uma lista/tupla com as dimensões(largura, altura) do spritesheet
           :espaco_horizontal: Espaçamento horizontal entre os sprites
           :espaco_vertical: Espaçamento vertical entre os sprites
           :dimensao_sprite: Recebe uma lista/tupla com a nova dimensão(largura, altura) do sprite
           :alfa: Recebe um valor booleano. Se alfa == True os sprites tem fundo transparente
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


class ConverteSpriteSheet:
    def __init__(self,
                 spritesheet,
                 num_animacao,
                 num_lados,
                 chave_spritesheet,
                 d_sprite,
                 d_spritesheet=None,
                 alfa=True):
        """
        Inicializando objeto

        :param spritesheet: Recebe o spritesheet que será convertido
        :param num_animacao: Recebe um valor, int, da quantidade de animações do spritesheet
        :param num_lados: Recebe um valor, int, da quantidade de lados do spritesheet
        :param chave_spritesheet: Recebe uma chave de spritesheet
                                  Exemplo: PLS.AHLV
                                           PLS.AHLH
                                           PLS.AVLH
                                           PLS.AVLV
                                  Chaves de spritesheet são os padrões de spritesheet
                                  AHLV: Animação na Horizontal e Lados na Vertical
                                  AHLH: Animação na Horizontal e Lados na Horizontal
                                  AVLH: Animação na Vertical e Lados na Horizontal
                                  AVLV: Animação na Vertical e Lados na Vertical
        :param d_sprite: Recebe uma lista/tupla com a dimensão(largura, altura) do sprite
        :param d_spritesheet: Parâmetro opcional. Recebe uma lista/tupla com a dimensão do spritesheet que será gerado
        :param alfa: Parâmetro opcional. Recebe um valor, booleano, que define a transparência do fundo do spritesheet
                     Obs.: Se nenhum valor for passado o padrão é True
        """
        self.spritesheet = spritesheet
        self.num_animacao = num_animacao
        self.num_lados = num_lados
        self.chave = chave_spritesheet
        self.d_sprite = d_sprite
        self.d_spritesheet = d_spritesheet
        self.alfa = alfa
    
    def converter(self):
        """
        -> Método responsável pela conversão do spritesheet
        :return: Retorna o spritesheet convertido
        """
        if self.d_spritesheet:
            self.spritesheet = pygame.transform.scale(self.spritesheet, self.d_spritesheet)
        if self.chave == AHLH:
            self.novo_spritesheet = pygame.Surface((self.d_sprite[0] * self.num_animacao + 10, self.d_sprite[1] * self.num_lados))
            self.novo_spritesheet.fill((0, 255, 0))
            self.largura_janela = self.spritesheet.get_rect()[-2] // self.num_lados
            self.altura_janela = self.d_sprite[1]
            self.janela = pygame.Surface((self.largura_janela, self.altura_janela))
            for c in range(self.num_lados):
                self.janela.fill((255, 0, 0))
                if self.alfa:
                    alfa_janela = self.janela.get_at((0, 0))
                    self.janela.set_colorkey(alfa_janela)
                    alfa_novo_spritesheet = self.novo_spritesheet.get_at((0, 0))
                    self.novo_spritesheet.set_colorkey(alfa_novo_spritesheet)
                self.janela.blit(self.spritesheet, (0, 0), (self.largura_janela * c, 0, self.largura_janela, self.altura_janela))
                self.novo_spritesheet.blit(self.janela, (0, self.altura_janela * c))
        elif self.chave == AVLV:
            pass
        elif self.chave == AVLH:
            pass
        return self.novo_spritesheet


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
                 dimensao_spritesheet=None):
        """
        Inicializando objeto
        
        :tela: Recebe a superficie onde os sprites serão desenhados
        :spritesheet: Recebe o spritesheet que será usado para animar
        :teclas_controle: Recebe uma lista/tupla com as teclas de movimento do sprite
                        OBS.: As teclas devem ser passadas de acordo com a ordem do seu spritesheet
                        Exemplo:
                               Se o seu spritesheet tiver a primeira animação como andar para a esquerda 
                               a primeira tecla será responsável por ativar a animação da esquerda e assim sucessivamente
        :largura: Recebe um valor do tipo int para definir a largura do sprite
        :altura: Recebe um valor do tipo int para definir a altura do sprite
        :p_img_x: Recebe um valor do tipo int para definir a posição x do sprite dentro do spritesheet
        :p_img_y: Recebe um valor do tipo int para definir a posição y do sprite dentro do spritesheet
        :x: Recebe um valor do tipo int para definir a posição x do sprite na superficie definida
        :y: Recebe um valor do tipo int para definir a posição y do sprite na superficie definida
        :num_animacao_h: Recebe um valor do tipo int, que é a quantidade de sprites na horizontal
        :dimensao_spritesheet: Recebe uma lista/tupla com a nova dimensão(largura, altura) do spritesheet
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
        self.dimensao_spritesheet = dimensao_spritesheet
        self.atraso = 0
        self.velocidade_animacao = 0.1
        self.sprite_inicio = 0
        self.andar = False
        self.sprite_padrao_xy = (0, None)
    
    def iniciar(self):
        """Método responsável por construir o sprite"""
        janela_avatar = pygame.Surface((self.largura, self.altura))
        if self.dimensao_spritesheet:
            self.spritesheet = pygame.transform.scale(self.spritesheet, self.dimensao_spritesheet)
        janela_avatar.blit(self.spritesheet, (0, 0), (self.p_img_x, self.p_img_y, self.largura, self.altura))
        self.tela.blit(janela_avatar, (self.x, self.y))
        self._controles()
    
    def _controles(self):
        """Método responsável por controlar as animações do spritesheet"""
        keys = pygame.key.get_pressed()
        for i, key in enumerate(self.teclas_controle):
            if keys[key]:
                self.p_img_y = i * self.altura 
                self.andar = True
        if self.andar:
            self.atraso += 1
            if self.atraso > self.velocidade_animacao * 20: # definindo a velocidade da animação
                self.atraso = 0
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
           :num: Recebe um valor, int, que define o p_img_x do primeiro sprite a ser exibido após cada loop da animação
        """
        self.sprite_inicio = num
    
    def set_posx(self, pos_x):
        """
        -> Método responsável por definir a posição x do sprite
           :pos_x: Recebe um valor, int, que será a nova posição x do sprite
        """
        self.x = pos_x
    
    def set_posy(self, pos_y):
        """
        -> Método responsável por definir a posição y do sprite
           :pos_y: Recebe um valor, int, que será a nova posição y do sprite
        """
        self.y = pos_y
    
    def set_sprite_padrao_xy(self, pos_xy):
        """
        -> Método responsável por definir a posição padrão
           :pos_xy: Recebe uma lista/tupla com dois valores, posição x e posição y. Caso queira definir
                    somente uma das posições use None para invalidar a posição que não irá definir
           Exemplo: .set_sprite_padrao_xy([x, None]) # x, y
        """
        self.sprite_padrao_xy = pos_xy
    
    def set_velocidade_animacao(self, num):
        """
        -> Método responsável por definir a velocidade da animação
           :num: Recebe um valor, int, para definir a velocidade de transição da animação
        """
        self.velocidade_animacao = num
    
    def set_num_animacaoh(self, num):
        """
        -> Método responsável por definir a quatidade de sprites na horizontal
           :num: Recebe um valor, int, para definir quantos sprites há na horizontal
        """
        self.num_animacao_h = num
    
    def set_num_animacaov(self, num):
        """
        -> Método responsável por definir a quantidade de sprites na vertical
           :num: Recebe um valor, int, para definir quantos sprites há na vertical
        """
        self.num_animacao_v = num
    
    def get_dimensao_sprite(self):
        """
        -> Método responsável por retornar a dimensão do spritesheet em uso
           :return: Retorna uma lista com a dimensão do spritesheet em uso
        """
        return self.spritesheet.get_rect()[2:]
    
    def get_posx(self):
        """
        -> Método responsável por retornar a posição x do sprite
           :return: Retorna um valor, int, da posição x do sprite
        """
        return self.x
    
    def get_posy(self):
        """
        -> Método responsável por retornar a posição y do sprite
           :return: Retorna um valor, int, da posição y do sprite
        """
        return self.y
    
    def get_velocidade_animacao(self):
        """
        -> Método responável por retornar a velocidade da animação
           :return: Retorna um valor int, da velocidade da animação
        """
        return self.velocidade_animacao
    
    def get_num_animacaoh(self):
        """
        -> Método responsável por retornar o número de animações na horizontal
           :return: Retorna a quantidade de animações na horizontal
        """
        return self.num_animacao_h


class Avatar:
    """Classe para manipulação de spritesheets AHLV"""
    def __init__(self, tela,
                       spritesheet,
                       p_img_x,
                       p_img_y,
                       x,
                       y,
                       largura,
                       altura,
                       chave_lados,
                       num_animacao_h,
                       dimensao=None):
        """
        Inicializando objeto
        
        :tela: Recebe uma superficie onde o sprite será desenhado
        :spritesheet: Recebe o spritesheet que será usado
        :p_img_x: Recebe um valor, int, para a posição x do sprite dentro do spritesheet
        :p_img_y: Recebe um valor, int, para a posição y do sprite dentro do spritesheet
        :x: Recebe um valor, int, para a posição x do sprite na superficie
        :y: Recebe um valor, int, para a posição y do sprite na superficie
        :largura: Recebe um valor, int, para definir a largura do sprite
        :altura: Recebe um valor, int, para definir a altura do sprite
        :chave_lados: Recebe uma lista/tupla com chaves de direção/lados
                      Exemplo: [PLS.C_cima, PLS.C_baixo, PLS.C_esquerda, PLS.C_direita]
        :num_animacao_h: Recebe um valor, int, para definir a quantidade de animações na horizontal do spritesheet
        :dimensao: Recebe uma lista/tupla com a nova dimensão(largura, altura) do spritesheet
        """
        self.tela = tela
        self.spritesheet = spritesheet
        self.p_img_x = p_img_x
        self.p_img_y = p_img_y
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.chave_lados = chave_lados
        self.num_lado = len(self.chave_lados)
        self.num_animacao_h = num_animacao_h
        self.dimensao_spritesheet = dimensao
        self.movimento = 1
        self.velocidade = 1
        self.atraso_animacao = 0
        self.pasos = 5
        self.acao_andando = False
        self.teclas_movimento = None
        self.avatar_visivel = True
        self.cor_fundo_avatar = (0, 0, 0)
    
    def _iniciar_sprite(self):
        """Método responsável por criar avatar"""
        if self.avatar_visivel:
            if self.dimensao_spritesheet:
                self.sprite = pygame.transform.scale(self.spritesheet, self.dimensao_spritesheet)
            self.tela.blit(self.spritesheet, (self.x, self.y), (self.p_img_x, self.p_img_y, self.largura, self.altura))
        elif self.fundo_avatar:
            fundo_avatar = pygame.Surface((self.largura, self.altura))
            fundo_avatar.fill(self.cor_fundo_avatar)
            self.tela.blit(fundo_avatar, (self.x, self.y))
    
    def atualizar(self):
        """Método responsável por atualizar a animação do avatar"""
        self._iniciar_sprite()
        if self.dimensao_spritesheet:
            self.spritesheet = pygame.transform.scale(self.spritesheet, self.dimensao_spritesheet)
        rect_sprite = self.spritesheet.get_rect()
        if self.acao_andando: # se o sprite tiver em movimento ou definido para loop infinito
            if self.atraso_animacao > (20 * self.velocidade):
                self.movimento += self.largura
                if self.movimento // self.largura == self.num_animacao_h:
                    self.movimento = 0
                self.p_img_x = self.movimento
                self.atraso_animacao = 0
        self.atraso_animacao += 1
    
    def controles(self, teclas, pasos=None):
        """
        -> Método responsável por controlar o movimento do avatar
           :teclas: Recebe uma lista/tupla com as chaves de movimento
                    Exemplo: (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
           :pasos: Parâmetro opcional. Senão for definido recebe None e a velocidade será padrão
        """
        if pasos:
            self.pasos = pasos
        tecla = pygame.key.get_pressed()
        self.acao_andando = False
        if self.teclas_movimento: # teclas de movimento personalizada
            for c in range(len(self.teclas_movimento)):
                if tecla[self.teclas_movimento[c]]:
                    if self.chave_lados == AHLV:
                        self.p_img_y = self.altura * c
                        if self.chave_lados[c] == C_cima:
                            self.y -= self.pasos
                            self.acao_andando = True
                        if self.chave_lados[c] == C_baixo:
                            self.y += self.pasos
                            self.acao_andando = True
                        if self.chave_lados[c] == C_esquerda:
                            self.x -= self.pasos
                            self.acao_andando = True
                        if self.chave_lados[c] == C_direita:
                            self.x += self.pasos
                            self.acao_andando = True
        else:
            self.teclas_movimento = teclas
    
    def set_posx(self, pos_x):
        """
        -> Método responsável por definir a posição x do sprite
           :pos_x: Recebe um valor, int, que define a posição x do sprite
        """
        self.x = pos_x
    
    def set_posy(self, pos_y):
        """
        -> Método responsável por definir a posição y do sprite
           :pos_y: Recebe um valor, int, que define a posição y do sprite
        """
        self.y = pos_y
    
    def set_num_animacaoh(self, num_animacao):
        """
        -> Método responsável por definir o número de animações na horizontal
           :num_animacao: Recebe um valor, int, que define quantos sprites há na horizontal
        """
        self.num_animacao_h = num_animacao
    
    def set_imgh(self, index_x):
        """
        -> Método responsável por definir a posição X da imagem dentro do spritesheet
           :index_x: Recebe um valor, int, do index horizontal do sprite dentro do spritesheet
        """
        self.p_img_x = index_x * self.largura
    
    def set_imgv(self, index_y):
        """
        -> Método responsável por definir a posição Y da sprite dentro do spritesheet
           :index_y: Recebe um valor, int, do index vertical do sprite dentro do spritesheet
        """
        self.p_img_y = index_y * self.altura
    
    def set_janelah(self, largura):
        """
        -> Método responsável por definir a largura da janela do sprite
           :largura: Recebe um valor, int, que define a largura da janela
        """
        self.largura = largura
    
    def set_janelav(self, altura):
        """
        -> Método responsável por definir a altura da janela do sprite
           :altura: Recebe um valor, int, que define a altura da janela
        """
        self.altura = altura
    
    def set_dimensao_sprite(self, l_a):
        """
        -> Método responsável por definir nova dimensão do spritesheet
           :l_a: Recebe uma lista/tupla com a nova dimensão(largura, altura) do spritesheet
        """
        self.dimensao_spritesheet = l_a
    
    def set_avatar_visivel(self, visivel, fundo_avatar=False, cor_fundo=(0, 0, 0)):
        """
        -> Método responsável por definir estado do avatar
           :visivel: Recebe um valor booleano
                     True visível
                     False invisível
           :fundo_avatar: Parâmetro opcional. Recebe um valor booleano. Se True, ficará um quadrado no local do avatar
           :cor_fundo: Parâmetro opcional. Recebe uma lista/tupla com 3 valores para RGB
                       Senão for passado recebe (0, 0, 0), preto, como padrão
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
           :teclas: Passe uma lista/tupla com as teclas de controle na seguinte ordem:
                  Para cima     exemplo: pygame.K_w
                  Para baixo    exemplo: pygame.K_s
                  Para esquerda exemplo: pygame.K_a
                  Para direita  exemplo: pygame.K_d
        """
        self.teclas_movimento = teclas
    
    def set_pasos(self, pasos):
        """
        -> Método responsável por definir a velocidade de pasos do avatar
           :pasos: Recebe um valor, int, que define a velocidade do movimento do avatar
        """
        self.pasos = pasos
    
    def get_sprite_atualh(self):
        """Método responsável por retornar o index do sprite atual na horizontal"""
        return self.movimento // self.largura
    
    def get_posx(self):
        """Método responsável por retornar a posição x do avatar na superficie"""
        return self.x
    
    def get_posy(self):
        """Método respionsável por retornar a posição y do avatar na superficie"""
        return self.y
    
    def get_avatar_visivel(self):
        """
        -> Método responsável por retornar o estado do avatar
           :return: Retorna o estado do sprite
                    True se for visível
                    False se for invisível
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
        """-> Método responsável por retornar o número de animações na horizontal"""
        return self.num_animacao_h
    
    def get_dimensao_spritesheet(self):
        """Método responsável por retornar uma lista com a dimensão(largura, altura) do spritesheet"""
        return self.spritesheet.get_rect()[-2:]
        
    def get_acao(self):
        """
        -> Método responsável por retornar o estado do avatar
           :return: Retorna um valor booleano.
                    True se estiver em movimento
                    False se estiver parado
        """
        return self.acao_andando
    
    def get_pasos(self):
        """Método responsável por retornar o valor atual de pasos"""
        return self.pasos


if __name__ == '__main__':
    from time import sleep

    LARGURA = 500
    ALTURA = 500
    BACKGROUND = (10, 50, 70)
    run = True
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('PLS')

    s1 = pygame.image.load(f'imgs/Adany 1.png')
    s2 = pygame.image.load(f'imgs/Adany 2.png')
    s3 = pygame.image.load(f'imgs/Adany 3.png')
    s4 = pygame.image.load(f'imgs/Adany 4.png')

    sprite = SpriteModifier(s1, s2, s3, s4)
    # new_sprites = sprite.flipsprite((True, False))
    new_sprites = sprite.spritescale(300)
    SpriteModifier.savesprite(sprites=new_sprites)

    index = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        tela.fill(BACKGROUND)

        tela.blit(new_sprites[index], (LARGURA // 2, ALTURA // 2))
        if index < 3:
            index += 1
        else:
            index = 0
        sleep(.5)

        pygame.display.flip()
