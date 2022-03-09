# PLSprite

<img alt="Github License" src="https://img.shields.io/github/license/pyluuu/PLSprite" /> <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Pyluuu/PLSprite" /> <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/Pyluuu/PLSprite" /> <img alt="File size" src="https://img.shields.io/github/repo-size/Pyluuu/PLSprite" />

Este projeto foi desenvolvido com propósito de facilitar a manipulação<br/>
de spritesheets para games 2D com uso da biblioteca Pygame

### Instalação
<code>pip install PLSprite</code> (não disponível, dia 07/03/2022)

Para que consiga fazer uso do nosso projeto você precisará apenas instalar a biblioteca Pygame. Para isso você pode usar o <code>pip</code>, ou algum instalador da sua preferência, com a seguinte linha de comando: <code>pip install pygame</code>.

### Como melhorar
Para que você possa adicionar melhorias ao projeto e queira desenvolver novas funcionalidades, você pode clonar o repositório com a seguinte linha de comando: <code>git clone https://github.com/Pyluuu/PLSprite</code>, use este comando dentro do diretório que deseja clonar o repositório.

### Benefícios
O nosso projeto tem como base ajudar a facilitar a maniuplação de spritesheets disponibilizando<br/>
diversas ferramentas de manipulação para os usuários.

Como a classe <code>Avatar()</code>, que é responsável por tratar de spritesheets <code>AHLV</code>, <code>AHLH</code>, <code>AVLH</code> e <br/><code>AVLV</code>(não disponível ainda).

<code>AHLV</code>: Animação na Horizontal e Lados na Vertical

<code>AHLH</code>: Animação na Horizontal e Lados na Horizontal

<code>AVLH</code>: Animação na Vertical e Lados na Horizontal

<code>AVLV</code>: Animação na Vertical e Lados na Vertical

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

#### Antes de tudo

Parâmetros da Classe <code>Avatar()</code>

**tela**: Você deve passar a janela onde seus sprites serão desenhados.

**sprite**: Você deve passar o spritesheet que irá trabalhar.

**p_img_x**: p_img_x(personagem imagem x). A posição x do meu sprite dentro do spritesheet.

**p_img_y**: p_img_y(personagem imagem y). A posição y do meu sprite dentro do spritesheet.

**x**: Recebe um valor do tipo int, a posição x do sprite.

**y**: Recebe um valor do tipo int, a posição y do sprite.

**largura**: Largura do sprite, um valor do tipo int.

**altura**: Altura do sprite, um valor do tipo int.

**lados**: Uma lista/tupla com os lados do seu sprite.

**animacao_h=False**: Recebe um valor booleano. Se este parâmetro não for passado o padrão é False.

**animacao_v=False**: Recebe um valor booleano. Se este parâmetro não for passado o padrão é False.

**num_animacao_h=0**: Recebe um valor do tipo int, a quantidade de sprites na horizontal.

**num_animacao_v=0**: Recebe um valor do tipo int, a quantidade de sprites na vertical.

**dimensao=None**: Recebe uma lista/tupla com a nova dimensão(largura e altura) do sprite.

### Explicando entradas de parâmetros

![Spritesheet com marcações](testes/imagens/sprite_adao_marcacao.png)

***Esta imagem contém as marcações de 4 parâmetros***

O **x** nos 3 primeiros sprites representa o parâmetro **p_img_x**, ou seja, onde inicia o sprite na horizontal.

**OBS.:** p_img_x não é o mesmo que o parâmetro x, enquanto x é a posição do sprite na janela p_img_x é a do sprite dentro do spritesheet.


O **y** nos 3 próximos sprites representa o parâmetro **p_img_y**, ou seja, onde inicia o sprite na vertical.

p_img_y não é y, p_img_y é a posição y dentro do spritesheet enquanto y é a posição dentro da janela.

Os parâmetros **largura** e **altura** são exatamente isso, a largura e altura do sprite.

Quando o sprite for exibido na janela a lógica é simples, ele pegará do parâmetro **p_img_x** até a **largura**, pegando assim a parte horizontal do sprite, e em seguida de **p_img_y** até a **altura**, pegando toda a parte vertical do sprite.

**animacao_h**: se a animação dos seus sprites estiverem na horizontal passe True para este parâmetro.

**animacao_v**: se a animação dos seus sprites estiverem na vertical passe True para este parâmetro.

O sprite com as marcações tem as animações na horizontal, enquanto os lados(costa, esquerda, frente, direita) estão na vertical. Nesse caso animação_h=True, porém a classe <code>Avatar()</code> tem como padrão manipular spritesheet **<a href="https://github.com/PyLuuu/PLSprite/edit/main/README.md#benef%C3%ADcios">AHLV</a>**(Animação na Horizontal e Lados na Vertical), mas caso seu spritesheet seja **<a href="https://github.com/PyLuuu/PLSprite/edit/main/README.md#benef%C3%ADcios">AHLH</a>**(Animação na Horizontal e Lados na Horizontal), você deve definir o parâmetro animacao_h=True.

O parâmetro **lados**, independente dos lados do seu spritesheets estarem na horizontal ou vertical os valores da lista/tupla devem estar na seguinte ordem cima/costa, baixo/frente, esquerda e direita. Se os lados do seu spritesheet estiverem na vertical, **lados** deve ter os valores de **p_img_y** da spritesheet, mas se os lados do seu spritesheet estiverem na horizontal **lados** deve receber os valores de **p_img_x** de cada sprite dentro da spritesheet.

***Agora vamos para a prática***

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

*Vá até o diretório de <code>testes</code>isso o ajudará a entender na prática como funciona nosso projeto.*

# Para contribuidores
Todos são muito bem-vindos(as)! Caso tenham ideias de como melhorar este projeto se manifeste 
e nos ajude a evoluir, peço que sejam criativos. Caso encontre bugs não se incomode em resolve-los, 
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
- Pyluucatnet@gmail.com


**OBS.**: Este é meu primeiro README.md. Peço desculpa desde já caso não tenha ficado muito <br/>
claro a explicação dos parâmetros para construir um avatar. Para melhor compreenção peço <br/>
que leia as docstrings do nosso projeto. Obrigado por usar nosso projeto.
