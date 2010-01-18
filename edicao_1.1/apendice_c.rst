.. $Id: apendice_c.rst,v 1.0 2009-04-08 21:40:00 francisco Exp $

=================================
Apêndice C: Leituras recomendadas
=================================

.. contents:: Tópicos

-------------------------------------
C.1 Recomendações para leitura
-------------------------------------

E agora, para onde você vai? Existem diversas direções que podem ser seguidas, aumentando o seu conhecimento especificamente em Python e/ou na ciência da computação em geral.

Os exemplos contidos neste livro foram deliberadamente simples, ou seja, eles podem não ter mostrado todo o potencial do Python. Abaixo uma lista de extensões e sugestões para projetos que usem Python:

    * Programar utilizando interfaces gráficas (GUI - graphical user interface) permite ao seu programa usar um ambiente de janelas para interagir com o usuário e exibir conteúdos gráficos (janelas, imagens, etc.) A biblioteca gráfica mais antiga para Python é o Tkinter, que é baseado no Tcl criado por Jon Ousterhout e na linguagem de script Tk. O Tkinter está incluso na distribuição padrão do Python, ou seja, quando instalamos o Python, o módulo do Tkinter é instalado também.

      Outra biblioteca famosa é o wxPython, que é essencialmente uma "folheagem" do Python sobre o wxWindows, uma biblioteca C++ que, por sua vez, implementa janelas usando a interfaces nativas nas plataformas Windows e Unix (incluindo Linux). As janelas e controles no wxPython tendem a ter um visual mais nativo do que no Tkinter e são mais um pouco mais simples de usar.
    
      Em qualquer biblioteca GUI que você usar, você usará a programação orientada a eventos, onde o usuário, e não o programador, determina o fluxo de execução. Este estilo de programação exige um novo costume que, por vezes, o obrigará a repensar toda a estrutura de um programa.

    * A programação web é um modelo de programação que integra o Python com a Internet. Por exemplo, você pode criar um cliente web que abre e lê uma página remota (quase) tão facilmente como você pode abrir um arquivo local. Existem, ainda, módulos para Python que permitem acesso remoto a arquivos utilizando FTP, e módulos que permitem você enviar e receber e-mails. Python também é usado (amplamente) para construir programas em servidores web com o intuito de tratar dados fornecidos por formulários.

    * Banco de dados são como super arquivos, que armazenam dados em esquemas predefinidos, e mantém relações entre itens de dados que lhe permitem acessar os dados de várias formas. Python tem vários módulos que possibilitam ao usuário conectar seus programas a diversos sistemas gerenciadores de banco de dados, tanto sistemas livres (Open source) quanto sistemas comerciais.

    * A programação multitarefa (multithread) permite que você execute várias tarefas (threads) dentro de um único programa. Se você já teve a experiência de usar um navegador web para se deslocar por uma página web enquanto o navegador ainda está carregando ela, então você já tem uma ideia do que da pra fazer usando a programação multitarefa.

    * Quando o desempenho é primordial, você pode escrever extensões para o Python em linguagens compiladas, como C e C++. Este abordagem é vastamente utilizada na biblioteca padrão do Python, formando a sua base. O mecanismo de ligação de dados e funções é um pouco complexo. Existe uma ferramenta, chamada SWIG (Simplified Wrapper and Interface Generator), que faz este processo de ligação ser mais simples.

-------------------------------------
C.2 Sites e livros sobre Python
-------------------------------------

Aqui estão algumas recomendações do autor de informações sobre Python na Internet:

    * A página oficial do Python (www.python.org) é o ponto de partida para pesquisa sobre qualquer material ligado a Python. Lá você encontrará ajuda, documentação, links para outros sites e listas de discussão nas quais você pode participar.

    * O Open Book Project (www.ibiblio.com/obp) contém não apenas este livro, mas também livros similares que abordam Java e C++, escritos por Allen Downey. Além disso, há aulas sobre Circuitos Elétricos feitas por Tony R. Kuphaldt; "Get down with ...", um conjunto de tutoriais sobre uma gama de tópicos em ciência da computação, escrito e editado por alunos de ensino médio; "Python for Fun", um conjunto de estudos de caso em Python, feito por Chris Meyers; e "The Linux Cookbook", escrito por Michael Stultz, com 300 páginas de dicas e técnicas.

    * Por último, se você for ao Google e buscar por "python -snake -monty", você encontrará cerca de 750 mil resultados.

E aqui estão alguns livros que contém material sobre Python:

    * Core Python Programming, escrito por Wesley Chun, é um grande livro com cerca de 750 páginas. A primeira párte do livro apresenta os recursos básicos do Python. A segunda parte traz uma introdução aos tópicos mais avançados, incluindo muitos dos mencionados acima.

    * Python Essential Reference, escrito por David M. Beazley, é um livro pequeno, mas que contém informações tanto da linguagem em si quanto dos módulos da biblioteca padrão. É também muito bem indexado.

    * Python Pocket Reference, escrito por Mark Lutz, este livro realmente cabe no seu bolso. Embora não seja tão abrangente quanto o "Python Essential Reference", "Python Pocket Reference" é uma referência para se ter em mãos o tempo todo, capaz de atender muito bem à explicação das funções e métodos mais comuns. Mark Luiz também é autor do livro "Programming Python", um dos primeiros (e maiores) livros sobre Python, e não visa o programador iniciante. Seu último livro, "Learning Python", é menor e mais acessível.

    * Python Programming on Win32, escrito por Mark Hammond e Andy Robinson, é um "tem que ter" para qualquer pessoa utilizando Python seriamente para desenvolver aplicações Windows. Entre outras coisas, o livro apresenta a integração entre Python e COM, cria uma pequena aplicação com wxPython, e ainda usar Python para criar scripts para aplicações como Word e Excel.

----------------------------------------------------
C.3 Livros de ciência da computação recomendados
----------------------------------------------------

As seguintes sugestões de leitura incluem muitos dos livros favoritos do autor. Eles lidam com as boas práticas de programação e ciência da computação em geral.

    * The Practice of Programming, escrito por Kernighan e Pike, abrange não apenas o projeto e a implementação de algoritmos e estrutura de dados, mas também depura, testa e melhora o desempenho de programas. Os exemplos são principalmente em C++ e Java, nenhum em Python.

    * The Elements of Java Style, editado por Al Vermeulen, é outro livro pequeno que discute alguns dos mais finos pontos de boas práticas de programação, como o bom uso de conveções, comentários, e ainda espaços em branco e endentação (o que não é um problema em Python). O livro também abrange programação por contrato, usando asserções para capturar erros testando precondições e poscondições, e programação adequada utilizando threads e sua sincronização.

    * Programming Pearls, escrito por Jon Bentley, é um livro clássico. O livro consiste de casos de estudo que originalmente apareceram na coluna do autor no site Communications of ACM (Association for Computing Machinery). Os estudos lidam com trade-offs em programação e por que isto é, muitas vezes, uma péssima idéia, especialmente para usar na sua primeira ideia para um programa. O livro é um pouco mais velho que os outros acima (1986), então os exemplos estão em linguagens antigas. Existem vários problemas para resolver, uns com solução e outros com dicas. O livro foi muito famoso e foi seguido por um segundo volume.

    * The New Turing Omnibus, escrito por A.K Dewdney, fornece uma leve introdução a 66 tópicos de ciência da computação, indo de computação paralela aos vírus de computador, de tomografias computadorizadas a algoritmos genéticos. Todos os tópicos são curtos e agradáveis. Um livro anterior escrito por Dewdney, The Armchair Universe, é uma coleção de sua coluna "Computer Recreations" (Brincadeiras computacionais) na revista Scientific American. Ambos os livros representam uma rica fonte de ideias para projetos.

    * Turtles, Termites and Traffic Jams, escrito por Mitchel Resnick, trata do poder de descentralização e como um comportamento complexo pode ocorrer a partir de simples atividades coordenadas, com um grande número de agentes. A execução do programa demonstra o comportamento complexo, que é, muitas vezes, contraintuitivo.

    * Gödel, Escher and Bach, escrito por Douglas Hofstadter. Simplificando, se você encontrar a magia na recursão, você vai encontrar também neste best-seller. Um dos temas abordados por Hofstadter envolve "loops estranhos" onde os padrões evoluem e ascendem até se encontrarem novamente. Esta é a controvérsia de Hofstadter, de que tais "loops estranhos" representam o elemento essencial que separa o animado do inanimado. Ele demonstra tais padrões na música de Bach, nos quadros de Escher e na incompletude dos teoremas de Gödel.
