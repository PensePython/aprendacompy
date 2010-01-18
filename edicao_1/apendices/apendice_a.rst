.. $Id: apendice_a.rst,v 2.1 2007-04-23 21:17:29 luciano Exp $

=====================
Apêndice A: Depuração
=====================

Diferentes tipos de erros podem acontecer em um programa, e é útil distinguir entre eles para os localizar mais rapidamente:

- Erros de sintaxe são produzidos por Python quando ela está traduzindo o código fonte em *bytecode*. Eles geralmente indicam que existe algo errado com a sintaxe do programa. Exemplo: Omitir o sinal de dois pontos (``:``) no final de uma declaração ``def`` produz a mensagem um tanto redundante ``SintaxError: invalid sintax`` (Erro de sintaxe: sintaxe inválida). 

- Erros de tempo de execução são produzidos pelo sistema de tempo de execução se algo de errado  acontece enquanto o programa está em execução. A maioria das mensagens de tempo de execução incluem informação sobre onde o erro ocorreu e que função estava em execução. Exemplo: Uma recursão infinita eventualmente causa um erro de tempo de execução de "maximum recursion depth exceeded" (Excedida a máxima profundidade de recursão).

- Erros de semântica são problemas com um programa que compila e executa mas não faz a coisa certa . Exemplo: Uma expressão pode não ser avaliada da forma que você espera, produzindo um resultado inesperado.

O primeiro passo na depuração é descobrir com que tipo de erro você está lidando. Embora as sessões a seguir estejam organizadas por tipo de erro, algumas técnicas são aplicáveis em mais de uma situação.


-------------------------------
A.1 Erros de sintaxe
-------------------------------


Erros de sintaxe são geralmente fáceis de corrigir uma vez que você descubra o que eles são. Infelizmente, as mensagens de erro geralmente ajudam pouco. Os mensagens mais comuns são: ``SyntaxError: invalid syntax`` (Erro de sintaxe: sintaxe inválida) e ``SyntaxError: invalid token`` (Erro de sintaxe: objeto inválido), nenhuma das quais é muito informativa.

Por outro lado, a mensagem diz a você onde no programa o problema ocorreu. Na verdade, ela diz a você onde Python encontrou o problema, que não é necessariamente onde o erro está. Às vezes o erro é anterior a localização da mensagem de erro, geralmente na linha precedente. Se você está construindo o programa incrementalmente, você deveria ter uma boa idéia sobre onde o erro está. Deveria estar na última linha adicionada.

Se você está copiando código de um livro, comece comparando seu código ao código do livro muito cuidadosamente. Verifique cada caracter. Ao mesmo tempo, lembre-se que o livro poderia estar errado, então se você encontrar algo que parece como um erro de sintaxe, ele poderia ser. 


Aqui estão algumas maneiras de evitar os mais comuns erros de sintaxe:

1. Certifique-se que você não está utilizando uma palavra reservada de Python para um nome de variável. 

2. Verifique que exista o sinal de dois pontos no final do cabeçalho de cada declaração composta, incluindo declarações ``for``, ``while``, ``if``, e ``def``. 

3. Verifique se indentação está consistente. Você pode indentar tanto com espaços quanto com tabulações mas é melhor não misturá-los. Cada nível deveria ser aninhado com a mesma quantidade.

4. Assegure-se de que cada *string* no código tenha as aspas correspondentes.

5. Se você tem *strings* de multilinhas com aspas triplas (simples ou duplas), assegure-se de que você terminou a *string* apropriadamente. Uma *string* não terminada pode gerar um erro de ``invalid token`` (objeto inválido) no final do seu programa, ou ele pode tratar a parte seguinte do programa como uma *string* até chegar à próxima *string*. No segundo caso, pode nem mesmo ser produzida uma mensagem de erro!

6. Um conjunto de parênteses, colchetes ou chaves não fechados corretamente faz com que Python continue com  a próxima linha como parte da declaração anterior. Geralmente, um erroocorre quase imediatamente na linha seguinte.

7. Verique o clássico ``=`` ao invés de ``==`` dentro de uma condicional.

Se nada funcionar, vá para a próxima seção.


===========================================================================
A.1.1 Eu não consigo fazer meu programa executar não importa o que eu faça
===========================================================================

Se o compilador diz que existe um erro e você não o vê, isto pode ser porque você e o compilador não estão olhando para o mesmo código. Verifique seu ambiente para se assegurar que o programa que você está editando é o mesmo que Python está tentando executar. Se você não está erto, tente colocar um erro de sintaxe óbvio e deliberado no início do programa. Agora execute (ou importe) o programa novamente. Se o compilador não encontrar o novo erro, provavelmente existe algo de errado com a maneira como o ambiente está configurado.

Se isto acontecer, uma abordagem é iniciar novamnente com um novo programa como "Hello World!",  e se assegurar de que você consegue colocar um programa conhecido para executar. Então gradualmente adicione os pedaços do novo programa aprograma que está funcionando.


-------------------------------
A.2 Erros de tempo de execução
-------------------------------


Uma vez que seu programa está sintaticamente correto,Python pode importá-lo e pelo menos começar a executá-lo. O que poderia dar errado?


===========================================================================
A.2.1 Meu programa não faz absolutamente nada
===========================================================================

Este é o problema mais comum quando um arquivo consiste de funções e classes mas não chama nada realmente para iniciar a execução. Isto pode ser intencional se você planeja apenas importar este módulo para fornecer classes e funções.

Se isto não é intencional, asegure-se de que você está invocando uma função para iniciar a execução ou execute uma do *prompt* interativo. Veja também a seção "Fluxo de Execução" abaixo.


===========================================================================
A.2.2 Meu programa trava
===========================================================================

Se um programa pára e parece não estar fazendo nada, dizemos que ele "travou". Geralmente isto significa que ele foi pego num laço infinito ou numa recursão infinita. 

- Se existe um laço em particular em que você suspeita que o problema esteja, adicione uma declaração ``print`` imediatamente antes do laço que diga "entrando no laço" e uma outra imediatamente depois que diga "saindo do laço". Execute o programa. Se você receber a primeira mensagem e não a segunda, você tem um laço infinito. Vá para a seção "Laço Infinito" abaixo. 

- Na maioria das vezes, uma recursão infinita fará com que o programa execute por um tempo e então ele produzirá um erro do tipo ``Runtime Error: Maximum recursion depth exceeded`` (Erro de tempo de execução: Excedida a máxima profundidade de recursão). Se isto acontecer, vá para a seção "Recursão Infinita" abaixo. Se você não está recebendo este erro mas suspeita que há um problema com um método ou função recursiva, você ainda pode utilizar as técnicas da seção "Recursão Infinita".

- Se nenhum destes passos funcionar, comecea testar outros laços ou  métodos ou funções recursivas.

- Se isso não funcionar, então é possível que você não entenda o fluxo de execução do seu programa. Vá para a seção "Fluxo de Execução" abaixo.


+++++++++++++++++++++++++++++++++++++
Laço Infinito
+++++++++++++++++++++++++++++++++++++

Se você acha que tem um laço infinito e você acha que sabe qual é o laço que está causando o problema, adicione uma declaração ``print`` no final do laço que imprima os valores das variáveis na condição e o valor da condição.

Por exemplo:

>>> while x > 0 and y < 0:
	# faz algo para x
	# faz algo para y
	print "x: ", x
	print "y: ", y
	print "condição: ", (x > 0 and y < 0)

Agora quando você executa o programa, você verá três linhas de saída para cada execução do laço. Na última vez dentro do laço, a condição deveria ser ``false`` (falso). Se o laço continuar, você terá condições de ver os valores de ``x`` e ``y``, e você poderia descobrir porque eles não estão sendo atualizados corretamente.


+++++++++++++++++++++++++++++++++++++
Recursão Infinita
+++++++++++++++++++++++++++++++++++++


Na maioria das vezes, uma recursão infinita fará com que um programa execute por um tempo e então produza um erro de ``Maximum recursion depth exceeded`` (Excedida a máxima profundidade de recursão). 

Se você suspeita que uma função ou método está causando uma recursão infinita, comece verificando para se assegurar que exista um caso básico. Em outras palavras, deveria existir alguma condição que faça com que a função ou método finalize sem fazer uma invocação recursiva. Se não, então você precisa repensar o algoritmo e identificar um caso base.

Se existe um caso base mas o programa parece não estar o alcançando, adicione uma declaração ``print`` no início  da função ou método que imprime o parâmetro. Agora quando você executa o programa, você verá umas poucas linhas de saída todas as vezes que a função ou método for invocada, e você verá os parâmetros. Se os parâmetros não estão se movendo em direção ao caso base, você obterá algumas idéias de por que não. 

+++++++++++++++++++++++++++++++++++++
Fluxo de Execução
+++++++++++++++++++++++++++++++++++++

Se você não está certo de como o fluxo de execução está se movendo através do programa, adicione declarações ``print`` ao início de cada funçãp com uma mensagem como "entrando na função ``foo``" onde ``foo`` é o nome da função. 

Agora quando você executar o programa, ele mostrará um rastro de cada função à medida em que ela é invocada.

===========================================================================
A.2.3 Quando eu executo o programa eu recebo uma exceção
===========================================================================

Se algo vai errado durante a execução, Python exibe uma mensagem que inclui o nome da exceção, a linha do programa onde o problema ocorre, e um caminho de volta **XXX (traceback)**.

O caminho de volta identifica a função que está sendo executada no momento, e então a função que a invocou, e então a função que invocou *aquela*, e assim por diante. Em outras palavras, ele traça o caminho das invocações da função que te levou até onde você está. Ele também inclui o número da linha em seu arquivo onde cada uma dessas chamadas ocorre.

O primeiro passo é examinar o lugar no programa onde o erro ocorreu e ver se você consegue descobrir o que aconteceu. Esses são alguns dos erros de tempo de execução mais comuns:

**NameError (Erro de Nome):** Você está tentando utilizar uma variável que não existe no ambiente atual. Lembre-se que variáveis locais são locais. Você não pode referenciá-la fora da função onde ela foi definida.

**TypeError (Erro de Tipo):** Existem várias causas possíveis:

 - Você está tentando utilizar um valor de forma inapropriada. Exemplo: indexando uma *string*, lista ou tupla com alguma coisa que não um inteiro. 
 - Há uma desacordo entre os itens em um formato de *string* e os itens passados para conversão. Isto pode acontecer se o número de itens não casa ou se uma conversão inválida é chamada.
 - Você está passando o número errado de argumentos para uma função ou método. Para métodos, olha a definição do e verifique se o primeiro parâmetro é ``self``. Entào verifique a invocação do método; certifque-se de que você está invocando o método em um objeto com o tipo correto e fornecendo os argumentos corretamente.

**KeyError (Erro de Chave):** Você está tentando acessar um elemento de um dicionário utilizando um valor de chave que o dicionário não contém.

**AttributeError (Erro de Atributo):** Você está tentando acessar um atributo ou método que não existe.

**IndexError (Erro de Índice):** O índice que você está usando para acessar a lista, *string* ou tupla é maior que seu comprimento menos um. Imediatamente antes do ponto do erro, adicione uma delaração *print* para mostrar o valor do índice e o comprimento do *array*. O *array* é do tamanho correto? O índice está com o valor correto?

=============================================================================
A.2.4 Eu adicionei tantas declarações *print* que fiquei inundado coma saída
=============================================================================

Um dos problemas com o uso de declarações *print* para a depuração é que você pode acabar enterrado na saída. Há duas formas de agir: simplificar a saída ou simplificar o programa.

Para simplificar a saída, você pode remover ou comentar as declarações *print* que não estão ajudando, ou combiná-las, ou formatar a saída para facilitar o entendimento.

Para simplificar o programa, existem várias coisas que você pode fazer. Primeiro, reduza o problema no qual o programa está trabalhando. Por exemplo, se você está ordenando um *array*, ordene um * array* **pequeno**. Se o programa recebe entrada do usuário, dê a ele a entrada mais simples que causa o problema.

Segundo, limpe o programa. Remova código morto e reorganize o programa para torná-lo tão fácil de ler quanto possível. Por exemplo, se você suspeita que o problema está numa parte profundamente aninhada doprograma, tente reescrever aquela parte com uma estrutura mais simples. Se você suspeita de uma função longa, tente dividi-la em funções menores e testá-las separadamente.

Muitas vezes o processo de encontrar o caso de teste mínimo leva você ao erro. Se você descobrir que o programa funciona em uma situação mais não em outra, isto te dá uma boa dica a respeito do que está acontecendo.

De forma semelhante, reescrever pedaços de código pode ajuda a encontrar erros sutis. Se você faz uma alteração que você pensa qe não afeta o programa, e ela afeta, isto pode te dar uma dica.


-------------------------------
A.3 Erros de semântica
-------------------------------


De certa forma, os erros de semântica são os mais difíceis de depurar, porque o complador e o sistema de tempo de execução não fornecem informações sobre o que está errado. Somente você sabe o que o programa deveria fazer, e somente você sabe que ele não está fazendo isto.

O primeiro passo é fazeruma conexão entre o texto do programa e o comportamento que você está vendo. Você precisa de uma hipótese sobre o que o programa está realmente fazendo. Uma das coisas que dificultam é que os computadores trabalham muito rápido.

Você sempre desejará que pudesse diminuir a velocidade do programa para velocidade humana, e com alguns depuradores você pode. Mas o tempo que leva para inserir umas poucas declarações *print* bem colocadas é geralmente mais curto quando comparado a configurar um depurador, inserir e remover pontos de parada, e "caminhar" pelo programa até onde o erro ocorre.


=============================================================================
A.3.1 Meu programa não funciona
=============================================================================

Você deveria se fazer as seguintes perguntas:

 - Há alguma coisa que o programa deveria fazer mas que não parece que estar acontecendo?
 - Alguma coisa está acontecendo que nào deveria? Encontre o código no seu programa que executa a função e veja se ele está executando quando não deveria.
 - Uma seção de código está produzindo um efeito que nào éo que você esperava? Cetifique-se que você entende o código em questão, especialmente se ele envolve chamadas de funções ou métodos em outros módulos da linguagem. Leia a documentação para as funções que você chama. Teste-as escrevendo casos simples de teste e verificando os resultados.

Para programar, você precisa ter um modelo mental de como seus programas trabalham. Se você escreve um programa que não faz aquilo que você espera, e muito comum que o problema não esteja no programa; esteja no seu modelo mental.

A melhor maneira de corrigir seu modelo mental é quebrar o programa em seus componentes (geralmente as funções e métodos) e testar cada componente independentemente. Uma vez que você tenha encontrado a discrepância entre seu modelo e a realidade, você pode resolver o problema.

É claro, você deveria estar construindo e testando componentes à medida que você desenvolve o programa, Se você encontra um problema, deveria haver apenas uma pequena quantidade de novo código que não se sabe se está correto.


=============================================================================
A.3.2 Eu tenho uma grande expressão cabeluda e ela não faz o que eu espero
=============================================================================


Escrever expressões complexas é legal se elas forem legíveis, mas pode ser difícil de depurar. Geralmente é uma boa idéia quebrar uma expressão complexa em uma séria de atrbuições para variáveis temporárias.

Por exemplo:

>>> self.mao[i].adicionaCarta(self.mao[self.encontraVizinho(i)].popCarta())

Isto pode ser escrito como:

>>> 	vizinho = self.encontraVizinho(i)
	cartaPega = self.mao[vizinho].popCarta()
	self.mao[i].adicionaCarta(cartaPega)

A versão explícita é mais fácil de ler porque os nomes das variáveis fornecem documentação adicional, e é mais fácil depurar porque voc6e pode verificar os tipos das variáveis intermediárias e mostrar seus valores.

Um outro problema que pode ocorrer com expressões longas é que a ordem de avaliação pode não ser o que você espera. Por exemplo, se você está traduzido a expressão pi/2pi (**XXX fazer a equação matemática XXX**) para Python, você poderia escrever:

>>> y = x / 2 * math.pi

Isto está correto porque a multiplicaçã e a divisão possuem a mesma precedência e são avalidados da esquerda pra direita. Então a expressão computa *x*pi/2 (**XXX fazer a equação matemática XXX**).

Uma boa maneira de depurar expressões é adicionar parênteses para tornara a ordem de avaliação explícita:

>>> y = x / (2 * math.pi)

Sempre que voc6e não estiver seguro sobe a ordemde avaliação, utilize parênteses. Não apenas o programa estará correto(no sentido de fazer aquilo que você tinha a intenção),  ele também será mais legível por outras pessoas que não tenham memorizado as regras de precedência.


=============================================================================
A.3.3 Eu tenho uma função ou método que não devolve o que eu espero
=============================================================================


Se você possui uma declaração *return* com uma expressão complexa, voc6e não tema chance de exibir o valor de *return* ante sque ele seja devolvido. Novamente, você pode utilizar uma variavel temporária. Por exemplo, ao invés de: 

>>> 	return self.mao[i].devolveEncontrados()

você poderia escrever:

>>>	qtEncontrados = self.mao[i].devolveEncontrados()
	return qtEncontrados


Agora você tem a oportunidade de mostrar o valor de *qtEncontrados* antes de devolvê-lo.


=============================================================================
A.3.4 Eu estou empacado mesmo e eu preciso de ajuda
=============================================================================

Primeiro,tente sair da frente do computador por alguns minutos. Computadores emitem ondas que afetam o cérebro, causando estes efeitos:

 - Frustação e/ou raiva.
 - Crenças superticiosas ("o computador me odeia") e pensamentos mágicos ("o prorama só funciona quando eu coloco meu chapéu de trás pra frente").
 - Programação pelo caminhar-aleatório (a tentativa de programar escrevendo cada programa possível e escolhendo aquele que faz a coisa certa).

Se você se encontrar sofrendo de qualquer um destes sintomas, levante-se e vá dar uma caminhada. Quando você estiver calmo, pense no programa. O que ele está fazendo? Quais são as possíveis causas daquele comportamento? Quando foi a última vez que você teve um programa funcionando, e o que você fez depois disto?

Às vezes é uma questão de tempo pra se achar um erro. Nós geralmente encontramos os erros quando estamos longe do computador e deixamos nossa mente vaguear. Algns dos melhores lugares para encontrar erros são trens, chuveiros e na cama, logo antes de pegar no sono. 


=============================================================================
A.3.5 Não, eu preciso mesmo de ajuda
=============================================================================

Isto acontece. Mesmo os melhores programadores empacam de vez em quando. Às vezes você trabalha num programa por tanto tempo que não consegue ver o erro. Um par fresco de olhos é o que se precisa.

Antes de trazer mais alguém, certifique-se de que você tenha esgotado as técnicas descritas aqui. Seu programa deveria ser tão simples quanto possível, e você deveria estar trabalhando com a menor entrada que cause o erro. Você deveria ter declarações *print*  nos lugares apropriados (e a sua saída deveria ser compreensível). Você deveria entender o problema o suficiente para descerevê-lo de forma concisa.

Quando você trouxer alguém pra ajudar, assegure-se de lhes dar a informação de que eles necessitem:

 - Se existe uma mensagem de erro, o que é ela e que parte do programa ela indica?
 - Qual foi a última coisa que você fez antes deste erro acontecer? Quais foram as últimas linhas de código que você escreveu, ou qual é o novo caso de teste que falha?
 - O que você já tentou até o momento, e o que você aprendeu?

Quando você encontrar um erro, gaste um segundo para pensar sobre o que você poderia fazer para encontrá-lo mais rápido. Da próxima vez que você vir algo similar, você terá condições de encontrar o erro mais rapidamente.

Lembre-se, o objetivo não é apenas fazer o programa funcionar. O objetivo é aprender como fazer o programa funcionar.
