.. $Id: capitulo_14.rst,v 2.1 2007-04-23 21:17:39 luciano Exp $

==============================
Capítulo 14: Classes e métodos
==============================

.. contents:: Tópicos

**ATENÇÃO** As referências cruzadas a nomes em códigos de outros capítulos (especialmente 13) ainda não foram unificadas...

14.1 Características da orientação a objetos
-----------------------------------------------

Python é uma **linguagem de programação orientada a objetos**, o que significa que ela tem características que suportam a **programação orientada a objetos**.

Não é fácil definir programação orientada a objetos, mas temos visto already algumas de suas características:

- Programas são construídos sobre definições de objetos e definições de funções, e a maioria das computações é expressa em termos de operações sobre objetos.

- Cada definição de objeto corresponde a algum objeto ou conceito do mundo real, e as funções que operam com aqueles objetos correspondem à maneira como os objetos do mundo real interagem.

Por exemplo, a classe ``Tempo``, definida no capítulo 13 corresponde à maneira como as pessoas registram as horas do dia, e as funções que definimos correspondem aos tipos de coisas que as pessoas fazem com times. Do mesmo modo, as classes ``Ponto`` e ``Retângulo`` correspondem aos conceitos matemáticos de um ponto e de um retângulo.

Até aqui, não tiramos vantagem das características fornecidas por Python que suportam a programação orientada a objetos. Estritamente falando, estas características não são necessárias. Na maior parte das vezes, elas fornecem uma sintaxe alternativa para as coisas que já fizemos, mas em muitos casos, a alternativa é mais concisa e convém mais acuradamente à estrutura do programa.

Por exemplo, no programa ``Time``, não existe uma conexão óbvia entre a definição da classe e a definição da função que segue. Com alguma investigação, fica aparente que toda função toma pelo menos um objeto ``Time`` como um parâmetro.

Esta observação é a motivação por trás dos **métodos**. Já temos visto alguns métodos, tais como ``keys`` (``chaves``) e ``values`` (``valores``), os quais foram invocados em dicionários. Cada método é associado com uma classe e é intended para ser invocado em instâncias daquela classe.

Métodos são simplesmente como funções, com duas diferenças:

- Métodos são definidos dentro da definição de uma classe para tornar explícita a relação entre a classe e o método.

- A sintaxe para a chamada do método é diferente da sintaxe para a chamada de uma função.

Nas próximas seções, vamos pegar as funções dos dois capítulos anteriores e transformá-las em métodos. Esta transformação é puramente mecânica: você pode conseguí-la simplesmente seguindo uma seqüência de passos. Se você se sentir confortável convertendo de uma forma para a outra, você estará apto para escolher a melhor forma para seja o lá o que for que você estiver fazendo.

14.2 exibeHora (printTime)
-----------------------------

No capítulo 13, definimos uma classe chamada ``Horário`` (``Time``) e você escreveu uma função chamada ``exibeHora`` (``printTime``), que deve ter ficado mais ou menos assim::

  class Horario:
    pass

  def exibeHora(time)
    print str(time.horas) + ?:? + \
      str(time.minutos) + ?:? + \
      str(time.segundos)

Para chamar esta função, passamos um objeto ``Time`` como um parâmetro:

>>> horaCorrente = Hora()
>>> horaCorrente.horas = 9
>>> horaCorrente.minutos = 14
>>> horaCorrente.segundos = 30
>>> exibeHora(horaCorrente)

Para fazer de ``exibeHora`` um método, tudo o que temos a fazer é mover a definição da função para dentro da definição da classe. Note a mudança na endentação::

  class Horario:
    def exibeHora(time):
      print str(time.horas) + ?:? + \
        str(time.minutos) + ?:? + \
        str(time.segundos)

Agora podemos chamar ``exibeHora`` usando a natação de ponto::

  >>> horaCorrente.exibeHora()

Como é usual, o objeto no qual o método é invocado aparece antes do ponto e o nome do método aparece depois do ponto.

O objeto no qual o método é invocado é atribuído ao primeiro parâmetro, então, neste caso, ``horaCorrente`` é atribuído ao parâmetro ``time``.

Por convenção, o primeiro parâmetro de um método é chamado ``self``. A razão para isto é um pouco convoluted, mas é baseada numa metáfora útil.

A sintaxe para uma chamada de função, ``exibeHora(horaCorrente)``, sugere que a função é um agente ativo. Diz algo como, ?Ei, ``exibeHora``! Aqui está um objeto para você exibir.?

Na programação orientada a objetos, os objetos são agentes ativos. Uma chamado do tipo ``horaCorrente.exibeHora()`` diz ?Ei, ``horaCorrente``! Por favor exiba-se a si mesmo!?

Esta mudança de perspectiva pode ser mais polida, mas não fica óbvio que seja útil. Nos exemplos que temos visto até aqui, pode ser que não seja. Mas às vezes, deslocar a responsabilidade das funções para cima dos objetos torna possível escrever funções mais versáteis, e torna mais fácil manter e reutilizar o código.

14.3 Um outro exemplo
-----------------------

Vamos converter ``incremento`` (da Seção 13.3) em um método. Para poupar espaço, deixaremos de fora métodos definidos previamente(anteriormente?), mas você deve mantê-los em sua versão::

  class Time:
    #previous method definitions here...

    def increment(self, segundos):
    self.seconds = seconds + self.seconds

    while self.segundos >= 60:
      self.seconds = self.segundos - 60
      self.minutes = self.minutos + 1

    while self.minutes >= 60:
      self.minutes = self.minutos - 60
      self.hours = self.horas + 1

A transformação é puramente mecânica ? movemos a definição do método para dentro da definição da classe e mudamos o nome do primeiro parâmetro.

Agora podemos chamar ``incremento`` como um método::

  horaCorrente.incremento(500)

De novo, o objeto no qual o método é chamado gets atribui ao primeiro parâmetro, ``self``. O segundo parâmetro, ``segundo`` toma(gets) o valor ``500``.

  *Como um exercício, converta ?converteParaSegundos? (da Seção 13.5) para um método na classe ?Time?.*

14.4 Um exemplo mais complicado
---------------------------------

...

14.10 Glossário
----------------

linguagem orientada a objetos
    Uma linguagem que provê características tais como classes definidas pelo usuário e herança, que facilitam a programação orientada a objetos.

programação orientada a objetos
    Um estilo de programação na qual os dados e as operações que os manipulam estão organizados em classes e métodos.

método
    Uma função que é definida dentro de uma definição de classe e é chamada em instâncias desta classe.

override (sem traducao; termo consagrado)
    Substituir uma definição já pronta. Exemplos incluem substituir um parâmetro padrão por um argumento particular e substituir um método padrão, fornecendo um novo método com o mesmo nome.

método de inicialização (tambem chamado de construtor)
    Um método especial que é invocado automaticamente quando um novo objeto é criado e que inicializa os atributos deste objeto.

sobrecarga de operador
    Estender a funcionalidade dos operadores nativos (\+, \-, \*, \>, \<, etc.) de forma que eles funcionem também com tipos definidos pelo usuário.

produto escalar
    Operação definida na álgebra linear que multiplica dois pontos (com coordenadas (x,y,z)) e retorna um valor            numérico.

multiplicação por escalar
    Operação definida na álgebra linear que multiplica cada uma das coordenadas de um ponto por um valor numérico.

polimórfica
    Uma função que pode operar com mais de um tipo. Se todas as operações de uma função pode ser aplicadas a um certo tipo, então a função pode ser aplicada a este tipo.
    
    
