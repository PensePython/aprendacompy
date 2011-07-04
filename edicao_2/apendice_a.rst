.. $Id: apendice_a.rst,v 2.1 2007-04-23 21:17:29 luciano Exp $

=====================
Apêndice A: Depuração
=====================

.. contents:: Tópicos

Diferentes tipos de erros podem acontecer em um programa, e é útil distinguir entre eles para os localizar mais rapidamente:

- Erros de sintaxe são produzidos por Python quando o interpretador está traduzindo o código fonte em *bytecode*. Estes erros geralmente indicam que existe algo errado com a sintaxe do programa. Exemplo: Omitir o sinal de dois pontos (``:``) no final de uma declaração ``def`` produz a mensagem um tanto redundante ``SintaxError: invalid sintax`` (Erro de sintaxe: sintaxe inválida). 

- Erros de tempo de execução são produzidos se algo de errado acontece enquanto o programa está em execução. A maioria das mensagens de tempo de execução incluem informação sobre onde o erro ocorreu e que função estava em execução. Exemplo: Uma recursão infinita eventualmente causa um erro em tempo de execução identificado como ``maximum recursion depth exceeded`` (Excedida a máxima profundidade de recursão).

- Erros de semântica, chamado por alguns autores de erros de lógica, são problemas com um programa que compila e executa mas não tem o resultado esperado. Exemplo: Uma expressão pode não ser avaliada da forma que você espera, produzindo um resultado inesperado.

O primeiro passo na depuração é descobrir com que tipo de erro você está lidando. Embora as seções a seguir estejam organizadas por tipo de erro, algumas técnicas são aplicáveis em mais de uma situação.


-------------------------------
A.1 Erros de sintaxe
-------------------------------

Erros de sintaxe são geralmente fáceis de corrigir, bastando apenas que você descubra onde eles estão. Infelizmente, as mensagens de erro geralmente ajudam pouco. As mensagens mais comuns são: ``SyntaxError: invalid syntax`` (Erro de sintaxe: sintaxe inválida) e ``SyntaxError: invalid token`` (Erro de sintaxe: objeto inválido), nenhuma das duas é muito informativa.

Por outro lado, a mensagem diz a você onde, no código do programa, ocorreu o problema. Na verdade, ela diz a você onde o Python encontrou o problema, que não é necessariamente onde o erro está. Às vezes o erro é anterior à localização da mensagem de erro, geralmente na linha precedente. 

Se você está construindo o programa incrementalmente, você terá uma boa ideia sobre onde estará o erro. Estará na última linha adicionada.

Se você está copiando código de um livro, comece comparando seu código ao código do livro de forma muito cuidadosa. Verifique cada caracter. Ao mesmo tempo, lembre-se que o livro pode estar errado, então você pode perfeitamente encontrar um erro de sintaxe em um livro. 

Aqui estão algumas maneiras de evitar os erros de sintaxe mais comuns:

1. Certifique-se que você não está utilizando uma palavra reservada de Python para um nome de variável. 

2. Verifique a existência do sinal de dois pontos no final do cabeçalho de cada declaração composta, incluindo as declarações ``for``, ``while``, ``if``, e ``def``. 

3. Verifique se a endentação está consistente. Você pode endentar com espaços ou com tabulações, mas é melhor não misturá-los. Cada nível deve ser aninhado com a mesma quantidade.

4. Assegure-se de que cada *string* no código tenha as aspas correspondentes.

5. Se você tem *strings* de multilinhas criadas usando três aspas (simples ou duplas), assegure-se de que você terminou a *string* apropriadamente. Uma *string* terminada de forma inapropriada ou não terminada pode gerar um erro de ``invalid token`` (objeto inválido) no final do seu programa, ou ele pode tratar a parte seguinte do programa como uma *string* até chegar à próxima *string*. No segundo caso, pode ser que o interpretador nem mesmo produza uma mensagem de erro!

6. Um conjunto de parênteses, colchetes ou chaves não fechados corretamente faz com que o Python continue com a próxima linha como parte da declaração anterior. Geralmente, um erro ocorre quase imediatamente na linha seguinte.

7. Verique o clássico ``=`` ao invés de ``==`` dentro de uma condicional.

Se nada funcionar, vá para a próxima seção.


A.1.1 Eu não consigo fazer meu programa executar não importa o que eu faça
---------------------------------------------------------------------------

Se o compilador diz que existe um erro e você não o vê, isto pode ser por que você e o compilador não estão olhando para o mesmo código. Verifique seu ambiente para se assegurar que o programa que você está editando é o mesmo que o Python está tentando executar. Se você não está certo, tente colocar um erro de sintaxe óbvio e deliberado no início do programa. Agora execute (ou importe) o programa novamente. Se o compilador não encontrar o novo erro, provavelmente existe algo de errado com a maneira como o ambiente está configurado.

Se isto acontecer, uma abordagem é iniciar novamente com um novo programa como "Hello World!",  e se assegurar de que você consegue colocar um programa conhecido para executar. Então gradualmente adicione as partes do novo programa ao programa que está funcionando.


-------------------------------
A.2 Erros de tempo de execução
-------------------------------


Uma vez que seu programa está sintaticamente correto, o interpretador do Python pode importá-lo e começar a executá-lo. O que poderia dar errado?


A.2.1 Meu programa não faz absolutamente nada
----------------------------------------------

Este é o problema mais comum quando um arquivo consiste de funções e classes mas não chama nada realmente para iniciar a execução. Isto pode ser intencional se você planeja apenas importar este módulo para fornecer classes e funções.

Se isto não é intencional, assegure-se de que você está chamando uma função para iniciar a execução ou execute uma "manualmente" do *prompt* interativo. Veja também a seção "Fluxo de Execução" abaixo.


A.2.2 Meu programa trava
-----------------------------

Se um programa para e parece não estar fazendo nada, dizemos que ele "travou". Geralmente isto significa que ele foi pego num laço infinito ou numa recursão infinita. 

- Se existe um laço em particular aonde você suspeita estar o problema, adicione uma declaração ``print`` imediatamente antes do laço que diga "entrando no laço" e uma outra imediatamente depois que diga "saindo do laço". Execute o programa. Se você receber a primeira mensagem e não a segunda, você tem um laço infinito. Vá para a seção "Laço Infinito" abaixo. 

- Na maioria das vezes, uma recursão infinita fará com que o programa execute por um tempo e então ele produzirá um erro do tipo ``Runtime Error: Maximum recursion depth exceeded`` (Erro de tempo de execução: Excedida a profundidade máxima de recursão). Se isto acontecer, vá para a seção "Recursão Infinita" abaixo. Se você não está recebendo este erro, mas suspeita que há um problema com um método ou função recursiva, você ainda pode utilizar as técnicas da seção "Recursão Infinita".

- Se nenhum destes passos funcionar, comecea testar outros laços ou métodos ou funções recursivas.

- Se isso não funcionar, então é possível que você não entenda o fluxo de execução do seu programa. Vá para a seção "Fluxo de Execução" abaixo.


Laço Infinito
==============

Se você acha que tem um laço infinito e desconfia de qual seja laço causador do problema, adicione uma declaração ``print`` no final do laço que imprima os valores das variáveis na condição e o valor da condição.

Por exemplo:

>>> while x > 0 and y < 0:
    # faz algo para x
    # faz algo para y
    print "x: ", x
    print "y: ", y
    print "condição: ", (x > 0 and y < 0)

Agora, quando você executar o programa, serão exibidas três linhas de saída para cada execução do laço. Na última execução do laço, a condição deveria ser ``False`` (falso). Se o laço continuar, você terá condições de ver os valores de ``x`` e ``y``, podendo, assim, descobrir o porquê das variáveis não serem atualizadas corretamente.


Recursão Infinita
=================

Na maioria das vezes, uma recursão infinita fará com que um programa execute por um determinado tempo e então produza um erro de ``Maximum recursion depth exceeded`` (Excedida a profundidade máxima de recursão). 

Se você suspeita que uma função ou método está causando uma recursão infinita, comece verificando para se assegurar que exista um caso básico. Em outras palavras, deve existir alguma condição que faça com que a função ou método finalize sem fazer uma chamada recursiva. Se não existe tal condição, você precisa repensar o algoritmo e identificar um caso base.

Se existe um caso base mas o programa parece não estar alcançando-o, adicione uma declaração ``print`` no início  da função ou método que imprime o(s) parâmetro(s). Agora, quando você executar o programa, você verá umas poucas linhas de saída todas as vezes que a função ou método for executado, e você verá o(s) parâmetro(s). Se o(s) parâmetro(s) não está(ão) se movendo em direção ao caso base, você terá ideias de por que não, e poderá então corrigir o problema. 

Fluxo de Execução
=================

Se você não está certo de como o seu programa está fluindo, adicione declarações ``print`` ao início de cada função com uma mensagem semelhante a "entrando na função ``foo``", onde ``foo`` é o nome da função. 

Agora quando você executar o programa, será exibido um rastro de cada função à medida em que ela é invocada.

A.2.3 Quando eu executo o programa, recebo uma exceção
------------------------------------------------------

Se algo vai errado durante a execução, o Python exibe uma mensagem que inclui o nome da exceção, a linha do código do programa onde o problema ocorre, e dados para investigação do erro, onde é descrita a pilha de execução de funções e métodos.

Tais dados identificam a função que está sendo executada no momento, e então a função que a invocou, e então a função que invocou *aquela*, e assim por diante (a pilha de execução de funções). Em outras palavras, ele traça o caminho das invocações da função que te levou até onde você está. Ele também inclui o número da linha no respectivo arquivo onde cada uma dessas chamadas ocorre.

O primeiro passo é examinar o lugar no programa onde ocorreu o erro e tentar descobrir o que aconteceu. Esses são alguns dos erros de tempo de execução mais comuns:

**NameError (Erro de Nome):** Você está tentando utilizar uma variável que não existe no ambiente atual. Lembre-se que variáveis locais são locais. Você não pode referenciá-la fora da função onde ela foi definida.

**TypeError (Erro de Tipo):** Existem várias causas possíveis:

 - Você está tentando utilizar um valor de forma imprópria. Exemplo: indexando uma *string*, lista ou tupla com alguma coisa que não é um inteiro. 
 - Há uma incompatibilidade entre os itens em um formato de *string* e os itens passados para conversão. Isto pode acontecer se o número de itens não for igual ou se uma conversão inválida é chamada. Por exemplo: Passar uma *string* para a formatação de conversão ``%f``.
 - Você está passando o número errado de argumentos para uma função ou método. Para métodos, verifique sua definição e confira se o primeiro parâmetro chama-se ``self``. Então verifique a chamada ao método; certifque-se de que você está chamando o método em um objeto com o tipo correto e fornecendo os argumentos adequados.

**KeyError (Erro de Chave):** Você está tentando acessar um elemento de um dicionário utilizando um valor de chave que o dicionário não contém.

**AttributeError (Erro de Atributo):** Você está tentando acessar um atributo ou método que não existe em um objeto.

**IndexError (Erro de Índice):** O índice que você está usando para acessar uma lista, *string* ou tupla não existe no objeto, ou seja, é maior que seu comprimento menos um. Imediatamente antes do ponto do erro, adicione uma delaração *print* para mostrar o valor do índice e o comprimento do *objeto*. O *objeto* é do tamanho correto? O índice está com o valor adequado?

A.2.4 Eu adicionei tantas declarações *print* que a saída do programa ficou bagunçada
--------------------------------------------------------------------------------------

Um dos problemas com o uso de declarações *print* para a depuração é que a saída pode ficar confusa, dificultando a depuração, ao invés de facilitar. Há duas coisas que podem ser feitas: simplificar a saída ou simplificar o programa.

Para simplificar a saída, você pode remover ou comentar as declarações *print* que não estão ajudando, ou combiná-las, ou, ainda, formatar a saída para facilitar o entendimento.

Para simplificar o programa, existem várias coisas que você pode fazer: Primeiro, reduza o problema no qual o programa está trabalhando. Por exemplo, se você está ordenando um *array*, ordene um * array* **pequeno**. Se o programa recebe entrada do usuário, dê a ele a entrada mais simples capaz de causar o problema.

Segundo, limpe o programa. Remova código inútil e reorganize o programa para torná-lo tão fácil de ler quanto possível. Por exemplo, se você suspeita que o problema está numa parte profundamente aninhada do programa, tente reescrever aquela parte com uma estrutura mais simples. Se você suspeita de uma função longa, tente dividi-la em funções menores e testá-las separadamente.

Muitas vezes o processo de encontrar o caso de teste mínimo leva você ao erro. Se você descobrir que o programa funciona em uma situação, mas não em outra, você já tem uma boa dica a respeito do que está acontecendo.

De forma semelhante, reescrever pedaços de código pode ajuda a encontrar erros sutis. Se você faz uma alteração que você pensa que não afeta o programa, e ela afeta, você também tem uma dica.


-------------------------------
A.3 Erros de semântica
-------------------------------


De certa forma, os erros de semântica são os mais difíceis de depurar, porque o compilador e o sistema de tempo de execução não fornecem informações sobre o que está errado. Somente você sabe o que o programa deve fazer, e somente você sabe que ele não está fazendo isto.

O primeiro passo é fazer uma conexão entre o texto do programa e o comportamento que você está vendo. Você precisa de uma hipótese sobre o que o programa está realmente fazendo. Uma das coisas que dificultam é que os computadores trabalham muito rápido.

Você sempre desejará que a velocidade do programa pudesse ser diminuída para a velocidade humana, e com alguns depuradores você pode. Mas o tempo que leva para inserir umas poucas declarações ``print`` bem colocadas é geralmente mais curto quando comparado a configurar um depurador, inserir e remover *breakpoints*, e "caminhar" pelo programa até onde o erro ocorre.


A.3.1 Meu programa não funciona
--------------------------------

Você deveria se fazer as seguintes perguntas:

 - Há alguma coisa que o programa deveria fazer, mas que não parece que estar acontecendo?
 - Não está acontecendo alguma coisa que não deveria acontecer? Encontre o código no seu programa que executa a função e veja se ele está executando no momento errado ou de forma errada.
 - Uma parte do código está produzindo o efeito esperado? Cetifique-se que você entende o código em questão, especialmente se ele envolve chamadas de funções ou métodos em outros módulos da linguagem. Leia a documentação das funções e módulos que você está utilizando. Teste as funções escrevendo casos simples de teste e verificando os resultados.

Para programar, você precisa ter um modelo mental de como seus programas trabalham. Se você escreve um programa que não faz aquilo que você espera, é muito comum que o problema não esteja no programa, mas sim no seu modelo mental.

A melhor maneira de corrigir seu modelo mental é quebrar o programa em seus componentes (geralmente as funções e métodos) e testar cada componente de forma independente. Uma vez que você tenha encontrado a diferença entre seu modelo e a realidade, você pode resolver o problema.

Obviamente, componentes devem ser desenvolvidos e testado à medida que o seu programa vai ganhando vida. Se você encontra um problema, haverá uma pequena quantidade de novo código com funcionamento incerto.



A.3.2 Eu tenho uma grande expressão cabeluda e ela não faz o que eu espero
---------------------------------------------------------------------------


Escrever expressões complexas é legal se elas forem legíveis, mas pode ser difícil de depurar. Geralmente é uma boa ideia quebrar uma expressão complexa em uma série de atribuições para variáveis temporárias.

Por exemplo:

>>> self.mao[i].adicionaCarta(self.mao[self.encontraVizinho(i)].popCarta())

Isto pode ser escrito como:

>>> vizinho = self.encontraVizinho(i)
>>> cartaPega = self.mao[vizinho].popCarta()
>>> self.mao[i].adicionaCarta(cartaPega)

A versão explícita é mais fácil de ler, pois os nomes das variáveis fornecem documentação adicional, e é mais fácil depurar, já que você pode verificar os tipos das variáveis intermediárias e mostrar seus valores.

Um outro problema que pode ocorrer com expressões longas é que a ordem de avaliação pode não ser o que você espera. Por exemplo, se você está traduzido a expressão `x / 2pi` (XXX fazer a equação matemática) para Python, você poderia escrever:

>>> y = x / 2 * math.pi

Isto está correto por que a multiplicação e a divisão possuem a mesma precedência e são avalidadas da esquerda pra direita. Então a expressão calcula `*x*pi/2` (XXX fazer a equação matemática).

Uma boa maneira de depurar expressões é adicionar parênteses para tornar a ordem de avaliação explícita:

>>> y = x / (2 * math.pi)

Sempre que você não estiver seguro sobe a ordem de avaliação, utilize parênteses. Não apenas o programa estará correto(no sentido de fazer aquilo que você tinha a intenção),  ele também será mais legível por outras pessoas que não tenham memorizado as regras de precedência.


A.3.3 Eu tenho uma função ou método que não retorna o que eu espero
--------------------------------------------------------------------


Se você possui uma declaração *return* com uma expressão complexa, você não tem a chance de exibir o valor de *return* antes que ele seja devolvido. Novamente, você pode utilizar uma variavel temporária. Por exemplo, ao invés de: 

>>> def pega_encontrados(self):
    return self.mao[i].devolveEncontrados()

você poderia escrever:

>>> def pega_encontrados(self):
    qtEncontrados = self.mao[i].devolveEncontrados()
    return qtEncontrados

Agora você tem a oportunidade de mostrar o valor de *qtEncontrados* antes de devolvê-lo.


A.3.4 Eu estou empacado mesmo e eu preciso de ajuda
----------------------------------------------------

Primeiro,tente sair da frente do computador por alguns minutos. Computadores emitem ondas que afetam o cérebro, causando estes efeitos:

 - Frustação e/ou raiva.
 - Crenças superticiosas ("o computador me odeia") e pensamentos mágicos ("o prorama só funciona quando eu coloco meu chapéu de trás pra frente").
 - Programação pelo caminhar aleatório (a tentativa de programar escrevendo cada programa possível e escolhendo aquele que faz a coisa certa).

Se você estiver sofrendo de qualquer um destes sintomas, levante-se e vá dar uma caminhada. Quando você estiver calmo, pense no programa. O que ele está fazendo? Quais são as possíveis causas do comportamento inadequado? Quando foi a última vez que você teve um programa funcionando, e o que você fez depois disto?

Às vezes é uma questão de tempo para encontrar um erro. Nós geralmente encontramos os erros quando estamos longe do computador e deixamos nossa mente vaguear. Alguns dos melhores lugares para encontrar erros são trens, chuveiros e na cama, logo antes de pegar no sono. 


A.3.5 Não, eu preciso mesmo de ajuda
-------------------------------------

Isto acontece. Mesmo os melhores programadores empacam de vez em quando. Às vezes você trabalha num programa por tanto tempo que não consegue ver o erro. Um par fresco de olhos é o que se precisa.

Antes de trazer mais alguém, certifique-se de que você tenha esgotado as técnicas descritas aqui. Seu programa deve ser tão simples quanto possível, e você deve estar trabalhando com a mais simples das entradas que causam o erro. Você deve ter declarações *print*  nos lugares apropriados (sem comprometer a compreensividade da saída do programa). Você tem que entender o problema o suficiente para descrevê-lo concisamente.

Quando você trouxer alguém pra ajudar, assegure-se de dar a este alguém a informação que ele precisa:

 - Se existe uma mensagem de erro, o que é ela e que parte do programa ela indica?
 - Qual foi a última coisa que você fez antes deste erro acontecer? Quais foram as últimas linhas de código que você escreveu, ou qual é o novo caso de teste que falha?
 - O que você já tentou até o momento, e o que você aprendeu?

Quando você encontrar um erro, gaste um segundo para pensar sobre o que você poderia fazer para encontrá-lo mais rápido. Da próxima vez que você ver algo similar, você terá condições de encontrar o erro mais rapidamente.

Lembre-se, o objetivo não é apenas fazer o programa funcionar. O objetivo é aprender como fazer o programa funcionar.
