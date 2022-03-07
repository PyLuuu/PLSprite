# PLSprite

<img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/Pyluuu/PLSprite" /> <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Pyluuu/PLSprite" /> <img alt="" src="https://img.shields.io/github/repo-size/Pyluuu/PLSprite" /> <img alt="Github License" src="https://img.shields.io/github/license/pyluuu/PLSprite" />

Este projeto foi desenvolvido com propósito de facilitar a manipulação<br/>
de spritesheets para games 2D com uso da biblioteca Pygame

### Instalação
<code>pip install PLSprite</code> (não disponível, dia 07/03/2022)

Para que consiga fazer uso do nosso projeto você precisará apenas instalar a <br/>
biblioteca Pygame. Para isso você pode usar o <code>pip</code>, ou algum instalador da <br/>
sua preferência, com a seguinte linha de comando: <code>pip install pygame</code>.

### Como melhorar
Para que você possa adicionar melhorias ao projeto e queira desenvolver novas 
funcionalidades, você pode clonar o repositório com a seguinte linha de comando: 
<code>git clone https://github.com/Pyluuu/PLSprite</code>, use este comando dentro do 
diretório que deseja clonar o repositório.

## Como usar
**Importações necessárias:**

```Python
import PLSprite as PLS
import pygame as pg
```

**Exemplo de uso:**
```Python
pg.init() # Inicializando o Pygame
largura = altura = 500 # dimensoes da janela
janela = pg.display.set_mode((largura, altura)) # criando janela
adao_spritesheet = pg.image.load('adao_andando.png') # pegando a imagem do meu spritesheet
run = True # estado do programa

# criando objeto
adao = Avatar(janela,
              adao_spritesheet,
              0,
              0,
              largura//2,
              altura//2,
              60,
              60,
              animacao_h=True,
              num_animacao_h=9)

while run:
  for event in pg.event.get(): # verificando lista de eventos do Pygame
    if event.type == pg.QUIT: # ao clicar para fechar a janela o event.type sera QUIT
      run = False # estado do programa recebe False
  
  tela.fill((0, 0, 0)) # apos cada loop preenche a tela com a cor RGB 0, 0, 0, ou seja, preto
  adao.atualizar() # fará com que o seu sprite seja desenhado na janela
  
  janela.display.flip() # apos cada loop atualiza a superficie
  
```
