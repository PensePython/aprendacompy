.. $Id: capitulo_18.rst,v 2.1 2007-04-23 21:17:40 luciano Exp $

===================
Capítulo 18: Pilhas
===================

.. contents:: Tópicos

18.1 Tipos abstratos de dados
-------------------------------

Os tipos de dados que você viu até agora são todos concretos, no sentido que nós especificamos completamente como eles são implementados. Por exemplo, a classe Card(*XXX ver como foi traduzido*) representa uma carta utilizando dois inteiros. Como discutimos no momento, esta não é a única maneira de representar uma carta; existem muitas implementações alternativas.

Um **tipo abstrato de dado**, ou TAD, especifica um conjunto de operações (ou métodos) e a semântica das operações (o que elas fazem), mas não especifica a implementação das operações. Isto é o que o faz abstrato.

Por que isto é útil?

  - Simplifica a tarefa dde especificar um algoritmo se você pode XXXdenotar(*denote*) as operações que você precisa sem ter que pensar, ao mesmo tempo, como as operações são executadas.

  - Uma vez que existem geralmente muitas maneiras de implementar um TAD, pode ser útil escrever um algritmo que pode ser usado com qualquer das possíveis implementações.

  - TADs bastante conhecidos, como o TAD Pilha deste capítulo, já estão implementados em bibliotecas padrão, então eles podem ser escritos uma vez e usado por muitos programadores.

  - As operações em TADs provêm uma linguagem de alto nível comum para especificar e falar sobre algoritmos.

Quando falamos sobre TADs, geralmente distinguimos o código que usa o TAD, chamado **cliente**, do código que implementa o TAD, chamado código **fornecedor**.


18.2 O TAD Pilha
------------------


Neste capítulo, iremos olhar um TAD comum, a **pilha**. Uma pilha é uma coleção, ou seja, é uma estrutura de dados que contei múltiplos elementos. Outras coleções que vimos incluem dicionários e listas.

Um TAd é definido pelo conjunto de operações que podem ser executadas nele, que é chamado **interface**. A interface para uma pilha consiste nestas operações:

``__init__`` : Inicializa uma nova pilha vazia.

``push`` : Adiciona um novo item na pilha

``pop`` : Remove um ítem da pilha e o retorna, O ítem que é retornadao é sempre o último adicionado.

``isEmpty`` : Verifica se a pilha está vazia.

Uma às vezes é chamada uma estrutura de dados "last in, first out" ou LIFO, porque o último ítem adicionad é o primeiro a ser removido.


18.3 Implementando pilhas com listas de Python
------------------------------------------------

As operações de lista que Python oferecem são similares às operações que definem uma pilha. A interface não é exatamente o que se supõe ser, mas podemos escrever um código para traduzir do TAD Pilha para as operações nativas.

Este código é chamado uma **implementação** do TAD Pilha. Geralmente, uma implementaçõa é um conjunto de métodos que satisfazem os requisitos sintáticos e semânticos de uma interface.

Aqui está uma implementação do TAD Pilha que usa uma lista do Python:

::

  class Stack :
    def __init__(self) :
      self.items = []

    def push(self, item) :
      self.items.apend(item)

    def pop(self) :
      return self.items.pop()

    def isEmpty(self) :
      return (self.items == [])

Um objeto ``Stack`` contém um atributo chamado ``items`` que é uma lista de ítens na pilha. O método de inicialização define items como uma lista vazia.

Para adicionar um novo ítem na pilha, ``push`` o coloca em ``items``. Para remover um ítem da pilha, pop usa o método de lista homônimo¹ para remover e retornar um último ítem da lista.

Finalmente, para verificar se a pilha está vazia, ``isEmpty`` comprara items a uma lista vazia.

Uma implementação como esta, na qual os métodos consistem de simples invocações de métodos existentes, é chamado **revestimento**. Na vida real, revestimento é uma fina camada de madeira de boa qualidade usado em XXX*furniture-making* para esconder madeira de menor qualidade embaixo. Cientistas da Computação usam esta metáfora para descrever um pequeno trecho de código que esconde os detalhes de uma implementação e fornece uma interface mais simples, ou mais padronizada.

18.4 Empilhando e desempilhando
---------------------------------

Uma pilha é uma **estrutura de dados genérica**, o que significa que podemos adicionar qualquer tipo de ítem a ela. O exemplo a seguir empilha dois inteiros e uma XXXstring na pilha:

  >>> s = Stack()
  >>> s.push(54)
  >>> s.push(45)
  >>> s.push("+")

Podemos usar ``isEmpty`` e pop para remover e imprimir todos os ítens da pilha:

  while not s.isEmpty() :
    priint s.pop()

A saída é + 45 54. Em outras palavras, usamos a pilha para imprimir os ítens ao contrário! Sabidamente, este não é o formato padrão de imprimir uma lista, mas, usando uma pilha, foi notavelmente fácil de fazer.

Você deve comparar este trecho de código com a implementação de `printBackward` na seção 17.4. Existe um paralelo natura entre a versão recursiva de `printBackward` e o algoritmo de pilha aqui. A diferenã é que printBackward usa a pilha de execução para XXXmanter a trilha(keep track) dos nós enquanto percorre a lista, e então imprime-a no retorno da recursão. o algoritmo de pilha faz a mesma coisa, exceto que usa o objeto Stack ao invés da pilha de execução.

18.5 Usando uma pilha para avaliar expressões pós-fixas
----------------------------------------------------------

Em muitas linguagens de programação, expressões matemáticas são executadas com o poerador entre os roid operandos, como em 1 + 2. Este formato é chamado notação **infixa**. Uma alternativa usada por algumas calculadoras é chamada notação **pós-fixa**. Em notação pós-fixa, o operador segue os operandos, como em 1 2 +. 

A razão pela qual a notação pós-fixa é útil algumas vezes é que existe uma maneira natural de avaliar uma expressão pós-fixa usando uma pilha:

  - começando no início da expressão, peque um termo (operador ou operando) de cada vez.
  - Se o termo é um operando, empilhe-o
  - Se o termo é um operador, desempilhe dois operandos, execute a operação neles, e empilhe o resultado.
  - Quando chegar ao fim da expressão, deve existir exatamente um operando sobrando na pilha. Este operando é o resultado.

  * Como um exercício, aplique este algoritmo à expressão 1 2 + 3 * .

Este exemplo demonstra uma das vantagens da notação pós-fixa - não é necessário usar parênteses para controlar a ordem das operações. Para ter o mesmo resultado em notação infixa, deveríamos escrever (1 + 2) * 3.

  * Como um exercício, escreva a expressão pós-fixa que é equivalente a 1 + 2 * 3.


18.6 Análise sintática
-------------------------

Para implementar o algoritmo anterior, necessitamos estar prontos para percorrer uma string e quebrá-la em operandos e operadores. Este processó é um exemplo de **XXXparsing**, e o resultado - os pedaços da string - são chamados **XXXtokens**. Você deve lembrar estas palavras do capítulo 1.

Python fornece um método split nos módulos string e re (expressões regulares). A função ``string.split`` separa uma string numa lista usando um único caracter como **delimitador**. Por exemplo:

  >>> import string
  >>> string.split ("Now is the time", " ")
   ['Now', 'is', 'the', 'time']

Neste caso, o delimitador é o caracter de espaço, então a string é dividida a cada espaço.

A função ``re.split`` é mais poderosa, permitindo-nos fornecer uma expresão regular ao invés de um delimitador. Uma expressão regular é uma maneira de especificar um conjunto de strings. Por exemplo, [A-z] é o conjunto de todas as letras e [0-9] é o conjunto de todos os dígitos. O operador ^nega um conunto, então [^0-9] é o conjunto de tudo o que não é número, que é exatamente o que queremos para dividir expressões pós-fixas.

  >>> import re
  >>> re.split ("[^0-9]", "123+456*/")
   ['123', '+', '456', '*', '', '/', ' ']

Note que a ordem dos argumentos é diferente de string.split, o delimitador vem antes da string.

A lista resultante inclui os operandos ``123`` e ``456``, e os operadores ``*`` e ``/``. Também inclui duas strings vazias que são inseridas depois dos operadores.


18.7 Avaliando em pós-fixo.
------------------------------

Para avaliar uma expressão pós-fixa, usaremos o parser da seção anterior e o algoritmo da seção anterior a ela. Para manter as coisas simples, começaremos com um avaliador que implementa somente os operadores ``+`` e  .

::

  def evalPostfix (expr) :
    import re 
    tokenList = re.split ("([^0-9])", expr) 
    stack = Stack() 
    for token in tokenList 
      if token == '' or token = ' ' :
        continue
      if token == '+' :
        sum = stack.pop() + stack.pop()
        stack.push(sum)
      if token == '*' :
        product = stack.pop() * stack.pop()
        stack.push(product)
      else:
        stack.push(int(token))
    return stack.pop()


A primeira condição cuida de espaços e strings vazias. As duas próximas condições manipulam os operadores. Nós assumimos, agora que qualquer coisa é um operador. É claro, seria melhor chegar por entrada errônea e enviar uma mensagem de erro, mas faremos isto depois.

Vamos testá-lo avaliando a forma pós-fixa de ``(56 + 47) * 2``

  >>> print evalPostfix("56 47 + 2 *")
   206

XXXthat's close enough

18.8 Clientes de fornecedores.

Um dos objetivos de um TAD é separar os interesses do fornecedor, quem escreve o código que implementa o TAD, e o cliente, que usa o TAD. O fornecedor tem que se preocupar apenas se a implementação está correta  - de acordo com a especificação do TAD - e não como ele será usado.

Inversamente, o cliente assume que a implementação do TAD está correta e não se preocupa com os detalhes. Quando você está usando um tipo nativo do Python, tem o luxo de pensar exclusivamente como um cliente.

É claro, quanto você implementa um TAD, você também tem que escrever código cliente para testá-lo. Neste caso, você faz os dois papéis, o que pode ser confuso. Você deve fazer algum esforçõ para manter a trilha do papel que está fazendo a cada momento.

---------------
18.9 Glossário
---------------

 
tipo abstrato de dados (TAD) (*abstract data type(ADT)*): 
     Um tipo de dado(geralmente uma coleção de objetos) que é definidopor um conjunto de operações, que podem ser implementadas de várias maneiras.

interface (*interface*):
     É o conjunto de operações que definem um TDA.

implementação (*implementation*):
     Código que satisfaz(preenche?) os requisitos sintáticos e semânticos de uma interface.

cliente (*client*):
     Um programa (ou o programador que o escreveu) que faz utilização de um TDA.

fornecedor (*provider*):
     Código (ou o programador que o escreveu) que implementa um TDA.

revestimento (*veneer*):
     Definição de classe que implementa um TDA com definições de métodos que são chamadas a outros métodos, às vezes com pequenas modificações. A lâmina faz um trabalho insignificante, mas melhora ou padroniza a interface dada ao cliente.

estrutura de dados genérica (*generic data structure*): 
     Tipo de estrutura de dados que contem data de um tipo qualquer(tipo genérico).

infixa (*infix*):
     Notação matemática em que os operadores se situam entre os operandos.

pós-fixa (*postfix*):
     Notação matemática em que os operadores se situam após os operandos.

XXX parse (*parse*):
     Ler um conjunto de caracteres(string de caracteres) ou tokens(símbolos atômicos) e analisar sua estrutura gramatical.

XXX token (*token*):
     Conjunto de caracteres que são tratados como uma unidade atômica para fins de análise gramatical, como as palavras na linguagem natural.

delimitador (*delimiter*):
     Um caracter que é utilizado para separar os símbolos atômicos(tokens), como a pontuação na linguagem natural.
     
     
