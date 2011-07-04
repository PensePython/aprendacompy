.. $Id: capitulo_15.rst,v 2.1 2007-04-23 21:17:39 luciano Exp $

=================================
Capítulo 15: Conjuntos de objetos
=================================

.. contents:: Tópicos

---------------
15.1 Composição
---------------

Até agora, você vio diversos exemplos de composição. Um dos primeiros exemplos foi o uso de uma invocação de método como parte de uma expressão. Outro exemplo é a estrutura aninhada dos comandos: você pode pôr um comando ``if`` dentro de um laço ``while``, dentro de outro comando ``if``, e assim por diante.

Tendo visto este padrão, e tendo aprendido a respeito de listas e objetos, você não deveria ficar surpreso em aprender que você pode criar listas de objetos. Você também pode criar obejtos que contêm listas (como atritos); você pode criar listas que contêm listas; você pode criar objetos que contêm objetos; e assim por diante.

Neste capítulo e no próximo, você irá ver alguns exemplos destas combinações, usando objetos ``Carta`` como exemplo.
 
----------------------
15.2 Objetos ``Carta``
---------------------- 

Se você não estiver familiarizado com jogos de cartas, agora é um bom momento para conseguir um baralho, ou então esse capítulo pode não fazer muito sentido. Há 52 cartas em um baralho, cada uma das quais pertence a um dos quatro naipes e a uma das treze posições. Os naipes são Espadas, Copas, Ouros e Paus (em ordem descendente no *bridge*). As posições são Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete, Rainha e Rei. Dependendo do jogo, a posição do Ás pode ser maior do que a do Rei ou menor do que a do 2.

Se quisermos definir um novo objeto para representar uma carta, é óbvio que os atributos devem ser ``posicao`` e ``naipe``. Não tão óbvio são os tipos aos quais devem pertencer os atributos. Uma possibilidade é usar strings contendo palavras como "``Espada``" para naipes e "``Rainha``" para posições. Um problema com esta implementação é que não seria fácil comparar cartas para ver qual possui o maior naipe ou posição.

Uma alternativa é usar inteiros para **codificar** as posições e naipes. "Codificar", neste caso, não significa o mesmo que as pessoas normalmente pensam, que é criptografar ou traduzir para um código secreto. O que um cientista da computação quer dizer com "codificar" é "definir um mapeamento entre uma seqüência de números e os itens que eu quero representar". Por exemplo:

- Espadas -> 3

- Copas   -> 2

- Ouros   -> 1

- Paus    -> 0

Uma característica óbvia deste mapeamento é que os naipes são mapeados para inteiros na ordem, de modo que nós podemos comparar naipes pela comparação de inteiros. O mapeamento de posições é bastante óbvio. Cada uma das posições numéricas mapeia para o inteiro correspondente e, as cartas com figura são mapeadas conforme abaixo:

- Valete -> 11

- Rainha -> 12

- Rei    -> 13

O motivo pelo qual nós estamos usando notação matemática para estes mapeamentos é que eles não são parte do programa Python. Eles são parte do projeto do programa, mas eles nunca aparecem explicitamente no código. A definição de classe para o tipo ``Carta`` fica parecida com esta::

  class Carta:
    def __init__(self, naipe=0, posicao=0):
      self.naipe = naipe
      self.posicao = posicao

Como sempre, nós fornecemos um método de inicialização que recebe um parâmetro opcional para cada atributo.

Para criar um objeto que representa o 3 de Paus, usa-se este comando::

  tresDePaus = Carta(0, 3)

O primeiro argumento, 0, representa o naipe de Paus.

-----------------------------------------------
15.3 Atributos de classe e o método ``__str__``
-----------------------------------------------

Para imprimir objetos ``Carta`` de uma maneira que as pessoas possam facilmente ler, nós gostaríamos de mapear os códigos inteiros para palavras. Uma forma natural de fazer isso é usar listas de strings. Nós atribuímos estas listas para **atributos de classe** no topo da definição de classe::

  class Carta:
    listaDeNaipes = ["Paus", "Ouros", "Copas", "Espadas"]
    listaDePosicoes = ["narf", "Ás", "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "Valete", "Rainha", "Rei"]

    # método init omitido

    def __str__(self):
      return (self.listaDePosicoes[self.posicao] + " de " +
              self.ListaDeNaipes[self.naipe])

Um atributo de classe é definido fora de qualquer método, e ele pode ser acessado por quaisquer métodos da classe.

Dentro de ``__str__``, nós podemos usar ``listaDeNaipes`` e ``listaDePosicoes`` para mapear os valores numéricos de ``naipe`` e ``posicao`` para strings. Por exemplo, a expressão ``self.listaDeNaipes[self.naipe]`` significa "use o atributo ``naipe`` do objeto ``self`` como um índice para o atributo de classe chamado ``listaDeNaipes``, e selecione a string apropriada".

O motivo para o "``narf``" no primeiro elemento em ``listaDePosicoes`` é preencher o lugar do 0-ésimo elemento da lista, que nunca será usado. As únicas posições válidas são de 1 a 13. Este item desperdiçado não é inteiramente necessário. Nós poderíamos ter iniciado com 0, como é normal. Porém, é menos confuso codificar 2 como 2, 3 como 3, e assim por diante.

Com os métodos que nós temos até agora, nós podemos criar e imprimir cartas::

  >>> carta1 = Carta(1, 11)
  >>> print carta1
  Valete de Ouros

Atributos de classe como ``listaDeNaipes`` são compartilhados por todos os objetos ``Carta``. A vantagem disso é que nós podemos usar qualquer objeto ``Carta`` para acessar os atributos de classe::

  >>> carta2 = Carta(1, 3)
  >>> print carta2
  3 de Ouros
  >>> print carta2.listaDeNaipes[1]
  Ouros

A desvantagem é que se nós modificarmos um atributo de classe, isso afetará cada instância da classe. Por exemplo, se nós decidirmos que "Valete de Ouros" deveria realmente se chamar "Valete de Baleias Rodopiantes", nós poderíamos fazer isso::

  >>> carta1.listaDeNaipes[1] = "Baleias Rodopiantes"
  >>> print carta1
  Valete de Baleias Rodopiantes

O problema é que *todos* os Ouros se tornam Baleias Rodopiantes::

  >>> print carta2
  Valete de Baleias Rodopiantes

Normalmente, não é uma boa idéia modificar atributos de classe.

----------------------
15.4 Comparando cartas
----------------------

Para tipos primitivos, existem operadores condicionais (<, >, ==, etc.) que comparam valores e determinam quando um é maior que, menor que ou igual a outro. Para tipos definidos pelo usuário, nós podemos sobrescrever o comportamento dos operadores pré-definidos fornecendo um método ``__cmp__``. Por convenção, ``__cmp__`` recebe dois parâmetros, ``self`` e ``other``, e retorna 1 se o primeiro objeto for maior, -1 se o segundo objeto for maior, e 0 se eles forem iguais.

Alguns tipos são totalmente ordenados, o que significa que nós podemos comparar quaisquer dois elementos e dizer qual é o maior. Por exemplo, os inteiros e os números de ponto flutuante são totalmente ordenados. Alguns conjuntos são não-ordenados, o que significa que não existe maneira significativa de dizer que um elemento é maior que o outro. Por exemplo, as frutas são não-ordenadas, e é por isso que não podemos comparar maçãs e laranjas.

O conjunto de cartas de jogo é parcialmente ordenado, o que significa que às vezes você pode comparar cartas, e às vezes não. Por exemplo, você sabe que o 3 de Paus é maior do que o 2 de Paus, e que o 3 de Ouros é maior do que o 3 de Paus. Mas qual é o melhor, o 3 de Paus ou o 2 de Ouros? Um tem uma posição maior, mas o outro tem um naipe maior.

Para tornar as cartas comparáveis, você tem que decidir o que é mais importante: posição ou naipe. Para ser honesto, a escolha é arbitrária. Por questão de escolha, nós iremos dizer que naipe é mais importante, porque um baralho de cartas novo vem ordenado com todas as cartas de Paus juntas, seguidas pelas de Ouros, e assim por diante.

Com essa decisão, nós podemos escrever ``__cmp__``::

  def __cmp__(self, other):
    # verificar os naipes
    if self.naipe > other.naipe: return 1
    if self.naipe < other.naipe: return -1
    # as cartas têm o mesmo naipe... verificar as posições
    if self.posicao > other.posicao: return 1
    if self.posicao < other.posicao> return -1
    # as posições são iguais... é um empate
    return 0

Nesta ordenação, Ases são menores do que 2.

  *Como um exercício, modifique ``__cmp__``, de modo que os Ases sejam maiores do que os Reis.*

-------------
15.5 Baralhos
-------------

Agora que nós temos objetos para representar ``Cartas``, o próximo passo lógico é definir uma classe para representar um ``Baralho``. É claro que um baralho é formado por cartas; portanto, cada objeto ``Baralho`` irá conter uma lista de cartas como um atributo.

A seguir, damos uma definição para a classe ``Baralho``. O método de inicialização cria o atributo ``cartas`` e gera o conjunto padrão de 52 cartas::

  classe Baralho
    def __init__(self):
      self.cartas = []
      for naipe in range(4):
        for posicao in range(1, 14):
          self.cartas.append(Carta(naipe, posicao))

A maneira mais fácil de popular o baralho é com um laço aninhado. O laço externo enumera os naipes de 0 até 3. O laço interno enumera as posições de 1 até 13. Como o laço externo repete quatro vezes e o laço interno 13 vezes, o número total de vezes que o corpo é executado é 52 (13 vezes quatro). Cada iteração cria uma nova instância de ``Carta`` com o naipe e posição atuais e a inclui na lista ``cartas``.

O método ``append`` trabalha sobre listas mas não, obviamente, sobre tuplas.

-------------------------
15.6 Imprimindo o baralho
-------------------------

Como sempre, quando nós definimos um novo tipo de objeto, nós gostaríamos de ter um método para imprimir o conteúdo de um objeto. Para imprimir um ``Baralho``, nós percorremos a lista e imprimimos cada ``Carta``::

  class Baralho:
    ...
    def imprimirBaralho(self):
      for carta in self.cartas:
        print carta

Aqui, e a partir daqui, as reticências (...) indicam que nós omitimos os outros métodos da classe.

Como uma alternativa a ``imprimirBaralho``, nós poderíamos escrever um método ``__str__`` para a classe ``Baralho``. A vantagem de ``__str__`` é que ela é mais flexível. Em vez de apenas imprimir o conteúdo de um objeto, ela gera uma representação em string que outras partes do programa podem manipular antes de imprimir ou armazenar para uso posterior.

Abaixo, uma versão de ``__str__`` que devolve uma representação em string de um ``Baralho``. Para adicionar um pouco de estilo, ela distribui as cartas em uma cascata, na qual cada carta é indentada um espaço a mais do que a carta anterior::

  class Baralho:
    ...
    def __str__(self):
      s = ""
      for i in range(len(self.cartas)):
        s = s + " "*i + str(self.cartas[i]) + "\n"
      return s

Este exemplo demonstra diversas características. Primeiro, em vez de percorrer ``self.cartas`` e atribuir cada carta a uma variável, nós estamos usando ``i`` como uma variável de laço e um índice para a lista de cartas.

Segundo, nós estamos usando o operador de multiplicação de strings para indentar cada carta com um espaço adicional com relação à anterior. A expressão ``" "*i`` produz um número de espaços igual ao valor atual de ``i``.

Terceiro, em vez de usar o comando ``print`` para imprimir as cartas, nós usamos a função ``str``. Passar um objeto como um argumento para ``str`` equivale a invocar o método ``__str__`` sobre o objeto.

Finalmente, nós estamos usando a variável ``s`` como um **acumulador**. Inicialmente, ``s`` é a string vazia. A cada repetição do laço, uma nova string é gerada e concatenada com o valor antigo de ``s`` para obter um novo valor. Quando o laço termina, ``s`` contém a representação em string completa do ``Baralho``, que se parece com::

  >>> baralho = Baralho()
  >>> print Baralho
  Ás de Paus
   2 de Paus
    3 de Paus
     4 de Paus
      5 de Paus
       6 de Paus
        7 de Paus
         8 de Paus
          9 de Paus
           10 de Paus
            Valete de Paus
             Rainha de Paus
              Rei de Paus
               Ás de Ouros

E assim por diante. Mesmo que o resultado apareça em 52 linhas, é uma string longa que contém *newlines*.

-----------------
15.7 Embaralhando
-----------------

Se um baralho estiver perfeitamente embaralhado, então cada carta tem a mesma probabilidade de aparecer em qualquer lugar no baralho, e qualquer localização no baralho tem a mesma probabilidade de conter qualquer carta.

Para embaralhar as cartas, nós usaremos a função ``randrange`` do módulo ``random``. Com dois argumentos inteiros, ``a`` e ``b``, ``randrange`` escolhe um inteiro aleatório no intervalo ``a <= x < b``. Como o limite superior é estritamente menor que ``b``, nós podemos usar o comprimento de uma lista como o segundo parâmetro, e nós garantimos que o índice sempre será válido. Por exemplo, esta expressão escolhe o índice de uma carta aleatória em um baralho::

  random.randrange(0, len(self.cartas))

Uma maneira fácil de embaralhar as cartas é percorrer a lista e trocar cada carta por outra escolhida aleatoriamente. É possível que a carta seja trocada por ela mesma, mas isso não é problema. Na verdade, se nós excluíssemos essa possibilidade, a ordem das cartas não seria totalmente aleatória::

  class Baralho:
    ...
    def embaralhar(self):
      import random
      nCartas = len(self.cartas)
      for i in range(nCartas):
        j = random.randrange(i, nCartas)
        self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

Em vez de assumir que existem 52 cartas no baralho, nós obtivemos o comprimento real da lista e o guardamos na variável ``nCartas``.

Para cada carta no baralho, nós escolhemos uma carta aleatória dentre as cartas que ainda não foram embaralhadas. Então, nós trocamos a carta atual (``i``) pela carta selecionada (``j``). Para trocar as cartas, nós usamos uma atribuição de tupla, como visto na Seção 9.2::

  self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]


*Como exercício, reescreva esta linha de código sem usar uma atribuição de seqüência.*

------------------------------------
15.8 Removendo e distribuindo cartas
------------------------------------

Outro método que pode ser útil para a classe ``Baralho`` é ``removerCarta``. Ele recebe uma carta como parâmetro, remove-a do baralho e retorna verdadeiro (1), se a carta estava no baralho e falso (0), caso contrário::

  class Baralho:
    ...
    def removerCarta(self, carta):
      if carta in self.cartas:
        self.cartas.remove(carta)
        return 1
      else
        return 0

O operador ``in`` retorna verdadeiro se o primeiro operando estiver contido no segundo, que deve ser uma lista ou uma tupla. Se o primeiro operando for um objeto, Python usa o método ``__cmp__`` do objeto para determinar igualdade com os itens da lista. Como o método ``__cmp__`` da classe ``Carta`` verifica por igualdade profunda, o método ``removerCarta`` também testa por igualdade profunda.

Para distribuir as cartas, nós iremos remover e devolver a carta do topo. O método de lista ``pop`` fornece uma maneira conveniente de fazer isso::

  class Baralho:
    ...
    def distribuirCarta(self):
      return self.cards.pop()

Na verdade, ``pop`` remove a *última* carta da lista. Portanto, nós estamos realmente distribuindo as cartas do fim para o início do baralho.

Uma última operação que nós poderíamos querer é a função booleana ``estahVazio``, que retorna verdadeiro se o baralho não contém cartas::

  class Baralho:
    ...
    def estahVazio(self):
      return (len(self.cartas) == 0)

--------------
15.9 Glossário
--------------

**codificar** (*encode*) 
  Representar um conjunto de valores usando outro conjunto de valores,  construindo um mapeamento entre eles.

**atributo de classe** (*class atribute*)
  Uma variável que é definida dentro de uma definição de classe, mas fora de qualquer método. Atributos de classe podem ser acessados a partir de qualquer método da classe e são compartilhados por todas as instâncias da classe.

**acumulador** (*accumulator*)
  Uma variável usada em um laço para acumular uma série de valores, para, por exemplo, concatená-los em uma string ou somá-los a uma soma em andamento.

