.. $Id: capitulo_09.rst,v 2.1 2007-04-23 21:17:35 luciano Exp $

==================
Capítulo 9: Tuplas
==================

.. contents:: Tópicos

-------------------------
9.1 Mutabilidade e tuplas
-------------------------

Até agora, você tem visto dois tipos compostos: strings, que são compostos de caracteres; e listas, que são compostas de elementos de qualquer tipo. Uma das diferenças que notamos é que os elementos de uma lista podem ser modificados, mas os caracteres em uma string não. Em outras palavras, strings são **imutáveis** e listas são **mutáveis**.

Há um outro tipo em Python chamado **tupla** *(tuple)* que é similar a uma lista exceto por ele ser **imutável**. Sintaticamente, uma tupla é uma lista de valores separados por vírgulas:

>>> tupla = 'a', 'b', 'c', 'd', 'e'

Embora não seja necessário, é convencional colocar tuplas entre parênteses:

>>> tupla = ('a', 'b', 'c', 'd', 'e')

Para criar uma tupla com um único elemento, temos que incluir uma vírgula final:

>>> t1 = ('a',)
>>> type(t1)
<type 'tuple'>

Sem a vírgula, Python entende ``('a')`` como uma string entre parênteses:

>>> t2 = ('a')
>>> type(t2)
<type 'string'>

Questões de sintaxe de lado, as operações em tuplas são as mesmas operações das listas. O operador índice seleciona um elemento da tupla.

>>> tupla = ('a', 'b', 'c', 'd', 'e')
>>> tupla[0]
'a'

E o operador *slice* (fatia) seleciona uma "faixa" (*range*) de elementos.

>>> tupla[1:3]
('b', 'c')

Mas se tentarmos modificar um dos elementos de uma tupla, teremos um erro:

>>> tupla[0] = 'A'
TypeError: object doesn't support item assignment

Naturalmente, mesmo que não possamos modificar os elementos de uma tupla, podemos substituí-la por uma tupla diferente:

>>> tupla = ('A',) + tupla[1:]
>>> tupla
('A', 'b', 'c', 'd', 'e')

-------------------------
9.2 Atribuições de tupla
-------------------------

De vez em quando, é necessário trocar entre si os valores de duas variáveis. Com operações de atribuição convencionais, temos que utilizar uma variável temporária. Por exemplo, para fazer a troca entre ``a`` e ``b``:

>>> temp = a
>>> a = b
>>> b = temp

Se você tiver que fazer isso com frequência, esta abordagem se torna incômoda. Python fornece uma forma de **atribuição de tupla** que resolve esse problema elegantemente:

>>> a, b = b, a

O lado esquedo é uma tupla de variáveis; o lado direito é uma tupla de valores. Cada valor é atribuído à sua respectiva variável. Todas as expressões do lado direito são avaliadas antes de qualquer das atribuições. Esta característica torna as atribuições de tupla bastante versáteis.

Naturalmente, o número de variáveis na esquerda e o número de valores na direita deve ser igual:

>>> a, b, c, d = 1, 2, 3
ValueError: unpack tuple of wrong size 

------------------------------------
9.3 Tuplas como valores de retorno
------------------------------------

Funções podem retornar tuplas como valor de retorno. Por Exemplo, nós poderíamos escrever uma função que troca dois parâmetros entre si::

  def troca(x, y):
    return y, x

Então nós poderíamos atribuir o valor de retorno para uma tupla com duas variáveis::

  a, b = troca(a, b)

Neste caso, não existe uma grande vantagem em fazer de ``troca`` (*swap*) uma função. De fato, existe um perigo em tentar encapsular ``troca``, o qual é a tentação de cometer o seguinte erro::

  def troca(x, y):      # versao incorreta
    x, y = y, x

Se nós chamarmos esta função desta forma::

  troca(a, b)

então ``a`` e ``x`` são apelidos para um mesmo valor. Mudar ``x`` dentro da função ``troca``, faz com que ``x`` se referencie a um valor diferente, mas sem  efeito sobre ``a`` dentro de ``__main__``. Do mesmo modo, a mudança em ``y`` não tem efeito sobre ``b``.

Esta função roda sem produzir uma mensagem de erro, mas ela não faz o que pretendemos. Este é um exemplo de um erro semântico.

  *Como exercício, desenhe um diagrama de estado pra esta função de modo que você possa ver porque ela não funciona.*

-----------------------
9.4 Números aleatórios
-----------------------

A maioria dos programas de computador fazem a mesma coisa sempre que são executados, então, podemos dizer que eles são **determinísticos**. Determinismo em geral é uma coisa boa, se nós esperamos que um cálculo dê sempre o mesmo resultado. Entretanto, para algumas aplicações queremos que o computador se torne imprevisível. Jogos são um exemplo óbvio, mas existem outros.

Fazer um programa realmente não-determinístico se mostra não ser tão fácil, mas existem maneiras de fazê-lo ao menos parecer não-determinístico. Uma dessas maneiras é gerar números aleatórios e usá-los para determinar o resultado de um programa. Python tem uma função nativa que gera números **pseudo aleatórios**, os quais não são verdadeiramente aleatórios no sentido matemático, mas para os nossos propósitos eles são.

O módulo ``random`` contém uma função chamada ``random`` que retorna um número em ponto flutuante (*floating-point number*) entre 0.0 e 1.0. Cada vez que você chama ``random``, você recebe o próximo número de uma longa série. Para ver uma amostra, execute este loop::

  import random

  for i in range(10):
    x = random.random()
    print x


Para gerar um número aleatório ente 0.0 e um limite superior, digamos ``superior``, multiplique ``x`` por ``superior``.

	*Como exercício, gere um número aleatório entre 'inferior' e 'superior'.*

	*Como exercício adicional, gere um número inteiro aleatório entre 'inferior' e 'superior', inclusive os dois extremos.*


--------------------------------
9.5 Lista de números aleatórios
--------------------------------

O primeiro passo é gerar uma lista aleatória de valores. ``listaAleatoria`` pega um parâmetro inteiro e retorna uma lista de números aleatórios com o comprimento dado. Inicia-se com uma lista de ``n`` zeros. A cada iteração do loop, ele substitui um dos elementos por um número aleatório. O valor retornado é uma referência para a lista completa::

  def listaAleatoria(n):
    s = [0] * n
    for i in range(n):
      s[i] = random.random()
    return s

Vamos realizar um teste desta função com uma lista de oito elementos. Para efeitos de depuração, é uma boa idéia começar com uma lista pequena.

>>> listaAleatoria(8)
0.15156642489
0.498048560109
0.810894847068
0.360371157682
0.275119183077
0.328578797631
0.759199803101
0.800367163582

Os números gerados por ``random`` são supostamente uniformemente distribuídos, o que significa que cada valor tem uma probabilidade igual de acontecer.

Se nós dividirmos a faixa de valores possíveis em intervalos do mesmo tamanho, e contarmos o número de vezes que um determinado valor aleatório caiu em seu respectivo intervalo, nós devemos obter  o mesmo número aproximado de valores em cada um dos intervalos. 

Nós podemos testar esta teoria escrevendo um programa que divida a faixa de valores em intervalos e conte o número de valores de cada intervalo.

-------------
9.6 Contando
-------------
Uma boa maneira de abordar problemas como esse é dividir o problema em subproblemas, e encontrar um subproblema que se enquadre em um padrão de solução computacional que você já tenha visto antes.

Neste caso, queremos percorrer uma lista de números e contar o número de vezes que valor se encaixa em um determinado intervalo. Isso soa familiar. Na Seção 7.8, nós escrevemos um programa que percorria uma string e contava o número de vezes que uma determinada letra aparecia.

Assim, podemos prosseguir copiando o programa original e adaptando-o para o problema atual. O programa original era::

  contador = 0
  for letra in fruta:
    if letra == 'a':
      contador = contador + 1
  print contador


O primeiro passo é substituir ``fruta`` por ``lista`` e ``letra`` por ``numero``. Isso não muda o programa, apenas o ajusta para que ele se torne mais fácil de ler e entender.

O segundo passo é mudar o teste. Nós não estamos interessados em procurar letras. Nós queremos ver se ``numero`` está entre ``inferior`` e ``superior``.::

  contador = 0
    for numero in lista
      if inferior < numero < superior:
        contador = contador + 1
    print contador


O último passo é encapsular este código em uma função chamada ``noIntervalo``. Os parâmetros são a lista e os valores ``inferior`` e ``superior``::

  def noIntervalo(lista, inferior, superior):
      contador = 0
      for numero in lista:
        if inferior < numero < superior:
          contador = contador + 1
      return contador


Através da cópia e da modificação de um programa existente, estamos aptos a escrever esta função rapidamente e economizar um bocado de tempo de depuração. Este plano de desenvolvimento é chamado de **casamento de padrões**. Se você se encontrar trabalhando em um problema que você já solucionou antes, reuse a solução.

--------------------------
9.7 Vários intervalos
--------------------------

Conforme o número de intervalos aumenta, ``noIntervalo`` torna-se intragável. Com dois intervalos, não é tão ruim::

  inferior = noIntervalo(a, 0.0, 0.5)
  superior = noIntervalo(a, 0.5, 1)

Mas com quatro intervalos, começa a ficar desconfortável.::

  intervalo1 = noIntervalo(a, 0.0, 0.25)
  intervalo2 = noIntervalo(a, 0.25, 0.5)
  intervalo3 = noIntervalo(a, 0.5, 0.75)
  intervalo4 = noIntervalo(a, 0.75, 1.0)

Existem aqui dois problemas. Um é que temos que criar novos nomes de variável para cada resultado. O outro é que temos que calcular os limites de cada intervalo.

Vamos resolver o segundo problema primeiro. Se o número de intervalos é ``numeroDeIntervalos``, então a largura de cada intervalo é 1.0 / ``numeroDeIntervalos``.

Vamos usar um laço (*loop*) para calcular a faixa, ou largura, de cada intervalo. A variável do *loop*, ``i``, conta de 0 até ``numeroDeIntervalos-1``::

  larguraDoIntervalo = 1.0 / numeroDeIntervalos
  for i in range(numeroDeIntervalos):
    inferior = i * larguraDoIntervalo
    superior = inferior + larguraDoIntervalo
    print "do" inferior, "ao", superior


Para calcular o limite inferior (``inferior``) de cada intervalo, nós multiplicamos a variável do *loop* (``i``) pela largura do intervalo (``larguraDoIntervalo``). O limite superior (``superior``) está exatamente uma "largura de intervalo" acima.

Com ``numeroDeIntervalos = 8``, o resultado é::

  0.0 to 0.125
  0.125 to 0.25
  0.25 to 0.375
  0.375 to 0.5
  0.5 to 0.625
  0.625 to 0.75
  0.75 to 0.875
  0.875 to 1.0


Você pode confirmar que cada intervalo tem a mesma largura, que eles não se sobrepõe, e que eles cobrem toda a faixa de valores de 0.0 a 1.0.

Agora, de volta ao primeiro problema. Nós precisamos de uma maneira de guardar oito inteiros, usando a váriavel do *loop* para indicar cada um destes inteiros. Você deve estar pensando, "Lista!"

Nós temos que criar a lista de intervalos fora do *loop*, porque queremos fazer isto apenas uma vez. Dentro do loop, nós vamos chamar ``noIntervalo`` repetidamente e atualizar o ``i``-ésimo elemento da lista::

  numeroDeIntervalos = 8
  intervalos = [0] * numeroDeIntervalos
  larguraDoIntervalo = 1.0 / numeroDeIntervalos
  for i in range(numeroDeIntervalos):
    inferior = i * larguraDoIntervalo
    superior = inferior + larguraDoIntervalo
    intervalos[i] = noIntervalo(lista, inferior, superior)
  print intervalos


Com uma lista de 1000 valores, este código vai produzir esta lista de quantidades de valores em cada intervalo::

  [138, 124, 128, 118, 130, 117, 114, 131]


Esses números estão razoavelmente póximos de 125, o que era o que esperávamos. Pelo menos eles estão próximos o bastante para nos fazer acreditar que o gerador de número aleatórios está funcionando.

  *Como exercício, teste esta função com algumas listas longas, e veja se o número de valores em cada um dos intervalos tendem a uma distribuição nivelada.*

-------------------------------
9.8 Uma solução em um só passo
-------------------------------

Embora este programa funcione, ele não é tão eficiente quanto poderia ser. Toda vez que ele chama ``noIntervalo``, ele percorre a lista inteira. Conforme o número de intervalos aumenta, a lista será percorrida um bocado de vezes.

Seria melhor fazer uma única passagem pela lista e calcular para cada valor o índice do intervalo ao qual o valor pertença. Então podemos incrementar o contador apropriado.

Na seção anterior, pegamos um índice, ``i``, e o multiplicamos pela ``larguraDoIntervalo`` para encontrar o limite inferior daquele intervalo. Agora queremos pegar um valor entre 0.0 e 1.0 e encontrar o índice do intervalo ao qual ele se encaixa.

Já que este problema é o inverso do problema anterior, podemos imaginar que deveríamos dividir por ``larguraDoIntervalo`` em vez de multiplicar. Esta suposição está correta.

Já que ``larguraDoIntervalo`` = 1.0 / numeroDeIntervalos, dividir por ``larguraDoIntervalo`` é o mesmo que multiplicar por ``numeroDeIntervalos``. Se multiplicarmos um número na faixa entre 0.0 e 1.0 por ``numeroDeIntervalos``, obtemos um número na faixa entre 0.0 e ``numeroDeIntervalos``. Se arredondarmos este número para baixo, ou seja, para o menor inteiro mais próximo, obtemos exatamente o que estamos procurando - o índice do intervalo::

  numeroDeIntervalos = 8
  intervalos = [0] * numeroDeIntervalos
  for i in lista:
    indice = int(i * numeroDeIntervalos)
    intervalos[indice] = intervalos[indice] + 1

Usamos a função ``int`` para converter um número em ponto flutuante (*float*) para um inteiro.

Existe a possibilidade deste cálculo produzir um índice que esteja fora dos limites (seja negativo ou maior que ``len(intervalos)-1``)?

Uma lista como ``intervalos`` que contém uma contagem do número de valores em cada intervalo é chamada de **histograma**.

  *Como exercício, escreva uma função chamada ``histograma`` que  receba uma lista e um número de intervalos como argumentos e retorne um histograma com o número de intervalos solicitado.*

---------------
9.9 Glossário
---------------

tipo imutável (*immutable type*)
   Um tipo de elemento que não pode ser modificado. Atribuições a um elemento ou "fatiamento (slices)" XXX aos tipos imutáveis causarão erro.

tipo mutável (*mutable type*)
   Tipo de dados onde os elementos podem ser modificados. Todos os tipos mutáveis, são tipos compostos. Listas e dicionários são exemplos de tipos de dados mutáveis. String e tuplas não são.

tupla (*tuple*)
   Tipo sequencial similar as listas com exceção de que ele é imutável. Podem ser usadas Tuplas sempre que um tipo imutável for necessário, por exemplo uma "chave (key)" em um dicionário

Atribuição a tupla (*tuple assignment*)
   Atribuição a todos os elementos de uma tupla feita num único comando de atribução. A atribuição aos elementos ocorre em paralelo, e não em sequência, tornando esta operação útil para *swap*, ou troca recíproca de valores entre variáveis (ex: a,b=b,a).

determinístico (*deterministic*)
   Um programa que realiza a mesma coisa sempre que é executado.

pseudo aleatório (*pseudorandom*)
   Uma sequência de números que parecem ser aleatórios mas são na verdade o resultado de uma computação "determinística"

histograma (*histogram*)
   Uma lista de inteiros na qual cada elemento conta o número de vezes que algo acontece.

casamento de padrão XXX (*pattern matching*)
   Um programa desenvolvido que envolve identificar um teste padrão computacional familiar e copiar a solução para um problema similar.
   
   
