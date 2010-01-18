.. $Id: apendice_b.rst,v 2.1 2007-04-23 21:17:30 luciano Exp $

========================================
Apêndice B: Criando um novo tipo de dado
========================================

.. contents:: Tópicos

Em linguagens com suporte à orientação a objetos, programadores podem criar novos tipos de dados que se comportam de forma semelhante aos tipos de dados built-in. Vamos explorar esse recurso criando uma classe chamada ``Fracao``. Esta classe terá comportamento muito semelhante aos tipos numéricos da linguagem: ``int``, ``long`` e ``float``.

Frações, também conhecidas como números racionais, são valores que podem ser expressos como uma razão de dois números inteiros, por exemplo, 5/6. No exemplo fornecido, o 5 representa o numerador, o número que fica em cima, que é dividido, e o 6 representa o denominador, o número que fica embaixo, pelo qual a divisão é feita. A fração 5/6 pode ser lida "cinco dividido por seis".

O primeiro passo é definir a classe ``Fracao`` com o método ``__init__`` que recebe como parâmetros o numerador e o denominador, sendo ambos do tipo ``int``: ::

 class Fracao:
     def __init__(self, numerador, denominador=1):
         self.numerador = numerador
         self.denominador = denominador

A passagem do denominador é opcional. Uma Fracao com apenas um parâmetro representa um número inteiro. Sendo o numerador n, a fração construída será n/1.

O próximo passo é escrever o método ``__str__`` que exibe as frações corretamente: a forma numerador/denominador. ::

 class Fracao:
     ...
     def __str__(self):
         return "%d/%d" %(self.numerador, self.denominador)

Para testar o que foi feito até aqui, salve a classe ``Fracao`` em um arquivo chamado ``Fracao.py`` e importe-a no interpretador interativo. Criaremos uma instância da classe e imprimiremos ele na tela: 

>>> from Fracao import Fracao
>>> numero = Fracao(5, 6)
>>> print "A fração é ", numero
A fração é 5/6

Como de costume, o comando ``print`` chama implicitamente o método ``__str__``.

-------------------------------
B.1 Multiplicação de frações
-------------------------------

É interessante que nossas frações possam ser somadas, subtraídas, multiplicadas, divididas, etc. Enfim, todas as operações matemáticas das frações. Para que isso seja possível, vamos usar o recurso de sobrecarga de operadores.

Começaremos pela multiplicação por que é a operação mais fácil de ser implementada. Para multiplicar duas frações, criamos uma nova fração, onde o numerador é o produto dos numeradores das frações multiplicadas e o denominador é o produto dos numeradores das frações multiplicadas. O método utilizado em Python para sobrecarga do operador ``*`` chama-se ``__mul__``: ::

 class Fracao:
     ...
     def __mul__(self, other):
         return Fracao(self.numerador * other.numerador,
                       self.denominador * ohter.denominador)
                       
Vamos testar este método criando e multiplicando duas frações:

>>> print Fracao(5, 6) * Fracao(3, 4)
15/24

O método funciona, mas pode ser aprimorado! Podemos melhorar o método visando possibilitar a multiplicação de uma fração por um inteiro. Usaremos a função ``isinstance`` para verificar se o objeto ``other`` é um inteiro, para em seguida convertê-lo em uma fração. ::

 class Fracao:
     ...
     def __mul__(self, other):
         if isinstance(other, int):
             other = Fracao(other)
         return Fracao(self.numerador * other.numerador,
                       self.denominador * ohter.denominador)
        
Agora conseguimos multiplicar funções por inteiros, mas só se a fração estiver à esquerda do operador ``*``. Vejamos um exemplo em que nossa multiplicação funciona e outro no qual ela não funciona:

>>> print Fracao(5, 6) * 4
20/6
>>> print 4 * Fracao(5, 6)
TypeError: __mul__ nor __rmul__ defined for these operands

O erro nos da uma dica: não mexemos em nenhum ``__rmul__``. 

Para realizar a multiplicação, busca no elemento à esquerda do operador ``*`` o método ``__mul__`` compatível com a multiplicação realizada (no nosso caso, que receba um inteiro e uma fração, nesta ordem). Se o método não for encontrado, o Python buscará no elemento à direita do operador ``*`` o método ``__rmul__`` compatível com a multiplicação realizada (que então deve ser lida da direita para a esquerda). Como a multiplicação é lida da direita para a esquerda, temos que o nosso método ``__rmul__`` deve ser igual ao método ``__mul__`` implementado anteriormente.::

 class Fracao:
     ...
     __rmul__ = __mul__

Fazendo assim, dizemos que o método ``__rmul__`` funciona da mesma forma que o método ``__mul__``. Agora, quando multiplicarmos ``4 * Fracao(5, 6)``, o interpretador Python chamará o método ``__rmul__`` do objeto ``Fracao``, passando o 4 como parâmetro.

>>> print 4 * Fracao(5, 6)
20/6

Como o método ``__rmul__`` é também o método ``__mul__``, e o método ``__mul__`` consegue trabalhar com parâmetro do tipo inteiro, nossa multiplicação está completa.

-------------------------------
B.2 Soma de frações
-------------------------------

Somar é mais complicado do que multiplicar, pelo menos quando estamos somando frações e temos que implementar isso em uma linguagem de programação. Mas não se assuste, não é tão complicado assim. A soma de a/b com c/d é (a*d+c*b)/(b*d).

Tomando a multiplicação como base, podemos facilmente implementar os métodos ``__add__`` e ``__radd__``: ::

 class Fracao:
     ...
     def __add__(self, other):
         if isinstance(other, int):
             other = Fracao(other)
         return Fracao(self.numerador   * other.denominador + 
                       self.denominador * other.numerador,
                       self.denominador * other.denominador)
     
     __radd__ = __add__

Podemos testar o método usando frações e inteiros:

>>> print Fracao(5, 6) + Fracao(5, 6)
60/36
>>> print Fracao(5, 6) + 3
23/6
>>> print 2 + Fracao(5, 6)
17/6

Os dois primeiros exemplos chamam o método ``__add__``, enquanto o último exemplo chama o método ``__radd__``.

-------------------------------------------------------
B.3 Simplificando frações: O algoritmo de Euclides
-------------------------------------------------------

No exemplo anterior, calculamos a soma de 5/6 com 5/6 e obtivemos o resultado 60/36. O resultado está correto, porém não está representado na melhor forma possível. O ideal é simplificarmos a fração. Para simplificar ao máximo esta fração, devemos dividir o numerador e o denominador pelo máximo divisor comum (MDC) deles, que é 12. Fazendo isso, chegamos à forma mais simples da fração, que é 5/3.

De forma geral, sempre que um objeto do tipo ``Fracao`` for criado, a fração deve ser simplificada, através da divisão do numerador e do denominador pelo seu MDC. Quando a fração já está em sua forma mais simples, o MDC vale 1.

Euclides de Alexandria (aprox. 325 a. C. -- 365 a. C.) desenvolveu um algoritmo para encontrar o MDC de dois inteiros ``m`` e ``n``:

    Se ``n`` é múltiplo de ``m``, então ``n`` é o MDC. Caso contrário, o MDC é o MDC de ``n`` e o resto da divisão de ``m`` por ``n``.
    
Esta definição recursiva pode ser representada de forma concisa pela função: ::

 def mdc(m, n):
     if m % n == 0:
         return n
     else:
         return mdc(n, m % n)

Na primeira linha da função, utilizamos o operador de módulo para checar se ``m`` é divisível por ``n``. Na última linha, usamos o mesmo operador para obter o resto da divisão de ``m`` por ``n``.

Já que todas as operações que escrevemos criam um novo objeto do tipo ``Fracao``, podemos utilizar a função ``mdc`` no método ``__init__`` de nossa classe: ::

 class Fracao:
     def __init__(self, numerador, denominador=1):
         m = mdc(numerador, denominador)
         self.numerador = numerador / m
         self.denominador = denominador / m 

Agora, sempre que criarmos uma fração, ela será reduzida:

>>> Fracao(100, -36)
-25/9

Sempre que o denominador é negativo, o sinal negativo deve passar para o numerador. O interessante é que, ao usarmos o Algoritmo de Euclides, esta operação ocorre de forma transparente.

Antes de seguirmos para o próximo passo, vamos ver como está nossa classe ``Fracao`` completa? 

::

 class Fracao:
     def __init__(self, numerador, denominador=1):
         m = mdc(numerador, denominador)
         self.numerador = numerador / m
         self.denominador = denominador / m
     
     def __str__(self):
         return "%d/%d" %(self.numerador, self.denominador)
     
     def __mul__(self, other):
         if isinstance(other, int):
             other = Fracao(other)
         return Fracao(self.numerador * other.numerador,
                       self.denominador * ohter.denominador)
     
     __rmul__ = __mul__
     
     def __add__(self, other):
         if isinstance(other, int):
             other = Fracao(other)
         return Fracao(self.numerador   * other.denominador + 
                       self.denominador * other.numerador,
                       self.denominador * other.denominador)
     
     __radd__ = __add__

-------------------------------
B.4 Comparando frações
-------------------------------

Suponha que tenhamos duas frações (instâncias da classe ``Fracao``), ``a`` e ``b``, e nós fazemos a comparação ``a == b``. A implementação padrão do operador ``==`` realiza um "teste raso", ou seja, verifica se ``a`` e ``b`` são o mesmo objeto.

Queremos personalizar este retorno, de forma que a comparação retorne ``True`` se ``a`` e ``b`` tiverem o mesmo valor, o que é chamado de "teste profundo".

Temos que ensinar às frações como elas devem se comparar. Como foi visto na seção 15.4, todos os operadores de comparação podem ser sobrecarregados por apenas um método: ``__cmp__``.

Por convenção, o método ``__cmp__`` retorna um número negativo se ``self`` for menor que ``other``, zero se eles forem iguais e um número positivo se ``self`` for maior que ``other``.

A forma mais simples de comparar frações é através da multiplicação cruzada (denominador * numerador e vice-versa). Se ``a/b > c/d``, então ``ad > bc``. Tendo isso em mente, vamos criar o ``__cmp__``: ::

 class Fracao:
     ...
     def __cmp__(self, other):
         diferenca = (self.numerador * other.denominador -
                      self.denominador * other.numerador)
         return diferenca
         
Se ``self`` for maior que ``other``, a ``diferenca`` será positiva. Se ``other`` for maior, a ``diferenca`` será negativa. Se os dois forem iguais, a ``diferenca`` será zero.

-------------------------------
B.5 Indo mais além...
-------------------------------

Obviamente, não terminamos de representar uma fração. Ainda temos que implementar a subtração sobrescrevendo o método ``__sub__`` e a divisão sobrescrevendo o método ``__div__``.

Uma forma de tratar tais operações é sobrescrever os métodos de negação (``__neg__``) e de inversão (``__invert__``). Assim, podemos fazer a subtração através da negação do elemento à direita do operador e somando, e podemos fazer a divisão através da inversão do elemento à direita do operador e multiplicando.

Depois, temos que implementar os métodos ``__rsub__`` e ``__rdiv__``. Infelizmente, não podemos utilizar o mesmo "macete" utilizado para multiplicação e soma, por que a divisão e a subtração não são comutativas, ou seja, a ordem dos fatores altera o resultado final.

As negações unárias, que representam o uso do sinal de negação com apenas um elemento, são implementadas através da sobrescrita do método ``__neg__``.

Potências podem ser calculadas através do método ``__pow__``, mas a implementação é um pouco complicada. Se o expoente da potência não for um inteiro, o resultado provavelmente não poderá ser representado como uma fração. Por exemplo, ``Fracao(2) ** Fracao(2)`` é a raiz quadrada de 2, que é um número irracional, e números irracionais não pode ser representados por frações. Logo, é uma tarefa complicada implementar uma versão genérica do método ``__pow__``.

Existe, ainda, uma outra extensão para a classe ``Fracao`` que pode vir à mente. Até aqui, assumimos que o numerador e o denominador são números inteiros.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
B.5.1 Exercício
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Como exercício, finalize a implementação da classe ``Fracao``, tornando-a capaz de tratar subtração, divisão e potenciação.

-------------------------------
B.6 Glossário
-------------------------------

máximo divisor comum (MDC)
    O maior inteiro positivo que tem como múltiplo o numerador e o denominador de uma fração.

negação unária
    É a operação que calcula a inversão de um elemento, usualmente representada com um sinal de menos ``-`` à esquerda do elemento. É chamada unária pelo contraste com a operação binária que usa o sinal de menos, a subtração.

simplificar
    Transformar uma fração em sua equivalente com o MDC valendo 1
