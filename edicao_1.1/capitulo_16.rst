.. $Id: capitulo_16.rst,v 2.4 2007-04-23 21:17:40 luciano Exp $

====================
Capitulo 16: Herança
====================

.. contents:: Tópicos

--------------
16.1 Herança
--------------

Uma das características mais marcantes das linguagens orientadas a objetos é a **herança**. Herança é a habilidade de definir uma nova classe que é uma versão modificada de uma classe existente.

A principal vantagem dessa característica é que você pode adicionar novos métodos a uma classe sem ter que modificar a classe existente. Chama-se "herança" porque a nova classe herda todos os métodos da classe existente. Ampliando a metáfora, podemos dizer que a classe existente é às vezes chamada de classe **mãe** (*parent*). A nova classe pode ser chamada de classe **filha** ou, simplesmente, "subclasse".

A herança é uma característica poderosa. Alguns programas que seriam complicados sem herança podem ser escritos de forma simples e concisa graças a ela. E a herança também pode facilitar o reuso do código, uma vez que você pode adaptar o comportamento de classes existentes sem ter que modificá-las. Em alguns casos, a estrutura da herança reflete a natureza real do problema, tornando o programa mais fácil de entender.

Por outro lado, a herança pode tornar um programa seja difícil de ler. Quando um método é invocado, às vezes não está claro onde procurar sua definição. A parte relevante do código pode ser espalhada em vários módulos. E, também, muitas das coisas que podem ser feitas utilizando herança também podem ser feitas de forma igualmente elegante (ou até mais) sem ela. Se a estrutura natural do problema não se presta a utilizar herança, esse estilo de programação pode trazer mais problemas que vantagens.

Nesse capítulo, vamos demonstrar o uso de herança como parte de um programa que joga uma variante de Mico. Um dos nossos objetivos é escrever um código que possa ser reutilizado para implementar outros jogos de cartas.

-----------------------
16.2 Uma mão de cartas
-----------------------

Para quase todos os jogos de baralho, é preciso representar uma mão de cartas. Uma mão de cartas é similar a um maço de baralho. Porque ambos são formados por uma série de cartas e ambos requerem operações, como, adicionar e remover cartas. Fora isso, a habilidade de embaralhar a mão e o baralho também são úteis.

Mas, ao mesmo tempo, a mão é também diferente do baralho. Dependendo do jogo que está sendo jogado, precisamos realizar algumas operações nas mãos de cartas que não fazem sentido para o baralho inteiro. Por exemplo, no pôquer, podemos classificar uma mão (trinca, flush, etc.) ou compará-la com outra mão. No jogo de bridge, podemos querer computar a quantidade de pontos que há numa mão, a fim de fazer um lance.

Essa situação sugere o uso de herança. Se ``Mao`` é uma subclasse de ``Baralho``, terá todos os métodos de ``Baralho``, e novos métodos podem ser adicionados.

Na definição de classe, o nome da classe pai aparece entre parênteses::

 class Mao(Baralho):
   pass

Esse comando indica que a nova classe ``Mao`` herda da classe existente ``Baralho``.

O construtor de ``Mao`` inicializa os atributos da mão, que são ``nome`` e ``cartas``. A string ``nome`` identifica essa mão, provavelmente pelo nome do jogador que está segurando as cartas. O nome é um parâmetro opcional com a string vazia como valor default. ``cartas`` é a lista de cartas da mão, inicializada com uma lista vazia ::

 class Mao(Baralho):
   def __init__(self, nome=""):
     self.cartas = []
     self.nome = nome

Em praticamente todos os jogos de cartas, é necessario adicionar e remover cartas do baralho. Remover cartas já está resolvido, uma vez que ``Mao`` herda ``removerCarta`` de ``Baralho``. Mas precisamos escrever ``adicionarCarta``::

 class Mao(Baralho):
   #...
   def adicionarCarta(self,carta):
     self.cartas.append(carta)

De novo, a elipse indica que omitimos outros métodos. O método de listas ``append`` adiciona a nova carta no final da lista de cartas. 

---------------------
16.3 Dando as cartas
---------------------

Agora que temos uma classe ``Mao``, queremos distribuir cartas de ``Baralho`` para mãos de cartas. Não é imediatamente óbvio se esse método deve ir na classe ``Mao`` ou na classe ``Baralho``, mas como ele opera num único baralho e (possivelmente) em várias mãos de cartas, é mais natural colocá-lo em ``Baralho``.

O método ``distribuir`` deve ser bem geral, já que diferentes jogos terão diferentes requerimentos. Podemos querer distribuir o baralho inteiro de uma vez só ou adicionar uma carta a cada mão. 

``distribuir`` recebe dois argumentos, uma lista (ou tupla) de mãos e o numero total de cartas a serem dadas. Se não houver cartas suficientes no baralho, o método dá todas as cartas e pára::

 class Baralho:
   #...
   def distribuir(self, maos, nCartas=999):
     nMaos = len(maos)
     for i in range(nCartas):
       if self.estahVazia(): break    # interromper se acabaram as cartas
       carta = self.pegarCarta()      # pegar a carta do topo
       mao = maos[i % nMaos]       # quem deve receber agora?
       mao.adicionarCarta(carta)   # adicionar a carta à mao

O segundo parâmetro, ``nCartas``, é opcional; o default é um número grande, o que na prática significa que todas as cartas do baralho serão dadas se este parâmetro for omitido.

A variável do laço ``i`` vai de 0 a ``nCartas-1``. A cada volta do laço, uma carta é removida do baralho, usando o método de lista ``pop``, que remove e retorna o último item na lista.

O operador módulo (%) permite dar cartas em ao redor da mesa (uma carta de cada vez para cada mão). Quando ``i`` é igual ao numero de mãos na lista, a expressão ``i % nMaos`` volta para o começo da lista (índice 0).

-----------------------
16.4 Exibindo a mao
-----------------------

Para exibir o conteúdo de uma mão, podemos tirar vantagem dos métodos ``exibirBaralho`` e ``__str__`` herdados de ``Baralho``. Por exemplo::

 >>> baralho = Baralho()
 >>> baralho.embaralhar()
 >>> mao = Mao("fabio")
 >>> baralho.distribuir([mao], 5)
 >>> print mao
 Mão fabio contém
 2 de espadas
  3 de espadas
   4 de espadas
    Ás de copas
     9 de paus

Nao é lá uma grande mão, mas tem potencial para um *straight flush*.

Embora seja conveniente herdar os métodos existentes, há outras informacoes num objeto ``Mao`` que podemos querer incluir quando ao exibí-lo. Para fazer isso, podemos fornecer um método ``__str__`` para a classe ``Mao`` que sobrescreva o da classe ``Baralho``::

 class Mao(Baralho)
   #...
   def __str__(self):
     s = "Mao " + self.nome
     if self.estahVazia():
       return s + " está vazia\n"
     else:
       return s + " contém\n" + Baralho.__str__(self)

Inicialmente, ``s`` é uma string que identifica a mão. Se a mão estiver vazia, o programa acrescenta as palavras ``está vazia`` e retorna o resultado.

Se não, o programa acrescenta a palavra ``contém`` e a representação de string do ``Baralho``, computada pela invocação do método ``__str__`` na classe ``Baralho`` em ``self``.

Pode parecer estranho enviar ``self``, que se refere à ``Mao`` corrente, para um método ``Baralho``, mas isso só até voce se lembrar que um ``Mao`` é um tipo de ``Baralho``. Objetos ``Mao`` podem fazer tudo que os objetos ``Baralho`` fazem, entao, é permitido passar uma instância de ``Mao`` para um método ``Baralho``.

Em geral, sempre é permitido usar uma instância de uma subclasse no lugar de uma instância de uma classe mãe.

------------------------------
16.5 A classe ``JogoDeCartas``
------------------------------

A classe ``JogoDeCartas`` toma conta de algumas tarefas básicas comuns a todos os jogos, como, criar o baralho e embaralhá-lo::

 class JogoDeCartas:
   def __init__(self):
     self.baralho = Baralho()
     self.baralho.embaralhar()

Este é o primeiro dos casos que vimos até agora em que o método de inicialização realiza uma computação significativa, para além de inicializar atributos.

Para implementar jogos específicos, podemos herdar de ``JogoDeCartas`` e adicionar caracteristicas para o novo jogo. Como exemplo, vamos escrever uma simulação de Mico.

O objetivo do jogo é livrar-se das cartas que estiverem na mão. Para fazer isso, é preciso combinar cartas formando pares ou casais que tenham a mesma cor e o mesmo número ou figura. Por exemplo, o 4 de paus casa com o 4 de espadas porque os dois naipes são pretos. O Valete de copas combina com o Valete de ouros porque ambos são vermelhos. 

Antes de mais nada, a Dama de paus é removida do baralho, para que a Dama de espadas fique sem par. A Dama de espadas então faz o papel do mico. As 51 cartas que sobram são distribuidas aos jogadores em ao redor da mesa (uma carta de cada vez para cada mão). Depois que as cartas foram dadas, os jogadores devem fazer todos os casais possíveis que tiverem na mão, e em seguida descartá-los na mesa.

Quando ninguém mais tiver nenhum par para descartar, o jogo começa. Na sua vez de jogar, o jogador pega uma carta (sem olhar) do vizinho mais proximo à esquerda, que ainda tiver cartas. Se a carta escolhida casar com uma carta que ele tem na mão, ele descarta esse par. Quando todos os casais possíveis tiverem sido feitos, o jogador que tiver sobrado com a Dama de espadas na mão perde o jogo.

Em nossa simulação computacional do jogo, o computador joga todas as mãos. Infelizmente, algumas nuances do jogo presencial se perdem. Num jogo presencial, o jogador que está com o mico na mão pode usar uns truques para induzir o vizinho a pegar a carta, por exemplo, segurando-a mais alto que as outras, ou mais baixo, ou se esforçando para que ela não fique em destaque. Já o computador simplesmente pega a carta do vizinho aleatoriamente...

---------------------------
16.6 Classe ``MaoDeMico``
---------------------------

Uma mão para jogar Mico requer algumas habilidades para alem das habilidades gerais de uma ``Mao``. Vamos definir uma nova classe, ``MaoDeMico``, que herda de ``Mao`` e provê um método adicional chamado ``descartarCasais``::

 class MaoDeMico(Mao):
   def descartarCasais(self):
     conta = 0
     cartasIniciais = self.cartas[:]
     for carta in cartasIniciais:
       casal = Carta(3 - carta.naipe, carta.valor)
       if casal in self.cartas:
         self.cartas.remove(carta)
         self.cartas.remove(casal)
         print "Mao %s: %s casais %s" % (self.nome,carta,casal)
         conta = conta + 1
     return conta

Começamos fazendo uma cópia da lista de cartas, para poder percorrer a cópia enquanto removemos cartas do original. Uma vez que ``self.cartas`` é modificada no laço, não queremos usá-la para controlar o percurso. Python pode ficar bem confuso se estiver percorrendo uma lista que está mudando!

Para cada carta na mão, verificamos qual é a carta que faz par com ela e vamos procurá-la. O par da carta tem o mesmo ``valor`` (número ou figura) e ``naipe`` da mesma cor. A expressão ``3 - carta.naipe`` transforma um paus (naipe 0) numa espadas (naipe 3) e um ouros (naipe 1) numa copas (naipe 2). Você deve analisar a fórmula até se convencer de que as operações opostas também funcionam. Se o par da carta tambem estiver na mão, ambas as cartas são removidas.

O exemplo a seguir demonstra como usar ``descartarCasais``::

 >>> jogo = JogoDeCartas()
 >>> mao = MaoDeMico("fabio")
 >>> jogo.baralho.distribuir([mao], 13)
 >>> print mao
 mão fabio contém
 Ás de espadas
  2 de ouros
   7 de espadas
    8 de paus
     6 de copas
      8 de espadas
       7 de paus
        Rainha de paus
         7 de ouros
          5 de paus
           Valete de ouros
            10 de ouros
             10 de copas

 >>> mao.descartarCasais()
 Mão fabio: 7 de espadas faz par com 7 de paus
 Mão fabio: 8 de espadas faz par com 8 de paus
 Mão fabio: 10 de ouros faz par com 10 de copas
 >>> print mao
 Mão fabio contém
 Ás de espadas
  2 de ouros
   6 de copas
    Rainha de paus
     7 de ouros
      5 de paus
       Valete de ouros

Observe que não existe um método ``__init__`` para a classe ``MaoDeMico``. Ele é herdado de ``Mao``.

---------------------
16.7 Classe ``Mico``
---------------------

Agora podemos focar nossa atenção no jogo em si. ``Mico`` é uma subclasse de ``JogoDeCartas`` com um novo método chamado ``jogar`` que recebe uma lista de jogadores como argumento.

Já que ``__init__`` é herdado de ``JogoDeCartas``, um novo objeto ``Mico`` contém um novo baralho embaralhado::

 class Mico(JogoDeCartas):
   def jogar(self, nomes):
     # remover a Dama de paus
     self.baralho.removerCarta(Carta(0,12))

     # fazer uma mão para cada jogador
     self.maos = []
     for nome in nomes :
       self.maos.append(MaoDeMico(nome))

     # distribuir as cartas
     self.baralho.distribuir(self.maos)
     print "---------- As cartas foram dadas"
     self.exibirMaos()

     # remover casais iniciais
     casais = self.removerTodosOsCasais()
     print "---------- Os pares foram descartados, o jogo começa"
     self.exibirMaos()

     # jogar até que 25 casais se formem
     vez = 0
     numMaos = len(self.maos)
     while casais < 25:
       casais = casais + self.jogarVez(vez)
       vez = (vez + 1) % numMaos

     print "---------- Fim do jogo"
     self.exibirMaos()

Algumas etapas do jogo foram separadas em métodos. ``removerTodosOsCasais`` percorre a lista de mãos e invoca ``descartarCasais`` em cada uma::

 class Mico(JogoDeCartas):
   #...
   def removerTodosOsCasais(self):
     conta = 0
     for mao in self.maos:
       conta = conta + mao.descartarCasais()
     return conta

    Como exercício, escreva ``exibirMaos`` que percorre ``self.maos`` e exibe cada mão. 

``conta`` é uma acumulador que soma o número de pares em cada mão e retorna o total.

Quando o número total de pares alcança 25, 50 cartas foram removidas das mãos, o que significa que sobrou só uma carta e o jogo chegou ao fim.

A variável ``vez`` mantém controle sobre de quem é a vez de jogar. Começa em 0 e incrementa de um em um; quando atinge ``numMaos``, o operador módulo faz ela retornar para 0.

O método ``jogarVez`` recebe um argumento que indica de quem é a vez de jogar. O valor de retorno é o número de pares feitos durante essa rodada::

 class Mico(JogoDeCartas):
   #...
   def jogarVez(self, i):
     if self.maos[i].estahVazia():
       return 0
     vizinho = self.buscarVizinho(i)
     novaCarta = self.maos[vizinho].pegarCarta()
     self.maos[i].adicionarCarta(novaCarta)
     print "Mao", self.maos[i].nome, "pegou", novaCarta
     conta = self.maos[i].descartarCasais()
     self.maos[i].embaralhar()
     return conta

Se a mão de um jogador estiver vazia, ele está fora do jogo, então, ele não faz nada e retorna 0.

Do contrário, uma jogada consiste em achar o primeiro jogador à esquerda que tenha cartas, pegar uma carta dele, e tentar fazer pares. Antes de retornar, as cartas na mão são embaralhadas, para que a escolha do próximo jogador seja aleatória.

O método ``buscarVizinho`` começa com o jogador imediatamente à esquerda e continua ao redor da mesa até encontrar um jogador que ainda tenha cartas::

 class Mico(JogoDeCartas):
   #...
   def buscarVizinho(self, i):
     numMaos = len(self.maos)
     for next in range(1,numMaos):
       vizinho = (i + next) % numMaos
       if not self.maos[vizinho].estahVazia():
         return vizinho

Se ``buscarVizinho`` alguma vez circulasse pela mesa sem encontrar cartas, retornaria ``None`` e causaria um erro em outra parte do programa. Felizmente, podemos provar que isso nunca vai acontecer (desde que o fim do jogo seja detectado corretamente).

Não mencionamos o método ``exibirBaralhos``. Esse você mesmo pode escrever.

A saída a seguir é produto de uma forma reduzida do jogo, onde apenas as 15 cartas mais altas do baralho (do 10 para cima) foram dadas, para três jogadores. Com esse baralho reduzido, a jogada pára depois que 7 combinações foram feitas, ao invés de 25:: 


 >>> import cartas
 >>> jogo = cartas.Mico()
 >>> jogo.jogar(["Alice","Jair","Clara"])
 ---------- As cartas foram dadas
 Mão Alice contém
 Rei de copas
  Valete de paus
   Rainha de espadas
    Rei de espadas
     10 de ouros

 Mão Jair contém
 Rainha de copas
  Valete de espadas
   Valete de copas
    Rei de ouros
     Rainha de ouros

 Mão Clara contém
 Valete of ouros
  Rei de paus
   10 de espadas
    10 de copas
     10 de paus

 Mão Jair: Dama de copas faz par com Dama de ouros 
 Mão Clara: 10 de espadas faz par com 10 de paus
 ---------- Os pares foram descartados, o jogo começa
 Mão Alice contém
 Rei de copas
  Valete de paus
   Rainha de espadas
    Rei de espadas
     10 de ouros

 Mão Jair contém
 Valete de espadas
  Valete de copas
   Rei de ouros

 Mão Clara contém
 Valete de ouros
  Rei de paus
   10 de copas

 Mão Alice pegou o Rei de ouros 
 Mão Alice: Rei de copas faz par com Rei de ouros 
 Mão Jair pegou 10 de copas 
 Mão Clara pegou Valete de paus  
 Mão Alice pegou Valete de copas
 Mão Jair pegou Valete de ouros 
 Mão Clara pegou Dama de espadas 
 Mão Alice pegou Valete de ouros 
 Mão Alice: Valete de copas faz par com Valete de ouros 
 Mão Jair pegou Rei de paus 
 Mão Clara pegou Rei de espadas 
 Mão Alice pegou 10 de copas 
 Mão Alice: 10 de ouros faz par com 10 de copas 
 Mão Jair pegou Dama de espadas 
 Mão Clara pegou Valete de espadas 
 Mão Clara: Valete de paus faz par com Valete de espadas
 Mão Jair pegou Rei de espadas
 Mão Jeff: Rei de paus faz par com Rei de espadas
 ---------- Fim do jogo
 Mão Alice está vazia

 Mão Jair contém
 Rainha de espadas

 Mão Clara está vazia

Então, o Jair perdeu.

---------------
16.8 Glossário
---------------

herança (*inheritance*)
    Habilidade de definir uma nova classe que é a versão modificada de uma classe definida anteriormente.

classe mãe (*parent class*)
    A classe de quem a classe filha herda.

classe filho (*child class*)
    Um nova classe criada herdando de uma classe existente; também chamada de "subclasse".

