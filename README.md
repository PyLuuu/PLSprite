# PLSprite

<img alt="Github License" src="https://img.shields.io/github/license/pyluuu/PLSprite" /> <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Pyluuu/PLSprite" /> <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/Pyluuu/PLSprite" /> <img alt="File size" src="https://img.shields.io/github/repo-size/Pyluuu/PLSprite" />

Este projeto foi desenvolvido com propósito de facilitar a manipulação<br/>
de spritesheets para games 2D com uso da biblioteca Pygame

### Instalação
<code>pip install PLSprite</code> (não disponível, dia 07/03/2022)

Para que consiga fazer uso do nosso projeto você precisará apenas instalar a <br/>
biblioteca Pygame. Para isso você pode usar o <code>pip</code>, ou algum instalador da <br/>
sua preferência, com a seguinte linha de comando: <code>pip install pygame</code>.

### Como melhorar
Para que você possa adicionar melhorias ao projeto e queira desenvolver novas <br/>
funcionalidades, você pode clonar o repositório com a seguinte linha de comando: <br/>
<code>git clone https://github.com/Pyluuu/PLSprite</code>, use este comando dentro do <br/>
diretório que deseja clonar o repositório.

### Benefícios
O nosso projeto tem como base ajudar a facilitar a maniuplação de spritesheets disponibilizando<br/>
diversas ferramentas de manipulação para os usuários.

Como a classe <code>Avatar()</code>, que é responsável por tratar de spritesheets <code>AHLV</code>, <code>AHLH</code>, <code>AVLH</code> e <br/><code>AVLV</code>(não disponível ainda).

<code>AHLV</code>: Animação na Horizontal e Lados na Vertical<br/>
<code>AHLH</code>: Animação na Horizontal e Lados na Horizontal<br/>
<code>AVLH</code>: Animação na Vertical e Lados na Horizontal<br/>
<code>AVLV</code>: Animação na Vertical e Lados na Vertical<br/>

**Exemplo de spritesheet** <code>AHLV</code>:

![Imagem AHLV](testes/imagens/adao_andando.png)


**Exemplo de spritesheet** <code>AHLH</code>:

![Imagem AHLH](testes/imagens/primo_mario_andando.png)


**Exemplo de spritesheet** <code>AVLH</code>:

![Imagem AVLH](testes/imagens/nora_andando.png)


**Exemplo de spritesheet** <code>AVLV</code>: (não disponível ainda)

## Como usar

### Importação
```Python
import PLSprite as PLS
import pygame as pg
```
*Importar a biblioteca Pygame e o nosso projeto, PLSprite, para que possamos começar a trabalhar.*
*Após a importação da biblioteca Pygame e do nosso projeto vamos construir um avatar*

**Exemplo de uso:**
```Python
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

```
*Isso fará com que seu sprite seja exibido no centro da janela*

OBS.: Este exemplo de código está <a href="https://github.com/PyLuuu/PLSprite/blob/main/testes/construindo_avatar.py">aqui</a>, outros tutoriais de como usar cada tipo de spritesheets estão na pasta <code><a href="testes">testes</a></code>.

