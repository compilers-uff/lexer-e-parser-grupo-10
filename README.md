[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/4nHL7_6-)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=18898001&assignment_repo_type=AssignmentRepo)
# CS 164: Programming Assignment 1

[PA1 Specification]: https://drive.google.com/open?id=1oYcJ5iv7Wt8oZNS1bEfswAklbMxDtwqB
[ChocoPy Specification]: https://drive.google.com/file/d/1mrgrUFHMdcqhBYzXHG24VcIiSrymR6wt

Note: Users running Windows should replace the colon (`:`) with a semicolon (`;`) in the classpath argument for all command listed below.

## Getting started

Run the following command to generate and compile your parser, and then run all the provided tests:

    mvn clean package

    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy --pass=s --test --dir src/test/data/pa1/sample/

In the starter code, only one test should pass. Your objective is to build a parser that passes all the provided tests and meets the assignment specifications.

To manually observe the output of your parser when run on a given input ChocoPy program, run the following command (replace the last argument to change the input file):

    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy --pass=s src/test/data/pa1/sample/expr_plus.py

You can check the output produced by the staff-provided reference implementation on the same input file, as follows:

    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy --pass=r src/test/data/pa1/sample/expr_plus.py

Try this with another input file as well, such as `src/test/data/pa1/sample/coverage.py`, to see what happens when the results disagree.

## Assignment specifications

See the [PA1 specification][] on the course
website for a detailed specification of the assignment.

Refer to the [ChocoPy Specification][] on the CS164 web site
for the specification of the ChocoPy language. 

## Receiving updates to this repository

Add the `upstream` repository remotes (you only need to do this once in your local clone):

    git remote add upstream https://github.com/cs164berkeley/pa1-chocopy-parser.git

To sync with updates upstream:

    git pull upstream master


## Submission writeup

Team member 1: Gabriel Albuquerque

Team member 2: Pedro Trinkenreich

Team member 3: Victor Filgueira

Que estratégia você usou para emitir tokens INDENT e DEDENT corretamente? Mencione o nome do arquivo e o(s) número(s) da(s) linha(s) para a parte principal da sua solução.

R:) 

A estratégia é mais simples: basicamente, o lexer conta os espaços ou tabulações no início de cada linha e usa uma pilha para guardar o "nível" atual de indentação. Se uma nova linha começar com mais espaços do que o valor atual da pilha, isso significa que você entrou num novo bloco – aí, ele empurra o novo nível na pilha e emite um token INDENT. Se começar com a mesma quantidade, não faz nada (por que o código está na mesma IDENTAÇÃO); mas se tiver menos, é sinal de que você saiu de um ou mais blocos, então o lexer desempilha os níveis necessários e, para cada nível que sai, emite um token DEDENT. Essa abordagem ajuda a identificar onde os blocos de código começam e terminam, da mesma forma que o Python faz, mas sem chaves ou outros delimitadores explícitos.

A parte central dessa estratégia está implementada no arquivo chocopy.jflex. Em especial, a regra no estado <YYINITIAL> para {InputCharacter} (ou seja, quando é detectado o primeiro caracter não branco numa nova linha) contém a lógica de comparação do nível atual com o topo da pilha e a emissão dos tokens INDENT ou DEDENT. Na especificação apresentada, essa lógica central encontra-se aproximadamente entre as linhas 107 à 120 do arquivo.


Como sua solução ao item 1. se relaciona ao descrito na seção 3.1 do manual de referência de ChocoPy? (Arquivo chocopy_language_reference.pdf.)

R:)

A minha solução implementa o controle de indentação através do uso de uma pilha, e comparado com o nível de indentação armazenado no topo da pilha. Essa abordagem é diretamente inspirada na ideia apresentada na seção 3.1 do manual de referência de ChocoPy, que explica como a estrutura física das linhas (com NEWLINE, INDENT e DEDENT) reflete a estrutura lógica do programa.

Conforme descrito na seção 3.1, o lexer deve interpretar o fim de uma linha (NEWLINE) e, ao iniciar uma nova linha, deve calcular a quantidade de espaços em branco (indentação) e gerar um token INDENT caso a indentação aumente em relação à linha anterior, ou um token DEDENT caso ela diminua. No meu lexer (arquivo chocopy.jflex), essa lógica se encontra na regra que processa o primeiro caractere não branco de uma linha ({InputCharacter})


Qual foi a característica mais difícil da linguagem (não incluindo identação) neste projeto? Por que foi um desafio? Mencione o nome do arquivo e o(s) número(s) da(s) linha(s) para a parte principal de a sua solução.

R:)

Lidar com atribuições múltiplas e encadeadas, como:
x[0] = y = z.f = 1

Esse tipo de construção exige que o parser reconheça vários targets em uma única linha e associe todos ao mesmo valor final. Isso vai além de uma atribuição binária e exige que a gramática produza um nó AssignStmt com uma lista de targets e um value.

POR EXEMPLO:
Se simple_stmt ::= target:e EQ expr:e
               {: RESULT = new AssignStmt(...); :}
Essa versão não reconheceria y = z.f = True, e ao encontrar o segundo =, geraria um erro "Parse error near token EQ: =":

Então, criamos uma regra recursiva target_list1 que acumula múltiplos alvos separados por =:
Implementar isso corretamente envolveu:
    1) Ajustar a regra simple_stmt ::= target_list1 expr no ChocoPy.cup para construir a AST.

    2) Construir a produção target_list1 de forma recursiva, acumulando os alvos corretamente em ordem.

    3) Gerenciar as localizações de forma precisa com getLeft() e exright para formar o nó AssignStmt.

target_list1 e simple_stmt -> linha 375 até 395
member_expr, target e index_expr -> linha 507 até 527


#gerar ast
java -cp "chocopy-ref.jar;target/assignment.jar" chocopy.ChocoPy --pass=r src/test/data/pa1/sample/<input>.py
java -cp "chocopy-ref.jar;target/assignment.jar" chocopy.ChocoPy --pass=r \src\test\data\pa1\student_contributed\ 
#compilar
mvn clean package

#testar tudo
java -cp "chocopy-ref.jar;target/assignment.jar" chocopy.ChocoPy --pass=s --test --dir src/test/data/pa1/sample/