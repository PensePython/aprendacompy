.. $Id: prefacio.rst,v 2.1 2007-04-23 21:17:42 luciano Exp $

========
Prefácio
========

Por Jeff Elkner

Este livro deve sua existência à colaboração possibilitada pela Internet e pelo movimento do software livre. Seus três autores -- um professor universitário, um professor secundarista e um programador profissional -- ainda não se encontraram pessoalmente, mas temos sido capazes de trabalhar em estreita colaboração e temos sido ajudados por muitos colegas maravilhosos que têm dedicado seu tempo e energia para ajudar a fazer deste um livro cada vez melhor.

Achamos que este livro é um testemunho dos benefícios e possibilidades futuras deste tipo de colaboração, cujo modelo tem sido posto em prática por Richard Stallman e pela Free Software Foundation.

----------------------------------------------
Como e porque eu vim a usar Python
----------------------------------------------

Em 1999, o Exame de Colocação Avançada em Ciência da Computação da Comissão de Faculdades  (College Board's Advanced Placement (AP) Computer Science XXX) foi aplicado em C++ pela primeira vez. Como em muitas escolas secundárias através do país, a decisão de mudar linguagens teve um impacto direto no currículo de ciência da computação na Yorktown High School em Arlington, Virginia, onde leciono. Até então, Pascal era a linguagem didática para nossos cursos de primeiro ano e avançado. Mantendo a prática corrente de dar aos estudantes dois anos de exposição à mesma linguagem, tomamos a decisão de mudar para C++ no curso de primeiro ano para o ano letivo de 1997-98 de modo que estaríamos em sincronismo com a mudança da Comissão de Faculdades (College Board's XXX) em relação ao curso avançado (AP XXX) para o ano seguinte.

Dois anos depois, eu estava convencido que C++ foi uma escolha infeliz para introduzir os alunos em ciência da computação. Ao mesmo tempo em que é certamente uma linguagem de programação muito poderosa, também é uma linguagem extremamente difícil de aprender e de ensinar. Eu me encontrava constantemente lutando com a sintaxe difícil de C++ e as múltiplas maneiras de fazer a mesma coisa, e estava, como resultado, perdendo muitos alunos desnecessariamente. Convencido de que deveria existir uma linguagem melhor para a nossa classe de primeiro ano, fui procurar por uma alternativa a C++.

Eu precisava de uma linguagem que pudesse rodar nas máquinas em nosso laboratório Linux bem como nas plataformas Windows e Macintosh que a maioria dos alunos tinha em casa. Eu precisava que ela fosse gratuita e disponível eletronicamente, assim os alunos poderiam utilizá-la em casa independentemente de suas rendas. Eu queria uma linguagem que fosse utilizada por programadores profissionais, e que tivesse uma comunidade de desenvolvimento ativa em torno dela. Ela teria que suportar ambas, programação procedural e orientada a objetos. E, mais importante, deveria ser fácil de aprender e de ensinar. Quando considerei as alternativas tendo em mente aquelas metas, Python sobressaiu-se como a melhor candidata para a tarefa.

Pedi para um dos talentosos estudantes de Yorktown, Matt Ahrens, que experimentasse Python. Em dois meses ele não só aprendeu a linguagem como também escreveu uma aplicação chamada pyTicket que possibilitou à nossa equipe reportar problemas de tecnologia pela Web. Eu sabia que Matt não poderia ter finalizado uma aplicação daquele porte em período tão curto em C++, e esta realização, combinada com a avaliação positiva de Python dada por Matt, sugeriam que Python era a solução que eu estava procurando.

---------------------------------------
Encontrando um livro-texto
---------------------------------------

Tendo decidido usar Python em minhas aulas introdutórias de ciência da computação do ano seguinte, o problema mais urgente era a falta de um livro-texto disponível.

O conteúdo livre veio em socorro. Anteriormente naquele ano, Richard Stallman tinha me apresentado a Allen Downey. Ambos havíamos escrito a Richard expressando interesse em desenvolver conteúdo educacional livre. Allen já tinha escrito um livro-texto para o primeiro ano de ciência da computação, *How to Think Like a Computer Scientist*. Quando li este livro, soube imediatamente que queria utilizá-lo nas minhas aulas. Era o mais claro e proveitoso texto em ciência da computação que eu tinha visto. Ele enfatizava o processo de reflexão envolvido em programação em vez de características de uma linguagem em particular. Lê-lo fez de mim imediatamente um professor melhor.

O *How to Think Like a Computer Scientist* era não só um excelente livro, como também fora lançado sob uma licença pública GNU, o que significava que ele poderia ser usado livremente e modificado para atender as necessidades de seu usuário. Uma vez que eu havia decidido usar Python, me ocorreu que eu poderia traduzir a versão original do livro de Allen do Java para a nova linguagem. Apesar de não estar capacitado para escrever eu mesmo um livro-texto, tendo o livro de Allen para trabalhar, tornou possível para mim fazê-lo, ao mesmo tempo demonstrando que o modelo de desenvolvimento cooperativo tão bem utilizado em software poderia também funcionar para conteúdo educacional.

Trabalhar neste livro pelos últimos dois anos tem sido recompensador para mim e meus alunos, e eles tiveram um grande papel neste processo. A partir do momento em que eu podia fazer mudanças instantâneas assim que alguém encontrasse um erro ortográfico ou um trecho difícil, eu os encorajei a procurar por erros no livro, dando a eles pontos de bonificação cada vez que fizessem uma sugestão que resultasse em uma mudança no texto. Isto teve o duplo benefício de encorajá-los a ler o texto mais cuidadosamente e de ter o texto totalmente revisado por seus críticos mais importantes: alunos utilizando-o para aprender ciência da computação.

Para a segunda metade do livro, sobre programação orientada a objetos, eu sabia que seria preciso alguém com uma maior experiência do que a minha em programação real para fazê-lo corretamente. O livro esteve em estado inacabado por quase um ano até que a comunidade de software livre providenciasse mais uma vez os meios necessários para sua conclusão.

Eu recebi um e-mail de Chris Meyers mostrando interesse no livro. Chris é um programador profissional que começou a dar um curso de programação no ano anterior usando Python no Lane Community College em Eugene, Oregon. A perspectiva de dar aquele curso ligou Chris ao livro, e ele começou a ajudar o trabalho imediatamente. Até o final do ano letivo ele tinha criado um projeto colaborativo em nosso Website em ``http://www.ibiblio.org/obp`` chamado *Python for Fun* e estava trabalhando com alguns dos meus alunos mais avançados como um guru (master teacher XXX), guiando-os além de onde eu poderia levá-los.

----------------------------------------
Introduzindo programação com Python
----------------------------------------

O processo de traduzir e utilizar *How to Think Like a Computer Scientist* pelos últimos dois anos tem confirmado a conveniência de Python no ensino de alunos iniciantes. Python simplifica tremendamente os programas exemplo e torna idéias importantes de programação mais fáceis de ensinar.

O primeiro exemplo do texto ilustra este ponto. É o tradicional programa "Alô mundo", o qual na versão C++ do livro se parece com isto::

   #include <iostream.h>

   void main()
   {
     cout << "Alô, mundo." << endl;
   }

Na versão Python, ele se transforma em::

   print "Alô, Mundo!"

Mesmo sendo um exemplo trivial, as vantagens do Python saltam aos olhos. O curso de Ciência da Computação I que ministro em Yorktown não tem pré-requisitos, assim, muitos dos alunos que veem esse exemplo estão olhando para o seu primeiro programa. Alguns deles estão indubitavelmente nervosos, por já terem ouvido falar que programação de computadores é difícil de aprender. A versão C++ tem sempre me forçado a escolher entre duas opções insatisfatórias: ou explicar os comandos ``#include``, ``void`` ``main()``, ``{``, e ``}`` e arriscar confundir ou intimidar alguns dos alunos logo assim que iniciam, ou dizer a eles "Não se preocupem com todas estas coisas agora; falaremos sobre elas mais tarde," e correr o mesmo risco. O objetivo educacional neste ponto do curso é introduzir os alunos à idéia de comando em programação e vê-los escrever seu primeiro programa, deste modo introduzindo-os ao ambiente de programação. O programa em Python tem exatamente o que é necessário para conseguir isto, e nada mais.

Comparar o texto explicativo do programa em cada versão do livro ilustra ainda mais o que significa para o aluno iniciante. Existem treze parágrafos de explicação do "Alô, mundo!" na versão C++; na versão Python existem apenas dois. Mais importante, os onze parágrafos perdidos não se ocupam das "idéias chave" da programação de computadores, mas com a minúcia da sintaxe C++. Vejo a mesma coisa acontecendo através de todo o livro. Parágrafos inteiros simplesmente desaparecem da versão Python do texto porque a sintaxe muito mais clara de Python os torna desnecessários.

Utilizar uma linguagem de tão alto nível como Python, permite ao professor deixar para falar mais tarde sobre os níveis mais baixos, próximos à máquina, quando os alunos já terão a experiência necessária para ver com mais sentido os detalhes. Desta maneira podemos pedagogicamente "por em primeiro lugar as primeiras coisas". Um dos melhores exemplos disto é a maneira com que Python lida com variáveis. Em C++ uma variável é um nome para um lugar que guarda uma coisa. Variáveis têm de ser declaradas com seu tipo pelo menos em parte por que o tamanho do lugar a que se referem precisa ser predeterminado. Assim, a idéia de variável fica amarrada ao hardware da máquina. O conceito poderoso e fundamental de variável já é bastante difícil para o aluno iniciante (tanto em ciência da computação quanto em álgebra). Bytes e endereços não ajudam neste caso. Em Python uma variável é um nome que se refere a uma coisa. Este é um conceito muito mais intuitivo para alunos iniciantes e está muito mais próximo do significado de "variável" que eles aprenderam em seus cursos de matemática. Eu tive muito menos dificuldade em ensinar variáveis este ano do que tive no passado, e gastei menos tempo ajudando aos alunos com problemas no uso delas.

Um outro exemplo de como Python ajuda no ensino e aprendizagem de programação é em sua sintaxe para função. Meus alunos têm sempre tido grande dificuldade na compreensão de funções. O problema principal gira em torno da diferença entre a definição de uma função e a chamada de uma função, e a distinção relacionada entre um parâmetro e um argumento. Python vem em auxílio com uma sintaxe não apenas curta quanto bela. As definições de função começam com ``def``, então eu simplesmente digo aos meus alunos "Quando você define uma função, comece com ``def``, seguido do nome da função que você está definindo; quando você chama uma função, simplesmente chame-a digitando o nome dela". Parâmetros ficam nas definições; argumentos vão com as chamadas. Não existem tipos de retorno, tipos de parâmetro ou passagem de parâmetros por valor ou por referência no meio do caminho, permitindo-me ensinar funções em menos da metade do tempo que isto me tomava anteriormente, com uma melhor compreensão.

A utilização do Python tem melhorado a efetividade de nosso programa em ciência da computação para todos os estudantes. Eu vejo um nível geral de sucesso muito mais alto e um nível mais baixo de frustração do que experimentei durante os dois anos em que ensinei C++. Eu avanço mais rápido com melhores resultados. Mais alunos deixam o curso com a habilidade de criar programas significativos e com uma atitude positiva em relação a experiência de programação que isso traz.

--------------------------------------
Construindo uma comunidade
--------------------------------------

Tenho recebido e-mails de todo o planeta de pessoas utilizando este livro para aprender ou ensinar programação. Uma comunidade de usuários tem começado a emergir e muitas pessoas têm contribuído com o projeto enviando seus materiais para o Website cooperativo em:

``http://www.thinkpython.com``

Com a publicação do livro em formato impresso, minha expectativa quanto ao crescimento da comunidade de usuários é que ela seja contínua e acelerada. O surgimento desta comunidade de usuários e a possibilidade que sugere de colaboração semelhante entre educadores tem sido para mim a parte mais excitante do trabalho neste projeto. Trabalhando juntos, podemos aumentar a qualidade do material disponível para o nosso uso e poupar tempo valioso. Eu convido você a se juntar a nossa comunidade e espero ouvir algo de você. Por favor, escreva para os autores em ``feedback@thinkpython.com``.


Jeffrey Elkner

Yorktown High School

Arlington, Virginia
