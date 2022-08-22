# Python docs 
#   - online em https://python.org/doc ou https://docs.python.org/pt-br/3.10/#
#   - Download: https://docs.python.org/pt-br/3.10/download.html
#   - Especificamente sobre arquivos: https://docs.python.org/pt-br/3.10/tutorial/inputoutput.html#reading-and-writing-files

#==============================================
# Manipulação de Arquivos em Python ===========
#==============================================

#-- 1 ---------------------------------------------------------------------------------------------------------
# Abrindo arquivo existente
#   A função open(path, mode) recebe dois parâmetros: path e mode. O primeiro se refere ao caminho de onde está 
# o arquivo a ser aberto. Já o segundo, se refere ao modo de acesso. A seguir, alguns modos de acesso:
#   - r : read / leitura
#   - w : write / escrita -> sobrescreve ou cria um novo
#   - r+ : read and write / leitura + escrita
#   - w+ : write and read / escrita + leitura
#   - a : append / acrescenta no fim
#   - a+ : append / acrescento no início
#
#                     | r   r+   w   w+   a   a+
#   ------------------|--------------------------
#   read              | +   +        +        +
#   write             |     +    +   +    +   +
#   write after seek  |     +    +   +
#   create            |          +   +    +   +
#   truncate          |          +   +
#   position at start | +   +    +   +
#   position at end   |                   +   +  
#
#   'after seek': significa que você pode definir o byte onde vai começar a operação. Por exemplo: arquivo.write(2).
#   'truncate': significa que o arquivo vai ser sobrescrito.
#   
#   Como estou utilizando o VSCode, tenho como workspace a pasta VS_Workspace, o qual é tido como o início do caminho 
# (path). Portanto, basta escrever o caminho do arquivo dentro do workspace.
#
#   A função open() retorna o arquivo pedido, com o respectivo modo de acesso. Por isso é necessário uma variável para 
# 'receber' esse arquivo. No nosso caso, o nome da variável é 'arquivo', mas poderia ser qualquer outra palavra, desde 
# que não seja alguma já reservada (exemplo de palavra reservada: if). A partir de então, é possível manipular o arqui
# vo a partir da variável.
#
#   É interessante sempre escrever logo o '.close()', para evitar problemas. Caso a execução seja interrompida, ou fina
# lizada normalmente, sem que o arquivo seja fechado, você terá problemas para acessá-lo, mesmo com outro programa, como 
# o bloco de notas.
#
##arquivo = open("RAD em Python/teste.txt", "r")
#
##print(arquivo.readable())  # imprimindo a verificação se o arquivo pode ser lido
##print(arquivo.read())      # imprimindo o arquivo
#
#   readline() lê uma linha e deixa o 'cursor' na linha seguinte. Portanto, uma sequência de readline() vai retornar sem
# pre a linha seguinte. Com o print(), a leitura de cada linha é impressa. Como cada linha do arquivo que está sendo lido 
# termina com '\n' (quebra de linha) o resultado de cada readline() vai ter a seguir uma linha em branco.
#
##print(arquivo.readline())
##print(arquivo.readline())
##print(arquivo.readline())
#
#   A função readlines() retorna uma lista, onde cada elemento da lista é o conteúdo de uma linha. Essa lista está sendo ar
# mazenada na variável lista. A partir daí podemos manipular a lista. Perceba que manipulando a lista, mesmo que apagando ele
# mentos, não vai afetar o arquivo.
#
##lista = arquivo.readlines()
##print(lista)
#
#   Outra maneira de imprimir uma lista é utilizando o comando for. Da maneira que foi escrita, este for funciona como o 'for 
# each' (para cada) de outras linguagens. Então, o código está dizendo mais ou menos assim: para cada elemento da lista, visto 
# como l : ...
#
#   Outra peculiaridade do Python é a sua necessidade de identação. Isto porque, como você já deve ter notado, não temos ponto 
# e vírgula para definir o fim de uma linha, ou { e } para definir o escopo de um bloco. Portanto, todo bloco em Python inicia 
# com a 'chamada' do bloco seguido de dois pontos. No nosso caso, a 'chamada' é o for, ou seja, a chamada de um bloco de repeti
# ção. Seguido do for temos o :. Após os dois pontos, para que o interpretador do Python saibda que uma linha faz parte do bloco,
# é necessário que aquela linha comece 'tabulada', ou seja, deslocada para o lado. Por isso, o print(l) é visto como uma linha 
# dentro do for. A primeira após o bloco cujo código não esteja deslocado, o interpretador já vai entender como um comando que não
# pertence ao for.
#
##for l in lista: 
##    print(l)
#
##arquivo.close()
#--------------------------------------------------------------------------------------------------------------

#-- 2 ---------------------------------------------------------------------------------------------------------
#   Abrinda um arquivo existente com o modo de acesso 'append'. A partir disso é possível acrescentar conteúdo ao arquivo. No 
# nosso caso, criamos um comando para que fosse escrito "\nSQL". Quando o arquivo é aberto em modo 'a' a nova escrita vai ini
# ciar no espaço seguinte ao último já existente. No nosso exemplo, em teste.txt, tínhamos como último elemento a palavra Matlab.
# Com o append, a nova escrita começaria colado ao Matlab. Porém, como escrevemos o \n, vai haver primeiro uma quebra de linha. 
# O SQL é escrito logo após a quebra de linha.
#
##arquivo = open("RAD em Python/teste.txt", "a")
##arquivo.write("\nSQL")
##arquivo.write("\nR\n")
##arquivo.close()
#--------------------------------------------------------------------------------------------------------------

#-- 3 ---------------------------------------------------------------------------------------------------------
#   Caso o modo de escrita seja 'selecionado', e o arquivo pedido não exista, então ele será criado. É importan te lembrar também
# que, caso o arquivo já exista, com este modo de acesso, o coonteúdo dele será sobrescrito.
#
##arquivo = open("RAD em Python/teste2.txt", "w")
##arquivo.write("Portugol\n")
##arquivo.write("ADA\n")
##arquivo.write("C#")
##arquivo.close()
#--------------------------------------------------------------------------------------------------------------

#-- 4 ---------------------------------------------------------------------------------------------------------
#   A remoção de arquivos pode ser feita com a importação do módulo 'os' (de operating system, ou sistema operacional).
# Esse módulo provê uma interface para funcionalidades dependentes do sistema operacional.
#
##import os # Apesar de ser nativo do Python, precisa ser explicitamente importado
#
#   Verificando se um arquivo existe. Caso positivo, o arquivo é removido. Senão, é impressa a mensagem.
##if os.path.exists("RAD em Python/teste3.txt"):
##    os.remove("RAD em Python/teste3.txt")
##else:
##    print("ESTO NON ECZISTE")
#--------------------------------------------------------------------------------------------------------------

#-- 5 ---------------------------------------------------------------------------------------------------------
# Da mesma forma, ou seja, com o uso do módulo 'os', é possível criar e remover pastas. Entretanto, a remoção só é
# possível se a pasta estiver vazia.
#
##os.mkdir("RAD em Python/TESTE")
##os.rmdir("RAD em Python") # Só remove se estiver vazia