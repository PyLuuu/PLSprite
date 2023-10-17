# **PLSprite**

<img alt="Github License" src="https://img.shields.io/github/license/pyluuu/PLSprite" /> <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Pyluuu/PLSprite" /> <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/Pyluuu/PLSprite" /> <img alt="File size" src="https://img.shields.io/github/repo-size/Pyluuu/PLSprite" />

Este projeto foi desenvolvido com propósito de facilitar a manipulação
de spritesheets para games 2D com uso da biblioteca Pygame.

## **Instalação**
<code>pip install PLSprite</code> (não disponível, dia 07/03/2022) 

<!--# **Sem PC, sem desenvolvimento, sem nada. Bye.**-->

Para que consiga fazer uso do nosso projeto você precisará apenas instalar a biblioteca Pygame. Para isso, você pode usar o <code>pip</code>, ou algum instalador da sua preferência, com a seguinte linha de comando: <code>pip install pygame</code>.

## **Como melhorar**
Para que você possa adicionar melhorias ao projeto e queira desenvolver novas funcionalidades, você pode clonar o repositório com a seguinte linha de comando: <code>git clone https://github.com/Pyluu/PLSprite</code>, use este comando dentro da pasta onde deseja clonar o repositório.

## **Benefícios**
O nosso projeto tem como base ajudar a facilitar a maniuplação de spritesheets disponibilizando ferramentas de conversão, criação, inversão de sprites entre outras funcionalidades de manipulação para spritesheet.

## **Forma de usar**

Classe <code>Avatar()</code>, ela é responsável por criar um avatar com o spritesheet desejado.

Está classe só aceita spritesheets <code>AHLV</code>

***Chaves de spritesheets***

<code>AHLV</code>: Animação na Horizontal e Lados na Vertical</del>

<code>AHLH</code>: Animação na Horizontal e Lados na Horizontal

<code>AVLH</code>: Animação na Vertical e Lados na Horizontal

<code>AVLV</code>: Animação na Vertical e Lados na Vertical

**Exemplo de spritesheet** <code>AHLV</code>:

![Imagem AHLV](tutoriais/imagens/adao_spritesheet.png)


**Exemplo de spritesheet** <code>AHLH</code>:

![Imagem AHLH](tutoriais/imagens/primo_mario_spritesheet.png)


**Exemplo de spritesheet** <code>AVLH</code>:

![Imagem AVLH](tutoriais/imagens/nora_spritesheet.png)


**Exemplo de spritesheet** <code>AVLV</code>

![Imagem AVLV](tutoriais/imagens/nora_spritesheet_AVLV.png)


## **Como usar**

### ***Importação***
```Python
import PLSprite as PLS
import pygame as pg
```

*Importar a biblioteca Pygame e o nosso projeto, PLSprite, para que possamos começar a trabalhar. Agora vamos construir um avatar.*

### Antes de tudo

Parâmetros da Classe <code>Avatar()</code>

**tela**: Você deve passar a superficie onde seus sprites serão desenhados.

**spritesheet**: Você deve passar o spritesheet que deseja.

**p_img_x**: p_img_x(personagem imagem x). A posição x do sprite dentro do spritesheet.

**p_img_y**: p_img_y(personagem imagem y). A posição y do sprite dentro do spritesheet.

**x**: Recebe um valor, int, para definir a posição x do sprite.

**y**: Recebe um valor, int, para definir a posição y do sprite.

**largura**: Recebe um valor, int, que define a largura do sprite.

**altura**: Recebe um valor, int, que define a altura do sprite.

**chave_lados**: Uma lista/tupla com as chaves de direção/lados.

**Exemplo:**
```Python
chave_lados=[
            PLS.C_cima,
            PLS.C_baixo,
            PLS.C_esquerda, 
            PLS.C_direita
            ]
```

**num_animacao_h**: Recebe um valor, int, que é o número de animações na horizontal.

**dimensao=None**: Recebe uma lista/tupla com a nova dimensão(largura e altura) do spritesheet.

### *Explicando parâmetros*

![Spritesheet com marcações](tutoriais/imagens/adao_spritesheet_marcado.png)

***Esta imagem contém as marcações de 4 parâmetros***

**p_img_x**: É a posição onde inicia o sprite na horizontal. Na imagem é possível ter uma ideia do que é p_img_x.

**p_img_y**: É onde inicia o sprite na vertical.

**altura**: Altura do sprite dentro do spritesheet.

**largura**: Largura do sprite dentro do spritesheet.

**OBS.:** *p_img_x não é o mesmo que o parâmetro x, enquanto x é a posição do sprite na janela p_img_x é a posição do sprite dentro do spritesheet. Igualmente para p_img_y e y*

A classe <code>Avatar()</code> tem suporte apenas para manipulação de spritesheets <code>AHLV</code>. Para facilitar o uso de spritesheets diversos temos a classe <code>ConverteSpriteSheet()</code>, ela converte spritesheets **AHLH**(disponível), **AVLH**(indisponível), **AVLV**(indisponível) em spritesheet **AHLV**, em breve todos estarão disponiveis.

## **Criando um avatar**
```Python
pg.init()
l, a = (500, 500) # largura, altura
pg.display.set_caption('Criando Avatar') # nomeando janela
tela = pg.display.set_mode((l, a)) # criando janela
run = True

adao_spritesheet = pg.image.load('imagens/adao_spritesheet.png')

# Instanciando a classe
adao = PLS.Avatar(
    tela=tela,
    spritesheet=adao_spritesheet,
    p_img_x=0,
    p_img_y=0,
    x=l//2,
    y=a//2,
    largura=60,
    altura=60,
    chave_lados=PLS.C_lados,
    num_animacao_h=9)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    tela.fill((10, 20, 30))

    adao.atualizar() # método atualizar() atualiza a animação do sprite

    pg.display.flip()
```
*Isso fará com que o avatar seja exibido no centro da janela*

**OBS**.: *Este exemplo de código está <a href="https://github.com/PyLuuu/PLSprite/blob/main/tutoriais/construindo_avatar.py">aqui</a>, outros tutoriais de como usar as classes PLS estão nos <code><a href="tutoriais">tutoriais</a></code>.*

# Para contribuidores
Todos são muito bem-vindos(as)! Caso tenham ideias de como melhorar este projeto se manifeste 
e nos ajude a evoluir, peço que sejam criativos. Eu sei que é um projeto pequeno, mas acredito que possa se tornar uma ferramenta útil para criadores de jogos 2D. Caso encontre bugs ou erros não se incomode em resolve-los, 
e ajude este pequeno projeto a se tornar uma ferramenta útil para desenvolvedores de jogos 2D.

# Links
- <a href="https://www.pygame.org/">Link para o site oficial do Pygame</a>

# Licença

MIT License

Copyright (c) 2022 Lus Henrique Alexandre dos S.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Criadores
- **PyLuu**

### Contatos
- contatopyluu@gmail.com


**OBS.**: *Este é meu primeiro README.md e meu primeiro projeto no GitHub. Peço desculpa desde já caso eu não tenha conseguido passar o recado de uma forma clara e objetiva e também por bugs no código, tentarei evoluir e adicionar mais funcionalidades e corrigir bugs que forem encontrados. Caso tenha dúvidas a respeito de como usar classes, métodos e funções leia as docstrings do nosso projeto. Obrigado por usar PLSprite.*
